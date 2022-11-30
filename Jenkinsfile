pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'sudo python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'sudo python3 main.py'
      }
    }
  }
}