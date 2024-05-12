pipeline {
    agent any
    triggers { 
        pollSCM('* * * * *') 
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "master",
                url: 'https://github.com/Rishh-k/test_web_server.git'
            }
        }

        stage('Build') {
            steps {
                // Define tag outside the script block
                script {
                    tag = "sample_web_server:${env.BUILD_NUMBER}"
                    // Build Docker image
                    bat "docker build -t $tag ."
                }
            }
        }

        stage('Test') {
            steps {
                echo "This is the test stage"
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Use the tag variable defined earlier
                    bat "docker stop sample_web_server || true"
                    bat "docker rm -f sample_web_server || true"
                    bat "docker run -d --name sample_web_server -p 5000:5000 $tag"
                }
            }
        }
    }

    post {
        success {
            echo 'Flask application deployed successfully!'
        }
        failure {
            echo 'Failed to deploy Flask application!'
        }
    }
}

