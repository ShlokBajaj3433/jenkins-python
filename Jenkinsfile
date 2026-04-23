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

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Web Smoke Test') {
            steps {
                sh '''
                    PORT=5000 python3 app.py > python-server.log 2>&1 &
                    PY_PID=$!
                    trap "kill $PY_PID" EXIT
                    sleep 3
                    curl -f http://localhost:5000/health
                '''
            }
        }

    }
}
