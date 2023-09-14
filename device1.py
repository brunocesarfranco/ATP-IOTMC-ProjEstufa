import paho.mqtt.client as mqtt
import time

user = ''
password = ''
client_id = 'clientId-9SSQNUHx0i'
server = 'mqtt-dashboard.com'
port = 1883

client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.publish('pucpr/iotmc/brunofranco/temperatura', 23.3)
time.sleep(1)

# client.disconnect()