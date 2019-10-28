node{
stage('Check out SCM')
{
checkout scm
}
  stage('install ruuvi sensor python package'){
    sh label: '', script: 'ssh pi \' PATH=${PATH}:/usr/local/bin \''
    sh label: '', script: 'ssh pi \' pip3 install -r requirements.txt \''
  }
stage('build python file')
{
sh label: '', script: 'ssh pi \ 'python3 ruuvi.py \''
}
}
