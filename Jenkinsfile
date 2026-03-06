pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/ABDUL7080/devops-python-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                sh 'python app.py'
            }
        }

    }
}