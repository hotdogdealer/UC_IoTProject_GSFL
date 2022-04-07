import random 
import sys
from azure.iot.hub import IoTHubRegistryManager 

raw_input = 0

MESSAGE_COUNT = 2
AVG_WIND_SPEED = 10.0 
MSG_TXT = "{\"Gratulation, sie haben einen kostenlosen Kaffee gewonnen!\": %.2f}"