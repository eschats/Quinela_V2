pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh "chmod +x -R ${env.WORKSPACE}"
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh "chmod +x -R ${env.WORKSPACE}"
        sh 'python3 main.py'
      }
    }
  }
}