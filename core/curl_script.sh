#!/bin/bash
let name
name="signin.html"
while IFS= read -r line; do
    if [[ $line == *"https://"* ]]
    then
        curl $line -o $name
    else 
        name=$(echo -e "$line" | tr -d '[:space:]')
        name="$line.mp4"
    fi
done < "$1"
