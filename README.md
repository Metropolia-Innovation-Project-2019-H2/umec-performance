# Nokia  uMec Project.

1. Introduction.

This project consists of four (4) teams working together to achieve a CI/CD environment for the Nokia uMec Servers.
The teams are; Hardware, Software, Api and Performance Monitoring teams. 
This part of the project describes the methods and tools used by the Performance Monitoring team to achieve the purposes of monitoring the servers.
The servers monitored included 2 raspberrypi 3s, and 3 Suse SLEs 15 servers. Docker containers were used in the entire project.

Performance monitoring and visualisation is an essential part of IT systems. A very good performance monitoring and visualisation gives insight into 
what is happening at any given time, under the hood. This information is useful to determine what actions to take and when to take them to avoid shutdowns,
damage to hardware, and also to detect malicious behaviour etc. 

The project is a complete containerized setup using docker. All the tools used are docker containers.

The performance team was task to use InfluxDB and Grafana for this project.
InfluxDB
link: https://www.influxdata.com

Grafana
link: https://grafana.com 

Telegraf
link:


2. TIG Stack

Through research, the team found out about the Telegraf, InfluxDB and Grafana (TIG) stack. 
Telegraf is used to collect system metrics. Telegraf metrics are then sent to influxdb. The grafana server is configured to display these values.
 

3. Implementation

- On raspberrypi r1, username is perfteam.
- On raspberrpi r2,s1,s2 and s3  username is performance

Setting up docker environment on r1 and r2

- ssh to pi

- using curl: curl -sSL https://get.docker.com | sh 

- it is important to add the docker group and add user to the group to avoid typing sudo each time. This will prove helpful because there will be a lot of docker commands that require sudo.

- to do this; sudo groupadd docker

- sudo usermod -aG docker $user in this case user is perfteam on r1 or performance on r2.

- refer to this page to learn more about post docker installation https://docs.docker.com/install/linux/linux-postinstall/

 

This project makes use of the ruuvisensor library from pypi, so it has to be installed first.

The link to ruuvitag python = https://pypi.org/project/ruuvitag_sensor/

Take note using ruuvitag python library requires Bluez, as is clearly stated in the documentation.

this is achieved by: sudo apt-get install bluez bluez-hcidump.

All of these have been taken care of with the jenkinsfile for CI/CD purposes. 

What will be added includes telegraf, influxdb and grafana. The task will be to get telegraf running with customised config, influxdb being the target of telegraf and grafana plotting the contents of databases on influxdb.


