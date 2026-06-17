pipeline {
    agent any

    stages {

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