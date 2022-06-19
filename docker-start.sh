#!/bin/sh
docker stop resume
echo "stopped container"
docker rm resume
echo "removed container"
docker build -t resume .
docker run -d --name=resume -p 9997:8080  resume