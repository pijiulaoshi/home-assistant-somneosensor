"""Platform for sensor integration."""
from datetime import timedelta
import logging
import urllib3
import requests
urllib3.disable_warnings()

import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle

from .const import *

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Somneo sensor platform."""
    host = config.get(CONF_HOST)
    port = config.get(CONF_PORT)
    data = SomneoData(host, port)
    dev = []
    for sensor in config[CONF_SENS]:
        dev.append(SomneoSensor(data, sensor))

    add_entities(dev, True)

class SomneoSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, data, sensor_types):
        """Initialize the sensor."""
        self.data = data
        self._name = SENSOR_TYPES[sensor_types][0]
        self._unit_of_measurement = SENSOR_TYPES[sensor_types][1]
        self.type = sensor_types
        self._state = None
    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name
    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state
    @property
    def unit_of_measurement(self):
        """Return the unit the value is expressed in."""
        return self._unit_of_measurement
    def update(self):
        """Get the latest data and updates the states."""
        self.data.update()
        if self.type == "temperature":
            self._state = self.data.temperature
        if self.type == "humidity":
            self._state = self.data.humidity
        if self.type == "light":
            self._state = self.data.light
        if self.type == "noise":
            self._state = self.data.noise


class SomneoData:
    """Get the latest data and update."""

    def __init__(self, host, port):
        """Initialize the data object."""
        self.temperature = None
        self.humidity = None
        self.light = None
        self.noise = None
        self.host = host
        self.port = port

    def get_sensor_data(self):
        host2 = self.host
        port2 = self.port
        url = 'https://' + host2 + ':' + str(port2) + '/di/v1/products/1/wusrd'
        sensor_data_update = {'mslux': None, 'mstmp': None, 'msrhu': None, 'mssnd': None, 'avlux': None, 'avtmp': None, 'avhum': None, 'avsnd': None, 'enscr': None}
        r = requests.get(url, verify=False, timeout=30, stream=True)
        if r.status_code == 200:
            r_data = r.json()
            for key, value in r_data.items():
                sensor_data_update[key] = value
        return sensor_data_update


    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Get the latest data from Somneo."""
        sensor_data = self.get_sensor_data()
        self.temperature = sensor_data['mstmp']
        self.humidity = sensor_data['msrhu']
        self.light = sensor_data['mslux']
        self.noise = sensor_data['mssnd']




