# test_web_server
Docker image creating flask web server and deploying it through jenkins.

- Jenkinsfile (groovy script) 
  - Sets the trigger to check for new changes in the git repo every 1 minute.
  - Checkout the git repo and the master branch.
  - Builds the docker image with the build version of the python web server.
  - Testing stage is mentioned but there are no actual tests to be performed for this application.
  - Deployment stage:
    - Stop the web-server already running in the background.
    - Removes the docker image for the existing web server.
    - Runs the newly built docker image of the web server with updated build number.
  - Lastly it checks whether the deployment was successful or not and indicates the results.

- web_server.py
  -Python code to host the flask web server on the local machine and port 5000.

- Dockerfile
  - Uses the python base image with the latest version for the docker container.
  - Installs the dependencies required in the container.
  - Sets the working directory in the container and copies the web server file in that directory of the container.
  - Exposes the web server at port 5000 of the local machine.
  - And hence runs the web server.
