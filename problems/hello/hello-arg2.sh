#!/bin/bash

set -u

#if no argument, then usage statement is printed
if [[ $# -lt 1 ]]; then
        printf "Usage: %s GREETING NAME\n" "$(basename "$0")"
        exit 1
fi

GREETING=$1
NAME=$2

echo "$GREETING, $NAME!"
