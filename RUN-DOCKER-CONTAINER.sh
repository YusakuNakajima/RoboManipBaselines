#!/bin/bash


################################################################################
# arg1: project name

################################################################################

# Set the Docker container name from a project name (first argument).
# If no argument is given, use the current user name as the project name.
PROJECT=${USER}
CONTAINER="${PROJECT}-robo-manip-baseline-1"
echo "$0: PROJECT=${PROJECT}"
echo "$0: CONTAINER=${CONTAINER}"
echo $(dirname "$0")/docker/compose.yaml


# Run the Docker container in the background.
# Any changes made to './docker/compose.yaml' will recreate and overwrite the container.
docker compose -p ${PROJECT} -f $(dirname "$0")/docker/compose.yaml up -d


################################################################################

# Display GUI through X Server by granting full access to any external client.
xhost +local:

################################################################################

# Enter the Docker container with a Bash shell
docker exec -it  -w /home/user/RoboManipBaselines ${CONTAINER} bash -i