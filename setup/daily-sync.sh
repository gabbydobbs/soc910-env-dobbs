#!/bin/bash
# Daily automated sync of the SOC 910 coursework folder to GitHub.
# Run unattended via launchd (~/Library/LaunchAgents/com.gabrielledobbs.soc910-daily-sync.plist)
# at midnight every day. Logs to ~/.claude/scripts/daily-sync.log.
#
# Scope is intentionally narrow: only ~/Desktop/SOC 910. It never touches
# ~/Desktop/Files/Fall 2025/Thesis or Apple Notes — those are outside this
# script's working directory entirely, not just gitignored.

set -euo pipefail

TARGET_DIR="/Users/gabrielledobbs/Desktop/SOC 910"
LOG_FILE="/Users/gabrielledobbs/.claude/scripts/daily-sync.log"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

cd "$TARGET_DIR" || { log "ERROR: could not cd into $TARGET_DIR"; exit 1; }

if [[ -z "$(git status --porcelain)" ]]; then
  log "No changes — nothing to sync."
  exit 0
fi

git add -A
git commit -m "Automated daily sync: $(date '+%Y-%m-%d')" >> "$LOG_FILE" 2>&1

if git push >> "$LOG_FILE" 2>&1; then
  log "Pushed successfully."
else
  log "ERROR: push failed — check network/auth and retry manually with 'git push' in $TARGET_DIR."
  exit 1
fi
