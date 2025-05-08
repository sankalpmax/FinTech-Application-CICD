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
	stage('Dockr Run'){
		steps{
			sh 'docker run -d -p 3000:3000 --name MyFintech-co my-fintech-application:02'
				}
			}
		}
	} 
