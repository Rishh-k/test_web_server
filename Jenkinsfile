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
                script{
                    def tag = "my_web_server:${env.BUILD_NUMBER}"
                    docker build -t $tag .
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
                script{
                    docker stop my_web_server
                    docker rm -f my_web_server
                    docker run -d --name my_web_server -p 5000:5000 $tag
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
