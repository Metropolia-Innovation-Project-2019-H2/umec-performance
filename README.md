# umec-performance
performance with grafana, influx and telegraf

Important:

This project makes use of the ruuvisensor library from pypi, so it has to be installed first.

The link to ruuvitag python = https://pypi.org/project/ruuvitag_sensor/

Take note using ruuvitag python library requires Bluez, as is clearly stated in the documentation.

this is achieved by: sudo apt-get install bluez bluez-hcidump.

All of these have been taken care of with the jenkinsfile for CI/CD purposes. 

What will be added includes telegraf, influxdb and grafana. The task will be to get telegraf running with customised config, influxdb being the target of telegraf and grafana plotting the contents of databases on influxdb.


