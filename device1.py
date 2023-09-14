import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor
from definitions import user, password, client_id, server, port

# Conexão Inicial
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

# Comportamento do Sistema
while True:
    client.publish('pucpr/iotmc/brunofranco/temperatura', temperatura())
    client.publish('pucpr/iotmc/brunofranco/umidade', umidade())
    time.sleep(5)

# client.disconnect()