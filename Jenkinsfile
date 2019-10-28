node{
stage('Check out SCM')
{
checkout scm
}
  stage('install ruuvi sensor python package'){
    sh 'pip install -r requirements.txt'
  }
stage('build python file')
{
sh 'python ruuvi.py'
}
}
