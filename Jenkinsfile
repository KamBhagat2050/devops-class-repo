pipeline {
    agent any

    environment {
        REGISTRY = "ghcr.io"
        IMAGE = "kambhagat2050/calculator-app"   // <-- your calculator app image
        TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'calculator-repo',
                    url: 'https://github.com/KamBhagat2050/devops-class-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${REGISTRY}/${IMAGE}:${TAG}")
                }
            }
        }

        stage('Push to GHCR') {
            steps {
                script {
                    docker.withRegistry("https://${REGISTRY}", "140634400") {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            when {
                expression { fileExists('k8s-deployment.yaml') }
            }
            steps {
                sh """
                kubectl set image deployment/calculator-app calculator-app=${REGISTRY}/${IMAGE}:${TAG} --namespace default
                """
            }
        }
    }
}
