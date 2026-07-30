#!/usr/bin/env python3
"""Collect a safe, shallow evidence inventory for software documentation work."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable


SKIP_DIRS = {
    ".cache",
    ".git",
    ".hg",
    ".idea",
    ".next",
    ".nuxt",
    ".pytest_cache",
    ".ruff_cache",
    ".svn",
    ".terraform",
    ".tox",
    ".venv",
    ".vite",
    ".yarn",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
}

SENSITIVE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    ".env.development",
    ".npmrc",
    ".pypirc",
    "credentials",
    "credentials.json",
    "id_rsa",
    "id_ed25519",
    "secrets.yml",
    "secrets.yaml",
}

SENSITIVE_SUFFIXES = {
    ".der",
    ".jks",
    ".key",
    ".p12",
    ".pem",
    ".pfx",
}

DOC_SUFFIXES = {".md", ".mdx", ".rst", ".adoc", ".txt"}

MANIFEST_NAMES = {
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "poetry.lock",
    "uv.lock",
    "Pipfile",
    "go.mod",
    "Cargo.toml",
    "composer.json",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "Gemfile",
    "mix.exs",
}

CONFIG_PATTERNS = {
    "containers": (
        re.compile(r"(^|/)(Dockerfile[^/]*)$"),
        re.compile(r"(^|/)(docker-compose|compose)\.ya?ml$"),
    ),
    "ci": (
        re.compile(r"^\.github/workflows/.+\.ya?ml$"),
        re.compile(r"(^|/)\.gitlab-ci\.ya?ml$"),
        re.compile(r"(^|/)Jenkinsfile$"),
        re.compile(r"^\.circleci/config\.ya?ml$"),
        re.compile(r"^azure-pipelines\.ya?ml$"),
    ),
    "infrastructure": (
        re.compile(r"\.tf$"),
        re.compile(r"(^|/)wrangler\.(toml|jsonc?)$"),
        re.compile(r"(^|/)serverless\.ya?ml$"),
        re.compile(r"(^|/)vercel\.json$"),
        re.compile(r"(^|/)netlify\.toml$"),
        re.compile(r"(^|/)fly\.toml$"),
        re.compile(r"(^|/)(Chart\.yaml|kustomization\.ya?ml)$"),
    ),
    "api_contracts": (
        re.compile(r"(^|/)(openapi|swagger).*\.(json|ya?ml)$", re.I),
        re.compile(r"\.(graphql|gql|proto)$", re.I),
        re.compile(r"(^|/)asyncapi.*\.(json|ya?ml)$", re.I),
    ),
    "database": (
        re.compile(r"(^|/)schema\.prisma$"),
        re.compile(r"(^|/)(migrations?|db/migrate)/"),
        re.compile(r"(^|/)(schema|database)\.sql$"),
    ),
    "tests": (
        re.compile(r"(^|/)(tests?|spec|__tests__)/"),
        re.compile(r"(\.|_)(test|spec)\.[^.]+$", re.I),
    ),
}

SPEC_PATH_PATTERNS = (
    re.compile(r"(^|/)\.specify/"),
    re.compile(r"(^|/)specs?/"),
    re.compile(r"(^|/)openspec/"),
    re.compile(r"(^|/)\.kiro/specs?/"),
    re.compile(r"(^|/)requirements?/"),
    re.compile(r"(^|/)features?/.*\.feature$", re.I),
    re.compile(r"(^|/)(rfcs?|adrs?)/", re.I),
)

ENV_EXAMPLE_RE = re.compile(
    r"(^|/)(\.env(\.[A-Za-z0-9_-]+)*\.(example|sample|template)|"
    r"\.env\.(example|sample|template)|env\.example)$",
    re.I,
)
ENV_KEY_RE = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=")


def is_sensitive(path: Path) -> bool:
    name = path.name.lower()
    if name in SENSITIVE_NAMES:
        return True
    if path.suffix.lower() in SENSITIVE_SUFFIXES:
        return True
    if name.startswith(".env") and not ENV_EXAMPLE_RE.search(path.as_posix()):
        return True
    return False


def walk_files(root: Path, max_files: int) -> tuple[list[Path], bool]:
    files: list[Path] = []
    truncated = False
    for current, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(
            d
            for d in dirs
            if d not in SKIP_DIRS
            and not (Path(current) / d).is_symlink()
        )
        for name in sorted(names):
            path = Path(current) / name
            if path.is_symlink() or is_sensitive(path):
                continue
            files.append(path)
            if len(files) >= max_files:
                truncated = True
                return files, truncated
    return files, truncated


def relative_paths(root: Path, paths: Iterable[Path]) -> list[str]:
    return sorted(path.relative_to(root).as_posix() for path in paths)


def safe_git(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    return value or None


def read_env_keys(path: Path) -> list[str]:
    keys: list[str] = []
    try:
        with path.open("r", encoding="utf-8", errors="replace") as stream:
            for line in stream:
                match = ENV_KEY_RE.match(line)
                if match:
                    keys.append(match.group(1))
    except OSError:
        return []
    return sorted(set(keys))


def detect(files: list[Path], root: Path) -> dict[str, object]:
    rel = {path: path.relative_to(root).as_posix() for path in files}
    docs = [
        path
        for path in files
        if path.suffix.lower() in DOC_SUFFIXES
        and (
            path.name.lower().startswith(("readme", "contributing", "changelog"))
            or "doc" in {part.lower() for part in path.relative_to(root).parts}
            or any(pattern.search(rel[path]) for pattern in SPEC_PATH_PATTERNS)
        )
    ]
    specs = [
        path
        for path in files
        if any(pattern.search(rel[path]) for pattern in SPEC_PATH_PATTERNS)
    ]
    manifests = [path for path in files if path.name in MANIFEST_NAMES]

    signals: dict[str, list[str]] = defaultdict(list)
    for path, relative in rel.items():
        for category, patterns in CONFIG_PATTERNS.items():
            if any(pattern.search(relative) for pattern in patterns):
                signals[category].append(relative)

    instructions = [
        path
        for path in files
        if path.name in {"AGENTS.md", "CONTRIBUTING.md", "CONTRIBUTING.rst"}
        or path.name.lower().startswith("readme")
    ]

    env_examples: dict[str, list[str]] = {}
    for path, relative in rel.items():
        if ENV_EXAMPLE_RE.search(relative):
            env_examples[relative] = read_env_keys(path)

    top_level = sorted(
        item.name + ("/" if item.is_dir() else "")
        for item in root.iterdir()
        if item.name not in SKIP_DIRS
        and not item.is_symlink()
        and not is_sensitive(item)
    )

    return {
        "project": {
            "root_name": root.name,
            "git_repository": safe_git(root, "rev-parse", "--is-inside-work-tree")
            == "true",
            "git_branch": safe_git(root, "branch", "--show-current"),
            "top_level_entries": top_level,
        },
        "instructions_and_entry_docs": relative_paths(root, instructions),
        "documentation_files": relative_paths(root, docs),
        "specification_artifacts": relative_paths(root, specs),
        "manifests": relative_paths(root, manifests),
        "signals": {key: sorted(values) for key, values in sorted(signals.items())},
        "safe_environment_examples": env_examples,
    }


def as_markdown(data: dict[str, object], file_count: int, truncated: bool) -> str:
    project = data["project"]
    assert isinstance(project, dict)
    lines = [
        "# Project evidence inventory",
        "",
        f"- Root name: `{project['root_name']}`",
        f"- Git repository: `{str(project['git_repository']).lower()}`",
        f"- Git branch: `{project['git_branch'] or 'not detected'}`",
        f"- Files inspected by path: `{file_count}`",
        f"- Inventory truncated: `{str(truncated).lower()}`",
    ]

    def add_list(title: str, values: object) -> None:
        lines.extend(["", f"## {title}", ""])
        if not values:
            lines.append("- None detected")
            return
        assert isinstance(values, list)
        lines.extend(f"- `{value}`" for value in values)

    add_list("Top-level entries", project["top_level_entries"])
    add_list("Instructions and entry documentation", data["instructions_and_entry_docs"])
    add_list("Documentation files", data["documentation_files"])
    add_list("Specification artifacts", data["specification_artifacts"])
    add_list("Build and dependency manifests", data["manifests"])

    lines.extend(["", "## Project signals", ""])
    signals = data["signals"]
    assert isinstance(signals, dict)
    if not signals:
        lines.append("- None detected")
    else:
        for category, values in signals.items():
            lines.append(f"### {category.replace('_', ' ').title()}")
            lines.append("")
            lines.extend(f"- `{value}`" for value in values)
            lines.append("")

    lines.extend(["## Safe environment variable names", ""])
    env_examples = data["safe_environment_examples"]
    assert isinstance(env_examples, dict)
    if not env_examples:
        lines.append("- No example environment files detected")
    else:
        for path, keys in env_examples.items():
            lines.append(f"### `{path}`")
            lines.append("")
            if keys:
                lines.extend(f"- `{key}`" for key in keys)
            else:
                lines.append("- No assignment keys detected")
            lines.append("")

    lines.extend(
        [
            "## Interpretation limits",
            "",
            "- This inventory proves only that paths or safe variable names were detected.",
            "- Read authoritative files before documenting behavior or intent.",
            "- Secret files and common generated or vendored directories were excluded.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect a safe path-level evidence inventory for documentation work."
    )
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--max-files", type=int, default=20000)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"error: project root is not a directory: {root}", file=sys.stderr)
        return 2
    if args.max_files < 1:
        print("error: --max-files must be at least 1", file=sys.stderr)
        return 2

    files, truncated = walk_files(root, args.max_files)
    data = detect(files, root)
    data["inventory"] = {
        "files_inspected_by_path": len(files),
        "truncated": truncated,
        "excluded_sensitive_values": True,
    }

    if args.format == "markdown":
        sys.stdout.write(as_markdown(data, len(files), truncated))
    else:
        json.dump(data, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
