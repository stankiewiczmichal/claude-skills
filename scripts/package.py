#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Zip each skill into dist/<skill>.zip for upload to claude.ai (Settings > Capabilities > Skills)."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

shutil.rmtree(DIST, ignore_errors=True)
DIST.mkdir()
for skill_md in sorted(ROOT.glob("plugins/*/skills/*/SKILL.md")):
    skill_dir = skill_md.parent
    archive = shutil.make_archive(str(DIST / skill_dir.name), "zip", skill_dir.parent, skill_dir.name)
    print(Path(archive).relative_to(ROOT))
