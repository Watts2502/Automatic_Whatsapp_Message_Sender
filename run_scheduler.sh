#!/bin/bash

# Path to Python virtual env and script
source <Insert path to your virtual environment>/bin/activate
PY_SCRIPT="<Insert path to your Python script>"

# Log file to track execution
LOG_FILE="<Insert path to your log file>"

# Get current time in 24h format
CURRENT_TIME=$(date +%H:%M)
TODAY=$(date +%Y-%m-%d)

# Check if already run today
if grep -q "$TODAY" "$LOG_FILE" 2>/dev/null; then
  echo "Already run today."
  exit 0
fi

# Check time range between 20:00 and 22:30 (Change as per your requirement)
if [[ "$CURRENT_TIME" > "20:00" && "$CURRENT_TIME" < "22:30" ]]; then
  echo "Running WhatsApp script at $CURRENT_TIME"
  python3 "$PY_SCRIPT"

  # Log the date
  echo "$TODAY" >> "$LOG_FILE"
else
  echo "Current time $CURRENT_TIME is outside allowed window."
fi
