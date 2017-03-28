import sys
import ssl
import paho.mqtt.client as mqtt
import json
import time
from time import gmtime, strftime
from read_sensor import *


aws = "a32e3zdwtbeerq.iot.us-west-2.amazonaws.com"


# called while client tries to establish connection with the server
def on_connect(mqtt_client, obj, flags, rc):
    if rc == 0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
    elif rc == 1:
        print ("Subscriber Connection status code: " + str(rc) + " | Connection status: Connection refused")


# called when a topic is successfully subscribed to
def on_subscribe(mqtt_client, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos)+"data"+str(obj))


# called when a message is received by a topic
def on_message(mqtt_clinet, obj, msg):
    print("Received message from topic: "+msg.topic+" | Qos: "+str(msg.qos)+" | Data Received: "+str(msg.payload))


# creating a client with client-id=myEdison
mqtt_client = mqtt.Client(client_id="myEdison")

mqtt_client.on_connect = on_connect
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_message = on_message


# Configure https
mqtt_client.tls_set("/home/root/aws_certs/rootCA.crt",
                    certfile="/home/root/aws_certs/certificate.pem.crt",
                    keyfile="/home/root/aws_certs/private.pem.key",
                    tls_version=ssl.PROTOCOL_TLSv1_2,
                    ciphers=None)
# connecting to aws-account-specific-iot-endpoint
mqtt_client.connect(aws, port=8883)

time.sleep(5)

# the topic to publish to
mqtt_client.subscribe("$aws/things/myEdison/shadow/get", qos=1)
mqtt_client.subscribe("sensor/data", qos=1)

thing = "myEdison"
SerialNumber = 'intel_edison_01'

mqtt_client.loop_start()

while 1:
    time.sleep(10)
    moisture = get_moisture()
    temperature, humidity = get_temp_hum()
    light = get_light()
    payload = json.dumps({
        "state": {
            "reported": {
                "this_thing_is_alive": True
            }
        }})

    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    sensor_data = json.dumps({
        "TimeStamp": timestamp,
        "temperature": temperature,
        "moisture": moisture,
        "humidity": humidity,
        "light": light
    })
    mqtt_client.publish("$aws/things/myEdison/shadow/update", payload)
    mqtt_client.publish("sensor/data", sensor_data, 1)