import time
from azure.iot.device import IoTHubDeviceClient

RECEIVED_MESSAGES = 0

CONNECTION_STRING = "HostName=iot3bhwii22-fi.azure-devices.net;DeviceId=Kaffeemaschine;SharedAccessKey=H4q5C+TfTjyUPLiRe8RmbN5UVOjP7zg9gQYFL9Xkyys="

def Nachrichten_empfang(message):
    global RECEIVED_MESSAGES
    RECEIVED_MESSAGES += 1
    print("")
    print("Messagve received:")

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        print ("    {}".format(property))

    print("Total calls received: {}".format(RECEIVED_MESSAGES))

def main():
    print ("Starting the Python IoT Hub C2D Messaging device sample...")

    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print ("Waiting for C2D messages, press Ctrl-C to exit")
    try:
        # Attach the handler to the client
        client.on_message_received = Nachrichten_empfang

        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()
main()