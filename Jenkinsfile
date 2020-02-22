#!/usr/local/bin/groovy
pipeline {
    agent { node { label 'master' } }

    environment {
        TEST_PREFIX = "test-IMAGE"
        
    }

    stages {

         stage("Getting Information Regarding Build") {
            steps {
                 echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                
                
            }
        }

        
          stage("Running Unittest") {
            steps {
                sh "/usr/local/bin/nosetests tests/test_helloworld.py"
                
                
            }
        }

        stage("Package Installation") {
            steps {
                sh "/usr/local/bin/pip install -r requirements.txt"
                
            }
          } 

        stage("Deploy") {
            steps {
                sh "cd helloworld"
                sh "/usr/local/bin/python  app.py"
                
            }
            post {
                always {
                    echo "always forever"
                  }
                success {
                    // we only worry about archiving the jar file if the build steps are successful
                    archiveArtifacts(artifacts: 'helloworld/*.py', allowEmptyArchive: true)
                }
              failure {
                  echo "failed"
               }
           }
        }

        stage("Production") {
        //when {
          //      environment TEST_PREFIX: "test-IMAGE"
                
           // }
            steps {
                echo "task fro production"
                
             }
           }
        
  
    }
}