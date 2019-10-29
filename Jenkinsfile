node{
stage('Check out SCM')
{
checkout scm
}
  stage('install bluez'){
    sh label: '', script: 'ssh pi \' sudo apt-get install bluez bluez-hcidump -y \''
   // sudo apt-get install bluez bluez-hcidump
  }
  stage('install ruuvi sensor python package'){
   // sh label: '', script: 'ssh pi \' PATH=${PATH}:/usr/local/bin \''
    sh label: '', script: 'ssh pi \' pip3 install ruuvitag_sensor \''
  }
stage('build python file')
{
sh label: '', script: 'ssh pi \' python3 uMec/umec-performance/ruuvi.py \''
}
  /* stage('JUnit publish')
  {
    junit 'reports/*.xml'
  } */
}
