from ruuvitag_sensor.ruuvi import RuuviTagSensor
from influxdb import InfluxDBClient


def main(found_data):
    #print('MAC ' + found_data[0])
    #print(found_data[1])

    temp = found_data[1].get("temperature")
    humidity = found_data[1].get('humidity')

    datapoints =  [
    {
        "measurement": "ruuvi_metrics",
        "tags": {
            "host": "Obibini",
            "region": "Fi Vantaa"
        },

        "fields": {
            "temperature": temp 
            "humidity": humidity

        }
    }
	]

   
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'ofienipa')
    client.write_points(datapoints)

RuuviTagSensor.get_datas(main)