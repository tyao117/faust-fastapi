#!/bin/bash
docker container stop $(docker container ls -a -q -f "label=io.confluent.docker")
docker system prune -a -f --volumes
