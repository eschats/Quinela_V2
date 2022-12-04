pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/eschats/Quinela_V2.git']]])
            }
        }
      stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/eschats/Quinela_V2.git'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
          }
        stage('SonarQube analysis') {
          steps {
            script {
            // requires SonarQube Scanner 2.8+
                scannerHome = tool 'sonarqube01'
              }
             withSonarQubeEnv('sonarqube') {
             sh "${scannerHome}/bin/sonar-scanner \
               -Dsonar.projectKey=ProyectoQuinela01 \
               -Dsonar.sources=. \
               -Dsonar.host.url=http://172.17.0.3:9000 \
               -Dsonar.login=sqp_390b7af671e64d4d4b923a71cc78ff52366ad654"
        }
      }
    }









      }
    }



sqp_a4f651d102b9e94d17758b18b2885dbad104545c

sqp_390b7af671e64d4d4b923a71cc78ff52366ad654