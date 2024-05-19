# Use a Python base image
FROM python:3.10.10-alpine

# Installing the dependencies in the container
RUN pip install flask

# Set the working directory in the container
WORKDIR /app

# Copying the web server file to app folder
# in the container
COPY web_server.py /app/web_server.py

# Exposing the web server at port 5000
EXPOSE 5000

# Command to start the python webserver
CMD ["python", "web_server.py"]