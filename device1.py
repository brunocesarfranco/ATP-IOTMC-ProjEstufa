import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor

user = ''
password = ''
client_id = 'clientId-pdNgIL1L80'
server = 'mqtt-dashboard.com'
port = 1883

client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

while True:
    client.publish('pucpr/iotmc/brunofranco/temperatura', temperatura())
    client.publish('pucpr/iotmc/brunofranco/umidade', umidade())
    time.sleep(5)

# client.disconnect()