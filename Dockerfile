FROM python:lastest

ADD ruuvi.ry /

RUN pip install ruuvitag_sensor

CMD [ "python", "./ruuvi.ry"]

