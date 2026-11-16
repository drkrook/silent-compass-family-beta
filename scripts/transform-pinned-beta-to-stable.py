#!/usr/bin/env python3
"""Prepare a separate Stable candidate from a verified, extracted pinned Beta artifact.
Does not deploy, modify Supabase, or alter the input directory.
Usage: python3 scripts/transform-pinned-beta-to-stable.py INPUT_DIR OUTPUT_DIR
"""
import hashlib, json, pathlib, shutil, sys

source, target = map(pathlib.Path, sys.argv[1:])
if not source.is_dir() or target.exists():
    raise SystemExit("Input must exist and output must not exist")
html_path = source / "index.html"
manifest_path = source / "manifest.webmanifest"
html = html_path.read_text()
manifest = json.loads(manifest_path.read_text())

# Exact substitutions only: fail closed if the pinned package has changed.
replacements = [
    ("🧭 SILENT COMPASS <small>Beta Testing", "🧭 LEDOVIA <small>Stable Release"),
    ('aria-label="Silent Compass beta version"', 'aria-label="LEDOVIA stable version"'),
    ("Silent Compass cannot send an emergency alert.", "LEDOVIA cannot send an emergency alert."),
    ("Silent Compass cannot activate it.", "LEDOVIA cannot activate it."),
    ("You opened Silent Compass from a local file.", "You opened LEDOVIA from a local file."),
    ("Silent Compass BETA v", "LEDOVIA v"),
]
for before, after in replacements:
    if html.count(before) != 1:
        raise SystemExit(f"Expected exactly one occurrence of {before!r}, found {html.count(before)}")
    html = html.replace(before, after)
if "Silent Compass" in html or "SILENT COMPASS" in html:
    raise SystemExit("Unreviewed legacy branding remains")

# Authentication redirect is deliberately NOT modified here: production
# Supabase redirect allowlisting and behavior must be verified first.
if "silent-compass-testing/index.html" not in html:
    raise SystemExit("Expected Beta recovery redirect missing; manual review required")
if manifest.get("name") != "LEDOVIA - Beta" or manifest.get("short_name") != "LEDOVIA - Beta":
    raise SystemExit("Unexpected pinned manifest branding")
manifest["name"] = "LEDOVIA — Your Offline Survival Companion"
manifest["short_name"] = "LEDOVIA"

shutil.copytree(source, target)
(target / "index.html").write_text(html)
(target / "manifest.webmanifest").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
report = {
    "status": "STAGING ONLY — NOT RELEASE READY",
    "source": str(source),
    "output": str(target),
    "changed_files": {
        name: {"before": digest(source / name), "after": digest(target / name)}
        for name in ("index.html", "manifest.webmanifest")
    },
    "blockers": [
        "Password recovery redirect still targets Beta path",
        "Production Supabase redirect allowlist not verified",
        "Stable PWA and full functional retesting not completed",
        "Explicit Captain production approval required"
    ]
}
(target / "stable-transformation-report.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
