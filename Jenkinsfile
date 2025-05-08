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
	}
}
