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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Run ETL') {
            steps {
                sh 'python app.py'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'output/*.csv'
            }
        }
    }
}
