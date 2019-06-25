import os
import sys
import time
import socket
from zeroconf import ServiceBrowser, Zeroconf

# Must match service type from the camera-player
SERVICE_TYPE = os.getenv("SERVICE_TYPE", "_cameraplayer._udp")

address = None

# Sets global address when the service is found


class MyListener:
    def remove_service(self, zeroconf, type, name):
        pass

    def add_service(self, zeroconf, type, name):
        global address
        info = zeroconf.get_service_info(type, name)
        address = "{}:{}".format(socket.inet_ntoa(info.address), info.port)


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "{}.local.".format(SERVICE_TYPE), listener)

# Loop for 30s and wait for the service, if not found, exit
try:
    start = time.time()
    while time.time() - start < 30:
        if address is not None:
            break
        time.sleep(1)
finally:
    zeroconf.close()

if address is not None:
    print(address)
else:
    sys.exit(-1)
