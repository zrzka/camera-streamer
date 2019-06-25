#!/usr/bin/env bash

echo "Searching for a camera player service ..."
if ! PLAYER_ADDRESS=$(python3 discover.py); then
    echo "Not found ..."
    exit $?
fi

echo "Camera player available at ${PLAYER_ADDRESS} ..."
echo "Streaming ..."
raspivid -t 0 -w 800 -h 480 -fps 10 -o udp://${PLAYER_ADDRESS}
