node{
stage('Check out SCM')
{
checkout scm
}
  stage('install ruuvi sensor python package'){
    sh 'pip3 install ruuvitag_sensor'
  }
stage('build python file')
{
sh 'python3 ruuvi.py'
}
}
