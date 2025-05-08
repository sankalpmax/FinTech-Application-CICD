pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/sankalpmax/FinTech-Application-CICD.git'
            		}
        	}
	stage('Docker Build'){
		steps{
			sh 'docker build -t my-fintech-application:02 .'
			}
		}
	stage('Docker Run'){
		steps{
			sh 'docker run -d -p 5000:5000 --name MyFintech-co my-fintech-application:02'
				}
			}

	stage('Docker Push Image'){
		steps{
			script{
				docker.withRegistry('https://index.docker.io/v1/', 'dockerhub'){
				sh 'docker tag my-fintech-application:02  sankalparava/my-fintech-application:02'
				sh 'docker push sankalparava/my-fintech-application:02'
					}
				}
			}
		}
	}
} 
