#!/bin/bash

# Use the current user name as docker project name.
DOCKER_PROJECT=${USER}

NVIDIA_OPTION=$1
echo "$1: NVIDIA_OPTION=${NVIDIA_OPTION}"
echo "$0: USER=${DOCKER_PROJECT}"
DOCKER_CONTAINER="${DOCKER_PROJECT}_robo_manip_baseline"
echo "$0: DOCKER_CONTAINER=${DOCKER_CONTAINER}"

# Stop and remove the Docker container.
EXISTING_DOCKER_CONTAINER_ID=`docker ps -aq -f name=${DOCKER_CONTAINER}`
if [ ! -z "${EXISTING_DOCKER_CONTAINER_ID}" ]; then
  echo "Stop the container ${DOCKER_CONTAINER} with ID: ${EXISTING_DOCKER_CONTAINER_ID}."
  docker stop ${EXISTING_DOCKER_CONTAINER_ID}
  echo "Remove the container ${DOCKER_CONTAINER} with ID: ${EXISTING_DOCKER_CONTAINER_ID}."
  docker rm ${EXISTING_DOCKER_CONTAINER_ID}
fi

# Build docker image
docker compose -p ${DOCKER_PROJECT} -f docker/compose.yaml build

# Initialize environments in the container
echo "Finished building docker image."