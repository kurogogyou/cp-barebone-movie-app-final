#!/bin/bash

# Converted into unix newline endings by dos2unix linux command. This script is used because normal users have no
# access to hosting on external ports on the VM. This way you can host a page in the (W)LAN.

# This is the default pipenv environment within the project:
source /home/mario/devenvs/python/cp-barebone-movie-app-final/bin/activate
# This is the project folder
cd /home/mario/devenvs/python/cp-barebone-movie-app-final/
# This command runs the locally hosted server
python3 manage.py runserver 0.0.0.0:80