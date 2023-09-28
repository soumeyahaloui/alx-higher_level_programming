#!/bin/bash
# This script sends a POST request to a URL with specific parameters and displays the body of the response

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST "$url" -d "email=$email" -d "subject=$subject"
