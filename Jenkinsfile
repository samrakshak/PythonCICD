pipeline {
  agent none 
  stages {
// nosetest for code coverage. This will generate the nosetests.xml file 
   stage('Test') {
     agent { 
         label 'devops_unittest'
     }
     steps {
       script {
      	scannerHome = '/home/jenkinsbot/sonar-scanner-2.9.0.670'
	sh "nosetests  --with-coverage --cover-xml --with-xunit tests/*"
	withSonarQubeEnv('Sonar(dk.147)') {
          sh "${scannerHome}/bin/sonar-scanner"
       }
      }
   }       
  }
}   
}
