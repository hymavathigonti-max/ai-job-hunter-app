pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/hymavathigonti-max/ai-job-hunter-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-job-hunter:v2 .'
            }
        }

        stage('List Images') {
            steps {
                sh 'docker images'
            }
        }
    }
}
