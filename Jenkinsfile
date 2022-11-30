pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh "chmod +x -R C//:ProgramData/Jenkins/.jenkins/workspace/ProyectoQuinela/ "
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh "chmod +x -R C://ProgramData/Jenkins/.jenkins//workspace//ProyectoQuinela/"
        sh 'python3 main.py'
      }
    }
  }
}