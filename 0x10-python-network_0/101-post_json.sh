#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response

# Check if the second argument (JSON file) exists
if [ ! -f "$2" ]; then
    echo "Usage: $0 <URL> <JSON file>"
    exit 1
fi

# Check if the JSON content in the file is valid
if ! jq empty < "$2" > /dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send the POST request and display the response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
