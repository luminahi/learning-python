#!/bin/bash

if [ -e "$1" ]; then
    file_content=$(cat < "$1")

    for ((i=0; i<24; i++)); do
        lsinsulin+=${file_content:i:1}
    done

    for ((i=24; i<54; i++)); do
        binsulin+=${file_content:i:1}
    done

    for ((i=54; i<89; i++)); do
        cinsulin+=${file_content:i:1}
    done

    for ((i=89; i<110; i++)); do
        ainsulin+=${file_content:i:1}
    done

    echo -n "$lsinsulin" > lsinsulin-seq-clean.txt
    echo -n "$binsulin" > binsulin-seq-clean.txt
    echo -n "$cinsulin" > cinsulin-seq-clean.txt
    echo -n "$ainsulin" > ainsulin-seq-clean.txt
fi