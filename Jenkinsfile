pipeline {
    agent any

    environment {
        IMAGE_NAME = "hymavathigonti/ai-job-hunter:v2"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credential',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }
        
        stage('Deploy to EC2') {
    steps {
        sshagent(['ec2-ssh-key']) {
            sh '''
            ssh -o StrictHostKeyChecking=no ec2-user@13.233.227.211 "
                sudo docker pull hymavathigonti/ai-job-hunter:v2 &&
                sudo docker stop ai-job-hunter || true &&
                sudo docker rm ai-job-hunter || true &&
                sudo docker run -d \
                --restart unless-stopped \
                --name ai-job-hunter \
                -p 5000:5000 \
                hymavathigonti/ai-job-hunter:v2
            "
            '''
     }
    }
        }
    }
}