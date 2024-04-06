#!/bin/bash

# tmux session name
SESSION_NAME="google-map-scrapper"

# Log file name
LOG_FILE="debug-terminal.log"

# Path to the Python script - update this to the correct path if necessary
SCRIPT_PATH="/home/ubuntu/google-map-scrapper/start.py"

# Function to get the PID of the running Python script
get_pid() {
    echo $(ps aux | grep -v "grep" | grep "${SCRIPT_PATH}" | awk '{print $2}')
}

# Attach to the tmux session
tmux attach-session -t $SESSION_NAME

# Get the PID of the running start.py script
PID=$(get_pid)

# If the script is running, kill it
if [ ! -z "$PID" ]; then
    echo "Stopping current script with PID: $PID"
    kill -9 "$PID"
fi

# Pull the latest code updates (skip this if not needed)
# cd /path/to/your/script/directory
# git pull origin main

# Restart the script and redirect output to log file
echo "Starting the script..."
tmux new-session -d -s $SESSION_NAME "python3 $SCRIPT_PATH > $LOG_FILE 2>&1"

# Detach from the tmux session (optional since we're using -d to start in detached mode)
# tmux detach -s $SESSION_NAME

echo "Restarted the script in tmux session: $SESSION_NAME and logging to $LOG_FILE"

# Exit the script
exit 0
