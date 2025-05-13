#!/bin/bash

if ! command -v docker &> /dev/null; then
    echo "You should install Docker: https://docs.docker.com/get-started/get-docker"
    exit 1
fi

SCRIPT_DIR=`dirname $(realpath -m "$0")`
CONTAINER_NAME="vasiniyo-hagman"
echo "Building $CONTAINER_NAME..."     && docker build -t "$CONTAINER_NAME" "$SCRIPT_DIR" &>/dev/null
echo "Stopping old $CONTAINER_NAME..." && docker stop "$CONTAINER_NAME" 2>/dev/null
echo "Removing old $CONTAINER_NAME..." && docker rm "$CONTAINER_NAME" 2>/dev/null
docker run -it\
           --rm \
           --name "$CONTAINER_NAME"\
           "$CONTAINER_NAME:latest"
