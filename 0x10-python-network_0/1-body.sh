#!/bin/bash
# a script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response.

response=$(curl -s -w "\nSTATUS_CODE:%{http_code}" "$1")
status_=$(echo "$response"| grep "STATUS_CODE"|cut -d":" -f2)

if [[ "$status_" -eq "200" ]]
then
  echo "$response"|grep -v "STATUS_CODE"
fi
