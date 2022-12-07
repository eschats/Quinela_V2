pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                slackSend channel: 'upana2022', message: 'Inicio de prueba, validación del repositorio'
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/eschats/Quinela_V2.git']]])
                slackSend channel: 'upana2022', message: 'Fin de prueba, validación del repositorio'
            }
        }
      stage('Build') {
            steps {
                slackSend channel: 'upana2022', message: 'Inicio de prueba, Creación del repositorio'
                git branch: 'main', url: 'https://github.com/eschats/Quinela_V2.git'
                slackSend channel: 'upana2022', message: 'Fin de prueba, Creación del repositorio'
            }
        }
        stage('Test') {
            steps {
                slackSend channel: 'upana2022', message: 'Inicio de prueba, Pruebas unitarias y de stress del repositorio'
                sh 'python3 -m pytest --seconds 45'
                slackSend channel: 'upana2022', message: 'Fin de prueba, Pruebas unitarias y de stress del repositorio'
            }
          }
        stage('SonarQube analysis') {
          steps {
            slackSend channel: 'upana2022', message: 'Inicio de prueba, Pruebas de Código SonarQuebe'
            script {
            // requires SonarQube Scanner 2.8+
                scannerHome = tool 'sonarqube'
              }
             withSonarQubeEnv('sonarqube') {
             sh "${scannerHome}/bin/sonar-scanner \
               -Dsonar.projectKey=ProyectoQuinela01 \
               -Dsonar.sources=. \
               -Dsonar.host.url=http://172.17.0.3:9000 \
               -Dsonar.login=sqp_390b7af671e64d4d4b923a71cc78ff52366ad654"
            slackSend channel: 'upana2022', message: 'Fin de prueba, Pruebas de Código SonarQuebe'
        }
      }
    }

     stage('Mensaje Final') {
            steps {
                slackSend channel: 'upana2022', message: 'Pruebas Finalizadas'
            }
     }





      }
    }
