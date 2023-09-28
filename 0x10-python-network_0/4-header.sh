#!/bin/bash
# This script sends a GET request to a URL with a custom header and displays the body of the response

url="$1"
header="X-School-User-Id: 98"

curl -s -H "$header" "$url"
