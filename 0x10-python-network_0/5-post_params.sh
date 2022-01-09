#!/bin/bash
# a script that sends a POST request to a given URL.

curl -s -X POST -d "email=test@gmail.comsubject=I will always be here for PLD" "$1"
