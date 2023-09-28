#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code

response=$(curl -sI "$1")

if [[ $response == *"HTTP/1.1 200 OK"* ]]; then
    curl -s "$1"
fi
