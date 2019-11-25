/* node{
stage('Check out SCM')
{
checkout scm
}

  stage('install bluez'){
    //sh label: '', script: 'r1 \' sudo apt-get install bluez bluez-hcidump -y \''
     sh label: '', script: 'ssh -tt perfteam@194.110.231.139'''
    //sh label: '', script: 'ssh citeam@194.110.231.139'
    //sh label: '', script: 'ssh citeam@194.110.231.139 \' sudo apt-get install bluez bluez-hcidump -y \''
    sudo apt-get install bluez bluez-hcidump -y
  }
  stage('install ruuvi sensor python package'){
   // sh label: '', script: 'ssh pi \' PATH=${PATH}:/usr/local/bin \''
    sh label: '', script: 'ssh citeam@194.110.231.139 \' pip3 install ruuvitag_sensor \''
  }
stage('build python file')
{sh label: '', script: 'ssh citeam@194.110.231.139 \'python3 home/citeam/umec-performance/ruuvi.py \''
}
 
} */

pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh '--junit-xml test-reports.results.xml python test.py'
      }   
    post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}
