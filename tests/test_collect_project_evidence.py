from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
COLLECTOR_PATH = (
    REPOSITORY_ROOT
    / ".agents/skills/document-software-project/scripts/collect_project_evidence.py"
)

SPEC = importlib.util.spec_from_file_location("collect_project_evidence", COLLECTOR_PATH)
assert SPEC and SPEC.loader
COLLECTOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(COLLECTOR)


class EvidenceCollectorTests(unittest.TestCase):
    def create_fixture(self, root: Path) -> None:
        (root / ".github/workflows").mkdir(parents=True)
        (root / ".specify/specs/001-login").mkdir(parents=True)
        (root / "README.md").write_text("# Test project\n", encoding="utf-8")
        (root / "package.json").write_text(
            '{"name":"test-project","private":true}\n', encoding="utf-8"
        )
        (root / ".env").write_text(
            "REAL_SECRET=must-not-appear\n", encoding="utf-8"
        )
        (root / ".env.example").write_text(
            "PUBLIC_API_URL=https://example.invalid\n"
            "API_TOKEN=replace-with-a-placeholder\n",
            encoding="utf-8",
        )
        (root / ".specify/specs/001-login/spec.md").write_text(
            "# Login specification\n", encoding="utf-8"
        )
        (root / "openapi.yaml").write_text(
            "openapi: 3.1.0\ninfo:\n  title: Test\n  version: 1.0.0\npaths: {}\n",
            encoding="utf-8",
        )
        (root / "Dockerfile").write_text("FROM scratch\n", encoding="utf-8")
        (root / ".github/workflows/test.yml").write_text(
            "name: Test\non: [push]\njobs: {}\n", encoding="utf-8"
        )

    def run_collector(self, root: Path, output_format: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(COLLECTOR_PATH),
                "--root",
                str(root),
                "--format",
                output_format,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_json_excludes_real_environment_file_and_value(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.create_fixture(root)

            result = self.run_collector(root, "json")

            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(result.stdout)
            serialized = json.dumps(data)
            self.assertNotIn("REAL_SECRET", serialized)
            self.assertNotIn("must-not-appear", serialized)
            self.assertIn("API_TOKEN", serialized)
            self.assertIn("PUBLIC_API_URL", serialized)
            self.assertEqual(data["inventory"]["files_inspected_by_path"], 7)

    def test_detects_specification_and_project_signals(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.create_fixture(root)

            result = self.run_collector(root, "json")
            data = json.loads(result.stdout)

            self.assertIn(
                ".specify/specs/001-login/spec.md",
                data["specification_artifacts"],
            )
            self.assertIn("openapi.yaml", data["signals"]["api_contracts"])
            self.assertIn("Dockerfile", data["signals"]["containers"])
            self.assertIn(
                ".github/workflows/test.yml",
                data["signals"]["ci"],
            )
            self.assertIn("package.json", data["manifests"])

    def test_markdown_explains_inventory_limits(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.create_fixture(root)

            result = self.run_collector(root, "markdown")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("# Project evidence inventory", result.stdout)
            self.assertIn("This inventory proves only", result.stdout)
            self.assertNotIn("must-not-appear", result.stdout)

    def test_does_not_follow_symlinked_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.create_fixture(root)
            external = root.parent / f"{root.name}-external-secret.txt"
            external.write_text("EXTERNAL_SECRET=hidden\n", encoding="utf-8")
            link = root / "linked-secret.txt"
            try:
                link.symlink_to(external)
            except OSError:
                self.skipTest("symlinks are not available in this environment")
            try:
                result = self.run_collector(root, "json")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotIn("linked-secret.txt", result.stdout)
                self.assertNotIn("EXTERNAL_SECRET", result.stdout)
            finally:
                external.unlink(missing_ok=True)

    def test_invalid_root_returns_error(self) -> None:
        result = self.run_collector(
            REPOSITORY_ROOT / "path-that-does-not-exist",
            "json",
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("project root is not a directory", result.stderr)


if __name__ == "__main__":
    unittest.main()
