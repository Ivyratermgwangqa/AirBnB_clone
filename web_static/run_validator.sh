#!/bin/bash

AIRBNB_REPO_PATH="/root/AirBnB_clone/web_static"  # Update this path to the correct one
W3C_VALIDATOR_SCRIPT="./W3C-Validator/w3c_validator.py"

FILES=$(find "$AIRBNB_REPO_PATH" -type f \( -name "*.html" -o -name "*.css" \))

for FILE in $FILES; do
    echo "Running W3C Validator for file: $FILE"
    python3 "$W3C_VALIDATOR_SCRIPT" "$FILE"
done
