#!/usr/bin/env bash
# One-command backup of the Zotero data folder to GitHub.
#
# Usage:
#   ./zotero-backup.sh
#   ./zotero-backup.sh "optional custom commit message"
#
# Close Zotero before running so the database is not captured mid-write.
set -euo pipefail

cd "$(dirname "$0")"

git add .gitignore locate storage styles translators zotero.sqlite zotero.sqlite.bak

if git diff --cached --quiet; then
  echo "No changes to back up."
  exit 0
fi

msg="${1:-Zotero library backup $(date +%Y-%m-%d_%H-%M)}"
git commit -m "$msg"
git push origin research
echo "Backup pushed to origin/research."
