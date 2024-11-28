#!/bin/bash

# Load environment variables from .env file
source ../.env
# Start the Django server on the local network with specific IP address 
# and port number for expo react native connection on a macOS device

# 1. start the expo server to get the server ip address
#    eg: exp://192.168.15.38:8081
# 2. modify the .env, to take the expo IP address, port 8000
# 3. modify the frontend DEV_SERVER_BASE_URL
#    eg: DEV_SERVER_BASE_URL=http://192.168.15.38:8000/
#    eg: DEV_SERVER_MEDIA_URL=http://192.168.15.38:8000/media/
# 4. start the Django server with the expo IP address and port number
#    eg: python3 manage.py runserver 192.168.15.38:8000
#    =========>> IMPORTANT <<=========
# 5. restart the expo server without cache  
#    eg: npx expo start -c
#    =========>> IMPORTANT <<=========

echo "Starting Django server at $FRONTEND_IP:8000..."
python3 manage.py runserver "$FRONTEND_IP:8000"