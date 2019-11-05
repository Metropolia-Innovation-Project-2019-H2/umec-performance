node{
stage('Check out SCM')
{
checkout scm
}
  stage('install bluez'){
    //sh label: '', script: 'r1 \' sudo apt-get install bluez bluez-hcidump -y \''
    sh label: '', script: 'r1 sudo apt-get install bluez bluez-hcidump'
   // sudo apt-get install bluez bluez-hcidump
  }
  stage('install ruuvi sensor python package'){
   // sh label: '', script: 'ssh pi \' PATH=${PATH}:/usr/local/bin \''
    sh label: '', script: 'r1 \' pip3 install ruuvitag_sensor \''
  }
stage('build python file')
{
sh label: '', script: 'r1 \' python3 home/citeam/umec-performance/ruuvi.py \''
}
  /* stage('JUnit publish')
  {
    junit 'reports/*.xml'
  } */
}
