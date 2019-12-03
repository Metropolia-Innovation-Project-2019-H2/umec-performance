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
link:

Grafana
link:


2. TIG Stack

Through research, the team found out about the Telegraf, InfluxDB and Grafana (TIG) stack. 
performance monitoring with grafana, influx and telegraf

Important:

This project makes use of the ruuvisensor library from pypi, so it has to be installed first.

The link to ruuvitag python = https://pypi.org/project/ruuvitag_sensor/

Take note using ruuvitag python library requires Bluez, as is clearly stated in the documentation.

this is achieved by: sudo apt-get install bluez bluez-hcidump.

All of these have been taken care of with the jenkinsfile for CI/CD purposes. 

What will be added includes telegraf, influxdb and grafana. The task will be to get telegraf running with customised config, influxdb being the target of telegraf and grafana plotting the contents of databases on influxdb.


