import paho.mqtt.client as mqtt
import time

print("This is a publisher client 2")
topic = input("Published topic: ")
payload = input("Published payload: ")
print(" ")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print(" ")


client = mqtt.Client()
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883, 60)

time.sleep(1)
while True:
    client.loop()
    client.publish(topic, payload)
    time.sleep(1)
