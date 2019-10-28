node{
stage('Check out SCM')
{
checkout scm
}
  stage('install ruuvi sensor python package'){
    git 'https://github.com/ttu/ruuvitag-sensor'
    sh 'pip install --user'
  }
stage('build python file')
{
sh 'python ruuvi.py'
}
}
