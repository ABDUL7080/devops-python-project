pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/ABDUL7080/devops-python-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-devops-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f python-app || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 8001:8000 --name python-app python-devops-app'
            }
        }

    }
}