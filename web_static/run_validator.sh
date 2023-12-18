#!/bin/bash

# Specify the absolute path to your project directory
PROJECT_DIR="/root/AirBnB_clone/web_static"

# Find all HTML and CSS files in the project directory
FILES=$(find "$PROJECT_DIR" -type f \( -name "*.html" -o -name "*.css" \))

# Path to the W3C validator script
W3C_VALIDATOR_SCRIPT="./W3C-Validator/w3c_validator.py"

# Loop through each file and run the W3C validator
for FILE in $FILES; do
    echo "Running W3C Validator for file: $FILE"
    "$W3C_VALIDATOR_SCRIPT" "$FILE"
done
