pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat cmd_exec('python --version')
      }
    }
    stage('hello') {
      steps {
        bat 'python3 main.py'
      }
    }
  }
}