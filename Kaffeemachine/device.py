from azure.iot.device import IoTHubDeviceClient
from random import randint

def main ():
    connection_string = "HostName=iot3bhwii22-fi.azure-devices.net;DeviceId=Kaffeemaschine;SharedAccessKey=H4q5C+TfTjyUPLiRe8RmbN5UVOjP7zg9gQYFL9Xkyys="
    client = IoTHubDeviceClient.create_from_connection_string(connection_string)
    client.connect()
    client.send_message("test")

    client.disconnect()
    client.shutdown()
    print("successfully sent")
main()