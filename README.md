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

 
Setting up docker environment on s1,s2 and s3

Details on docker installation here https://docs.docker.com/install/linux/docker-ee/suse/#install-from-a-package

- ssh to server

- sudo zypper refresh //updates the zypper package index

- zypper install docker //installs docker

- sudo groupadd docker //add docker group

- sudo usermod -aG docker $User //add user to docker group


uMec SERVER 1 (S1)

Server 1 at ip ***.***.***.**0 is the main server used in this project. 

Issuing docker ps command shows the containers running on this server. The server hosts five (5) containers. These are influxdb, grafana, telegraf, prometheus, prometheus node exporter.


INFLUXDB:

For more detailed instructions on working with docker influxdb refer to; https://hub.docker.com/_/influxdb/

- To begin pull the docker image

docker pull influxdb

- Create a default influxdb config file (This command will create a config file in the current working directory, not a container.

docker run --rm influxdb influxd config > influxdb.conf

- To verify the location of the config file, use

sudo readlink -f influxdb.conf 

-The location of the influxdb.conf printed above will be used to create the influxdb container. This allows for future editing of the influxdb. The configuration file can be edited,

and then the container restarted. Doing so allows the container to pick up the changes implemented in the configuration file. It is recommended to implement all the containers in this manner.

 All subsequent containers were implemented this way.

- Create influxdb container by modifying the $PWD to /home/performance/influxdb.conf or the path to the default configuration generated previously. 

docker run -p 8086:8086 -p 50000:50000 \
      -v $PWD/influxdb.conf:/etc/influxdb/influxdb.conf:ro \
      influxdb -config /etc/influxdb/influxdb.conf

- Verify the container was created.

docker ps

- In this project, influxdb was used with default settings. Default settings was enough to achieve the target in the time frame we had. 

- Security and other settings can be added in the future by editing the /home/performance/influxdb.conf file and restarting the container.

This influxdb container was used as the default database. All other servers reported their metrics by targetting the ip of Server1:50000 as will be shown in the telegraf config file of other servers.

- To query the influxdb for databases

docker exec -it influxdb influx 

SHOW DATABASES //displays the databases present on the influxdb server. The output is

Connected to http://localhost:8086 version 1.7.8
InfluxDB shell version: 1.7.8

- > SHOW DATABASES

- name: databases
- name

- _internal
- telegraf	 
- rpi_telegraf	//Raspberry pi 1 database	  	
- s1telegraf	//Server 1 database
- s2telegraf	//Server 2 database
- s3telegraf	//Server 3 database
- rpi2_telegraf	//Raspberry pi 2 database


GRAFANA

Grafana server was used for the purposes of visualisation of data from the influxdb database. 

For detailed instructions on working with grafana https://grafana.com/docs/installation/docker/

The default grafana image:latest was used for this project. No serious modifications have been made as at the time of this document. There is username and password security in place. 

Should you need the login details, please contact albert.offei@metropolia.fi. 

- To install grafana:

docker run -d -p 3000:3000--name=grafana -v grafana-storage:/var/lib/grafana grafana/grafana

- After installation, ssh tunnel using command:

ssh -L 3000:localhost:3000 user@ip

- Login using username and password.

- Set up data source by selecting influxdb as database. Edit source to point to docker network address of influxdb (172.17.0.*). Give the name of the database e.g. rpi_telegraf and test.

- After successful connection. Grafana is ready to graphically display the metrics recorded in the database.

- Grafana comes with add ons including ready made dashboards that can be imported instead of building dashboards from scratch. 



TELEGRAF


Telegraf is the agent for collecting metrics from linux systems. These metrics are then outputed to influxdb. The telegraf.conf file is used to configure the behaviour of telegraf.

- Telegraf has several inputs that can be used to grab specific metrics. In this project, the inputs used on all servers were [[inputs.temp]] to monitor the temperature of the cpu cores
and [[inputs.net]] to monitor network stats.

- Telegraf can output metrics to a lot of different servers and services. In this project, telegraf outputs metrics via http to influxdb on Server1. 

- On Server1, telegraf.conf is configured to target influxdb directly at 172.17.0.4:8086. All other servers report metrics to the same influxdb but target it at http://Server1ip:50000


The project is still ongoing and changes are being made constantly. This readme will be updated to reflect the status of the project including any add ons and additionaly services deployed.

Example config files will be added to the github organisation. 

For more details do not hesitate to contact: albert.offei@metropolia.fi and marko.uusitalo@metropolia.fi

Current additions:

Prometheus monitoring: Implemented. Working. Details will be available shortly. 

Prometheus alertmanager: Installed. Under configurations and soon will be sending email alerts. Initial targets will be alerts on unsual network activity and alerts if a server were to go down.

Promeeteus node-explorer: Implemented, currently being visualized by grafana. Still being configured.
