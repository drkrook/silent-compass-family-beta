# LEDOVIA Beta-to-Stable controlled release — implementation plan

**Status: design only. No production publishing is enabled or authorized.**

## Required release sequence

1. Beta independent packaging produces `ledovia-beta-candidate` and `ledovia-package-inventory` tied to an exact successful GitHub Actions run and full commit SHA. Current packaging runs on `release/independent-build-prep`, **not necessarily the public Beta site**.
2. Captain tests the **exact candidate** on a nonproduction URL, including offline/PWA update, maps, pinch zoom, saved locations, survival guides, and authentication. A green packaging job alone does not constitute functional approval.
3. Stable's existing read-only inspection, preflight, and rehearsal jobs verify the exact Beta run, SHA, file inventory, and staged output. They must remain no-deploy.
4. A future release workflow must accept the exact source run ID, 40-character SHA, and an explicit approval confirmation. It must re-fetch the exact artifacts, validate run provenance, verify every file digest, and reject expired or unexpected artifacts. Never rebuild from a moving branch.
5. Before any production publishing job, require `environment: ledovia-production` and Captain's GitHub required-reviewer approval. The protected environment currently targets `release/stable-v1.0-candidate`; do not bypass it.
6. Create an immutable release record (artifact digest, source SHA, approval, target URL, workflow run), preserve a known-good recovery reference, then publish only after separately authorized implementation of the production job.
7. Verify live file hashes, HTTPS, service worker/PWA update, offline functionality, and Supabase compatibility after release. Halt and seek approval if checks fail. Never automatically roll back shared user data.

## Critical blockers before implementing publishing

- **No production deployment authorization** has been granted.
- Current packaging success does not establish that the artifact is identical to the public Beta build Captain tested.
- Public Stable is still the existing Silent Compass-labelled build; branding and base-path compatibility must be checked in the candidate before promotion.
- GitHub Pages deployment mode, protected environment behavior, and exact release artifact retention must be validated without changing the live site.
- The source snapshot and protected recovery branch are not substitutes for an independently verified, full deployed-build backup.

## Protected boundaries

No writes to Stable `main`, no GitHub Pages deployment, no Supabase modifications, no DNS changes, no deletion or force push of recovery refs. Implementation requires a new explicit scoped authorization, one change at a time, followed by verification and a stop.
