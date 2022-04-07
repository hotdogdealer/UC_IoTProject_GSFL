import random
import sys
from azure.iot.hub import IoTHubRegistryManager

MESSAGE_COUNT = 2
AVG_WIND_SPEED = 10.0
MSG_TXT = "{\"Test Nachricht\": %.2f}"

CONNECTION_STRING = "HostName=iot3bhwii22-fi.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=ek2o9UlnB5DI3+z4Gf74eFuyrC78KrRn5nph5GA6CwY="
DEVICE_ID = "Kaffeemaschine"

def Nachrichten_send():
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        for i in range(0, MESSAGE_COUNT):
            print ( 'Sending message: {0}'.format(i) )
            data = MSG_TXT % (AVG_WIND_SPEED + (random.random() * 4 + 2))

            props={}
            # optional: assign system properties
            props.update(messageId = "message_%d" % i)
            
            props.update(correlationId = "correlation_%d" % i)
            props.update(contentType = "application/json")

            # optional: assign application properties
            prop_text = "PropMsg_%d" % i
            props.update(testProperty = prop_text)

            registry_manager.send_c2d_message(DEVICE_ID, data, properties=props)

        try:
            # Try Python 2.xx first
            raw_input("Press Enter to continue...\n")
        except:
            pass
            # Use Python 3.xx in the case of exception
            input("Press Enter to continue...\n")

    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

if __name__ == '__main__':
    print ( "Starting the Python IoT Hub C2D Messaging service sample..." )

    
Nachrichten_send()

