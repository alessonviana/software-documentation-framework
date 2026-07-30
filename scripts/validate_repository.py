#!/usr/bin/env python3
"""Validate framework structure, Markdown links, and public-repository safety."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_PATHS = (
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/ARCHITECTURE.md",
    "docs/METHODOLOGY.md",
    "docs/PUBLIC-REPOSITORY-SAFETY.md",
    "docs/USAGE.md",
    "docs/VALIDATION.md",
    "docs/pt-BR/GUIA-DE-USO.md",
    ".agents/skills/document-software-project/SKILL.md",
    ".agents/skills/document-software-project/agents/openai.yaml",
    ".agents/skills/document-software-project/references/documentation-standard.md",
    ".agents/skills/document-software-project/references/document-templates.md",
    ".agents/skills/document-software-project/references/spec-driven-development.md",
    ".agents/skills/document-software-project/scripts/collect_project_evidence.py",
)

PROHIBITED_PUBLIC_SUFFIXES = {
    ".doc",
    ".docx",
    ".epub",
    ".gz",
    ".mobi",
    ".pdf",
    ".ppt",
    ".pptx",
    ".tar",
    ".xls",
    ".xlsx",
    ".zip",
}

SENSITIVE_FILENAMES = {
    ".env",
    ".env.local",
    ".env.production",
    ".npmrc",
    ".pypirc",
    "credentials",
    "credentials.json",
    "id_ed25519",
    "id_rsa",
    "secrets.yaml",
    "secrets.yml",
}

TEXT_SUFFIXES = {
    "",
    ".json",
    ".md",
    ".py",
    ".rst",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)


def iter_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(root).parts
    )


def check_required(root: Path) -> list[str]:
    return [
        f"missing required path: {relative}"
        for relative in REQUIRED_PATHS
        if not (root / relative).is_file()
    ]


def check_skill_frontmatter(root: Path) -> list[str]:
    skill_path = root / ".agents/skills/document-software-project/SKILL.md"
    if not skill_path.is_file():
        return []
    text = skill_path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return ["SKILL.md must start with YAML frontmatter"]

    keys: list[str] = []
    values: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return [f"invalid SKILL.md frontmatter line: {line}"]
        key, value = line.split(":", 1)
        keys.append(key.strip())
        values[key.strip()] = value.strip()

    errors: list[str] = []
    if set(keys) != {"name", "description"}:
        errors.append("SKILL.md frontmatter must contain only name and description")
    if values.get("name") != "document-software-project":
        errors.append("SKILL.md name must be document-software-project")
    if not values.get("description"):
        errors.append("SKILL.md description must not be empty")
    return errors


def check_markdown_links(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        relative = path.relative_to(root)
        if path.suffix.lower() not in {".md", ".mdx"}:
            continue
        if relative.parts[:4] == (
            ".agents",
            "skills",
            "document-software-project",
            "assets",
        ):
            continue

        text = CODE_FENCE_RE.sub("", path.read_text(encoding="utf-8"))
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if (
                not target
                or target.startswith(("#", "mailto:"))
                or "://" in target
            ):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"{relative}: link escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"{relative}: broken local link: {raw_target}")
    return errors


def check_public_files(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        relative = path.relative_to(root)
        lowered_name = path.name.lower()
        if "__pycache__" in relative.parts or path.suffix.lower() == ".pyc":
            errors.append(f"generated Python artifact is not allowed: {relative}")
        if lowered_name in SENSITIVE_FILENAMES:
            errors.append(f"sensitive filename is not allowed: {relative}")
        if path.suffix.lower() in PROHIBITED_PUBLIC_SUFFIXES:
            errors.append(f"prohibited public file type: {relative}")
    return errors


def check_text_content(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    prohibited_fragments = {
        "/workspace/" + "scratch/": "local scratch path",
        "/root/" + ".codex/": "internal Codex path",
        "file_" + "000000": "internal attachment identifier",
        "libfile" + "_": "internal Library identifier",
        "BEGIN " + "PRIVATE KEY": "private key material",
    }
    prohibited_dashes = {
        chr(0x2011): "non-breaking hyphen",
        chr(0x2014): "em dash",
    }

    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(root)
        for fragment, label in prohibited_fragments.items():
            if fragment in text:
                errors.append(f"{relative}: contains {label}")
        for character, label in prohibited_dashes.items():
            if character in text:
                errors.append(f"{relative}: contains prohibited {label}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"error: repository root is not a directory: {root}", file=sys.stderr)
        return 2

    files = iter_files(root)
    errors = [
        *check_required(root),
        *check_skill_frontmatter(root),
        *check_markdown_links(root, files),
        *check_public_files(root, files),
        *check_text_content(root, files),
    ]

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository validation passed ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
