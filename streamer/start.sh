#!/usr/bin/env bash

printf "Searching for a camera player service ... "
if ! PLAYER_ADDRESS=$(python3 discover.py); then
    printf "not found\n"    
    exit $?
else
    printf "found\n"
fi

printf "Camera player address is %s\n" ${PLAYER_ADDRESS}
printf "Streaming ...\n"
raspivid -t 0 -w 800 -h 480 -fps 10 -o udp://${PLAYER_ADDRESS}
