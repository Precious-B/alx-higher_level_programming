#!/bin/bash
# a script that Sends a DELETE request to a given URL and
# displays the response body.

curl -sX DELETE "$1"
