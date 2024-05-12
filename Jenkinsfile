pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: "master",
                url: 'https://github.com/Rishh-k/test_web_server.git'
            }
        }

        stage('Build') {
            steps {
                echo "This is the build stage"
            }
        }

        stage('Test') {
            steps {
                echo "This is the test stage"
            }
        }

        stage('Deploy') {
            steps {
                sh 'python web_server.py &'
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
