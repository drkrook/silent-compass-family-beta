# LEDOVIA Stable rollback runbook — preparation only

**Status:** DRAFT / NO ROLLBACK AUTHORIZED. This document is not an executable deployment mechanism.

## Scope and limitations

This procedure concerns the static Stable website in `drkrook/silent-compass-family-beta`. The recovery artifact `ledovia-stable-source-recovery` is a snapshot of Git-tracked repository source, **not** a backup of the deployed GitHub Pages output, untracked assets, DNS, secrets, or Supabase database and authentication state. A successful archive extraction is not proof of a functioning production rollback.

The protected environment `ledovia-production` requires Captain's approval and restricts eligible branches to `release/stable-v1.0-candidate`. The production publishing job remains disabled. Do not bypass these safeguards.

## Before any rollback (mandatory)

1. **Stop and obtain explicit Captain authorization for the specific rollback.** Record incident, intended recovery commit, current production URL, and the approved target. Approval to prepare this runbook is **not** authorization to deploy.
2. Determine the **actual deployed** release and its source/build identity. Do not assume Stable `main` or the most recent snapshot equals the live site. Check GitHub Pages deployment history and, where possible, deployed asset hashes and service-worker cache version.
3. Confirm the target recovery archive is the correct prior **known-good, functionally tested** release. An archive generated from `main` alone is insufficient evidence.
4. Record current production state and preserve a separate recovery copy **before** changes. Confirm any required Supabase backup/restore strategy separately; never roll back shared authentication or user data as part of a static-site rollback without a separate reviewed plan.
5. Validate the target archive using the read-only `Verify Stable Recovery Restore (No Deploy)` workflow. Check snapshot run ID, expected full SHA, archive digest, extracted file set, PWA manifest, and service worker. Review compatibility with current Supabase configuration and data.
6. Review differences between the current deployed build and the target, including routes, caching, authentication configuration, and offline map assets. Document risks and rollback/forward recovery choices.

## Controlled restoration (NOT IMPLEMENTED)

7. Prepare a **new immutable release candidate** from the approved, verified recovery content. Do not rewrite production `main` or publish the snapshot directly. Record artifact digest and source commit.
8. Require Captain to test the candidate on a nonproduction URL, including offline use, map interaction, saved locations, authentication, and survival guides. Preserve existing functionality and data.
9. Require a **new explicit production approval** for that exact candidate and the protected `ledovia-production` environment. Only a separately implemented and reviewed release workflow may publish it. Never enable the disabled production job as part of an incident without separate authorization.
10. After an approved deployment, verify `app.getledovia.com` (once configured), HTTPS, service-worker update behavior, PWA install/launch, critical offline workflows, and auth. Monitor errors and document the outcome. If verification fails, stop and seek a new decision; do not automatically repeat deployment.

## Audit record template

- Incident and reason:
- Captain's explicit authorization and date:
- Previously deployed release/build and digest:
- Recovery snapshot run ID:
- Recovery source full commit SHA:
- Recovery archive SHA-256:
- Read-only restore verification run:
- Nonproduction test evidence:
- Production approval evidence:
- Deployment run and URL (if separately authorized):
- Post-deployment checks and outcome:

## Current verified baseline (historical)

- Recovery snapshot workflow #2 succeeded and produced `ledovia-stable-source-recovery`.
- Snapshot run ID: `43817358225`.
- Source commit: `f232749d4098a4e535d371c3d31956b45e0e2fb5`.
- Read-only restore verification workflow #4 succeeded.
- This baseline is a **source recovery snapshot**, not a certified production release.
- No production rollback or deployment is authorized by this runbook.
