#!/bin/bash

# Prompt the user for the path
echo "Please enter the path to the directory you want to lint (default is current directory):"
read TARGET_PATH

# If no path is provided, default to the current directory
if [ -z "$TARGET_PATH" ]; then
    TARGET_PATH="."
fi

# Run pylint with the specified path
pylint --ignore=migrations --ignore-patterns='migrations/.*\.py' --disable=too-many-ancestors "$TARGET_PATH"
