#!/bin/bash

if [ -e "$1" ]; then
    file_content=$(cat < "$1" | sed 's/[^a-z]//g' | tr -d "\n")
    echo -n "$file_content" > "clean_$1"
else
    echo "file not found"
fi
