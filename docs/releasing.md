# Releasing a new version

Countertop uses version numbers like `v0.3.1`. A **fix** release bumps the last number (0.3.1 to 0.3.2), and a **feature** release bumps the middle one (0.3.1 to 0.4.0).

## While you work

Every pull request that changes something people will notice adds a one-line note file under [changes/](../changes/README.md): `changes/new/`, `changes/changed/` or `changes/fixed/`, written for the people who use Countertop. Separate files never conflict, so several pull requests can be open at once. Those notes become the release notes.

## Publish

1. On GitHub, open **Actions → Release → Run workflow**.
2. Leave the branch on `main`, and type `fix`, `feature`, or an exact version such as `1.0.0`.
3. Press **Run workflow**.

The workflow:

- sets `VERSION` in `tools/countertop.py` gathers the notes in `changes/` into a new section of the changelog, removes the note files, then commits that to `main`,
- publishes the GitHub release with those notes,
- builds and tests the Docker image and pushes `ghcr.io/kizit/countertop:vX.Y.Z` and `:latest`,
- builds and tests the Mac app for Apple Silicon and Intel, and attaches both zips to the release.

It takes about 15 minutes. It stops before changing anything if there are no notes in `changes/`.

Unraid's **Check for Updates** and `docker compose pull` pick up `:latest`. Within 12 hours, every install's Controls shows the update notice with a link to the release notes, and the Mac app shows **Install Countertop vX.Y.Z** in its menu.

## By hand

The same steps from a clone, with the GitHub CLI:

```sh
git switch main && git pull
python3 .github/prepare-release.py fix      # or feature, or 1.0.0; prints the new tag
git commit -am "Release vX.Y.Z" && git push
gh release create vX.Y.Z --target main --title "Countertop vX.Y.Z" \
  --notes "$(python3 .github/release-notes.py vX.Y.Z)"
```

A release created this way starts the Docker and Mac app builds by itself.
