pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Run ETL') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'output/*.csv'
            }
        }
    }
}
