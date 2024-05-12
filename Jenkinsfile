// Defining the pipeline
pipeline {

    // Agent selection
    agent any
    // Initiating the trigger to check for SCM every minute
    triggers { 
        pollSCM('* * * * *') 
    }

    // Initializing the pipeling stages 
    stages {
        // Checkout stage
        // Checkout to the git repo and master branch 
        stage('Checkout') {
            steps {
                git branch: "master",
                url: 'https://github.com/Rishh-k/test_web_server.git'
            }
        }

        // Build stage
        // Builds the docker image of the web server and update the version number
        stage('Build') {
            steps {
                script {
                    // Defines the tag for build number
                    tag = "sample_web_server:${env.BUILD_NUMBER}"
                    // Build Docker image
                    bat "docker build -t $tag ."
                }
            }
        }

        // Test stage
        // Test stage, but no test require for this application
        stage('Test') {
            steps {
                echo "This is the test stage"
            }
        }

        // Deployment stage
        // Deploys the docker image for python web server with updated build version
        // and exposes it at port 5000 for localhost
        stage('Deploy') {
            steps {
                script {
                    // Use the tag variable defined earlier
                    bat "docker stop sample_web_server || exit 0"
                    bat "docker rm -f sample_web_server || exit 0"
                    bat "docker run -d --name sample_web_server -p 5000:5000 $tag"
                }
            }
        }
    }

    // Checks the final output of the pipeline stages after deployment and 
    // indicates the final result
    post {
        success {
            echo 'Flask application deployed successfully!'
        }
        failure {
            echo 'Failed to deploy Flask application!'
        }
    }
}

