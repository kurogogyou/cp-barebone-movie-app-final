
# Converted into unix newline endings by dos2unix linux command. 

# This script is used because normal users have no
# access to hosting on external ports on the VM. This way you can host a page in the (W)LAN.

# NOTE: find a way to ask for sudo inside the script.

# This is the project folder
cd /home/mario/devenvs/python/cp-barebone-movie-app-final/

# This adds the environment variables into the actual environment
# direnv allow .
for V in $(cat .env)
do    
	export $V 
done

# This is the default pipenv environment within the project:
# /home/mario/devenvs/python/cp-barebone-movie-app-final/
source .venv/bin/activate

# This command runs the locally hosted server
python3 manage.py runserver 0.0.0.0:80