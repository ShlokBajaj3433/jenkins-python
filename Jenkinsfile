pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Python App') {
            steps {
                sh 'python3 app.py'
            }
        }

    }
}
