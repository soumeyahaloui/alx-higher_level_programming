#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -sI "$1" | grep -i "HTTP/1.1 200 OK" && curl -s "$1"
