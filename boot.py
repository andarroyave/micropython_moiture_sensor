# import machine
# import network
# 
# if machine.reset_cause() != machine.SOFT_RESET:
#     wlan = network.WLAN(network.STA_IF)
#     ap = network.WLAN(network.AP_IF)
#     ap.active(False)
#     if not wlan.active():
#         wlan.active(True)
#     wlan.ifconfig(('192.168.0.18', '255.255.255.0', '192.168.0.1', '8.8.8.8'))    
#     if not wlan.isconnected():
#         print('connecting to network...')
#         wlan.connect('user', 'pass')
#         while not wlan.isconnected():
#             pass
# print('network config:', wlan.ifconfig())
#

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'user'
password = 'pass'
mqtt_server = '192.168.0.6'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
#topic_sub = b'casa/h1'
topic_pub = b'casa/h1'


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
