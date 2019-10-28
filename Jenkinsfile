node{
stage('Check out SCM')
{
checkout scm
}
  stage('install ruuvi sensor python package'){
    sh 'pip install ruuvitag_sensor'
  }
stage('build python file')
{
sh 'python ruuvi.py'
}
}
