"""constants for somneosensor"""
import voluptuous as vol
from datetime import timedelta

from homeassistant.helpers import config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (TEMP_CELSIUS, UNIT_PERCENTAGE)
#DOMAIN = 'somneo'
VERSION = "1.3"

DEFAULT_NAME = "somneosensor"
DEFAULT_HOST = "192.168.2.131"
DEFAULT_PORT = 443
DEFAULT_SENS = ["temperature", "humidity"]

CONF_NAME = "name"
CONF_HOST = "host"
CONF_PORT = "port"
CONF_SENS = "sensors"
MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=60)

SENSOR_TYPES = {
    "temperature": ["somneo_temperature", TEMP_CELSIUS],
    "humidity": ["somneo_humidity", UNIT_PERCENTAGE],
    "light": ["somneo_light", "lux"],
    "noise": ["somneo_noise", "db"],
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_SENS, default=list(SENSOR_TYPES)): [
            vol.In(SENSOR_TYPES)
        ],
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_HOST, default=DEFAULT_HOST): cv.string,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
    }
)

NOTIFICATION_ID = 'somneosensor_notification'
NOTIFICATION_TITLE = 'SomneoSensor Setup'

#SCAN_INTERVAL = timedelta(seconds=60)
#ATTR_S_TEMP = 'temperature'
#ATTR_S_HUM = 'humidity'
#ATTR_S_LIGHT = 'light'
#ATTR_S_NOISE = 'noise'
