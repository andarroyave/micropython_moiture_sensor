try:
  import usocket as socket
except:
  import socket
from machine import Pin, ADC
import time
import json

# def toggle_led(led):
#     pin_status = False
#     if led.value():
#         pin_status = True
#         led_state = "OFF"        
#     led.value(not pin_status)

adc = ADC(0)
device_name = 'casa_h1'
#"41.12,-71.34"
coordinates = "40.32988667,-74.34678694"

def publish(server, client, topic, message):
    c = MQTTClient(client, server)
    c.connect()
    c.publish(topic, message)
    c.disconnect()

def getMoisture():
    moisture = adc.read()
    moisture_percent = 100 - int(moisture*100/1023)
    message = '{{"device_name": "{0}", "moisture_percent": "{1}", "coordinates": "{2}"}}'.format(device_name, moisture_percent, coordinates)
    #message = str(moisture_percent)
    print(message)
    return message
    


while True:
    message = getMoisture()
    publish(mqtt_server, client_id, topic_pub, message)
    print('message {0} published!'.format(message))
    time.sleep(10)
 