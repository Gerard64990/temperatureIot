#!/usr/bin/env python3

import sys
from w1thermsensor import W1ThermSensor
import paho.mqtt.publish as publish

sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "021791772c0a")
temperature = sensor.get_temperature()

s_temperature = str("%.1f" %  float(temperature))
publish.single("Temperature/parentsRoom", temperature, 0, False, "192.168.1.33");