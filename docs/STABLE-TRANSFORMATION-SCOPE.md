# LEDOVIA Stable transformation — approved planning scope

**Planning document only. No code transformation, production deployment, or Supabase modification is authorized by this document.**

## Pinned source
- Repository: `drkrook/silent-compass-testing`
- Packaging run: `43811995143`
- Full commit: `39213ae9165f28f015b4f70e975ad9ed515b5228`
- Candidate: `ledovia-beta-candidate`; checksum inventory: `ledovia-package-inventory`
- Public Beta comparison: 154/154 public assets matched; zero-byte `.nojekyll` verified in inventory.
- Captain reported passing all seven functional acceptance checks.

## Exact findings from downloaded branding-reference-contexts.json
Six occurrences in packaged `index.html`:
1. Offset 32665: header `SILENT COMPASS` with `Beta Testing` subtitle.
2. Offset 32897: `aria-label="Silent Compass beta version"`.
3. Offset 106962: emergency warning `Silent Compass cannot send an emergency alert.`
4. Offset 119927: satellite SOS warning `Silent Compass cannot activate it.`
5. Offset 213876: local-file help `You opened Silent Compass from a local file.`
6. Offset 215578: update notice `Silent Compass BETA v` + remote version.

One hard-coded Beta repository path at offset 99219 in password recovery:
`location.origin+'/silent-compass-testing/index.html'`.

Manifest is Beta-branded (`LEDOVIA - Beta`); icon references include Beta-named assets. Audit source ZIP contains only extracted evidence, not the full candidate.

## Permitted changes in a **new, isolated, reproducible Stable candidate** (not the accepted Beta source)
- Replace six **exact user-facing** legacy-name occurrences with LEDOVIA, preserving emergency/satellite safety warnings verbatim except the product name.
- Replace customer-facing `Beta Testing`, version accessibility text, update notice, and manifest `name`/`short_name` with approved Stable wording.
- Replace the hard-coded Beta password recovery path **only after** verifying correct production origin/redirect allowlist and behavior; prefer a deployment-base-aware URL rather than an unverified literal.
- Preserve original icon assets until their content and cache references are reviewed. Renaming an icon file is **not** automatically required merely because its filename contains `beta`.

## Protected behavior
Do not change mapping, GPS, pinch zoom, offline resources, service worker caching logic, saved locations, survival guides, emergency advice, accounts, Supabase project settings, domains, or existing public Beta/Stable sites as part of this planning step.

## Validation gates before any promotion
1. Build transformation from the exact pinned artifact; verify original SHA-256 inventory before editing and record all changed files and before/after hashes.
2. Validate HTML, manifest JSON, referenced assets, relative base paths, and PWA scope/start URL for the Stable project path.
3. Test password recovery redirect on an isolated nonproduction origin and verify Supabase allowlisting without changing settings.
4. Test install/update/offline cache migration and all seven acceptance functions against the **transformed Stable candidate**, not just original Beta.
5. Confirm recovery snapshot and protected `ledovia-production` environment approval are still effective.
6. Require fresh explicit Captain approval for production deployment. No deployment is permitted based solely on this plan.

## Immediate next decision
Inspect the exact pinned package's manifest, icon references and password recovery implementation in full, and inspect the current Supabase redirect configuration read-only. Do not implement the transformation until that review is complete.
