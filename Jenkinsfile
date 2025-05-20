pipeline {
    agent any

    environment {
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/sankalpmax/FinTech-Application-CICD.git'
            }
        }

        stage('Docker Build Image') {
            steps {
                sh 'docker build -t sankalparava/phonepay:03 .'
            }
        }

        stage('Docker Run Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 --name digital-bank sankalparava/phonepay:03
                '''
            }
        }

        stage('Docker Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
                        sh 'docker push sankalparava/phonepay:03'
                    }
                }
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                sh '''
                kubectl apply -f phonepay-app-deployment.yaml
     		kubectl apply -f phonepay-app-service.yaml           
                '''
            }
        }
    }
}
