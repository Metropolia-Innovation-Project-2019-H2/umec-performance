FROM python:latest

ADD ruuvi.py /

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
  sudo build-essential bluez bluez-tools bluez-hcidump \
  python3 python3-setuptools python3-dev python3-pip
  
RUN pip install ruuvitag_sensor

CMD [ "python3", "./ruuvi.py"]

EXPOSE 8000
