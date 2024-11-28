# Django - Expo macOS Setup

This guide will help you start the Django server on the local network with a specific IP
address and port number to enable Expo React Native connection on a macOS device.

## Steps

### 1. Start the Expo server to get the server IP address

Run the following command to start the Expo server:

```sh
npx expo start
```

Take note of the server IP address provided by Expo. For example, if the server address is:

```sh
exp://192.168.15.38:8081
```

The IP address to use is 192.168.15.38.

### 2. Configure the Django .env File

Update the .env file to set the IP address and port for the Django server.
Combine the IP address from the Expo output with port 8000.

example .env:

```sh
FRONTEND_IP=192.168.15.38:8000
```

### 3. Start the Django server with the Expo IP address and port number

Run the following command to start the Django server:

```sh
./scripts/start.sh
```

## FOR FRONTEND

### 1. Modify the frontend environment variables (for later)

Set the backend server URL in your frontend environment configuration:

```sh
DEV_SERVER_BASE_URL=http://192.168.15.38:8000/
DEV_SERVER_MEDIA_URL=http://192.168.15.38:8000/media/
```

### 2. Restart the Expo server without cache

Clear the cache and restart the Expo server using:

```sh
npx expo start -c
```

By following these steps, your Expo app should be able to connect to your Django backend
running on your local network, on a macOS device.

---

## This project uses DRF Spectacular to generate API documentation.

https://drf-spectacular.readthedocs.io/en/latest/readme.html
https://github.com/tfranzel/drf-spectacular?tab=readme-ov-file

Available documentation interfaces:

### Swagger UI

**URL:** `[domain]/api/schema/swagger-ui/`

#### Features:

- **Interactive Documentation**: Test API endpoints directly from the documentation.
- **User-Friendly Interface**: Expandable sections for each endpoint.
- **Automatic Request Generation**: Input parameters and body data to generate and send requests.
- **Ideal For**:
  - Development and testing
  - Interactive learning
  - Debugging

### ReDoc

**URL:** `[domain]/api/schema/redoc/`

#### Features:

- **Static Documentation**: Read-only, well-structured, and responsive interface.
- **Advanced Documentation**: Nested objects, detailed schema descriptions, markdown support.
- **Responsive Design**: Clean and easy to navigate.
- **Ideal For**:
  - Read-only documentation
  - Detailed exploration
  - Client and stakeholder presentation

### Updating API Documentation

To update the OpenAPI schema (`schema.yml`), run the following command:

```sh
python manage.py spectacular --color --file docs/api/schema.yml
```

Ensure this command is run whenever significant changes are made to the API endpoints to keep the documentation up-to-date.

# create / load data

## create fixtures

Example:

```sh
python manage.py dumpdata user.CustomUser --indent 4 > ./fixtures/users.json
```

## load user fixtures

```sh
python manage.py loaddata fixtures/*
```
