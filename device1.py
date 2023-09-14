import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor
from definitions import user, password, client_id, server, port

def mensagem(client, user, msg):
    if msg.topic == 'pucpr/iotmc/brunofranco/aquecedor':
        aquecedor(msg.payload.decode())

# Conexão Inicial
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

# Assinatura do tópico
client.on_message = mensagem
client.subscribe('pucpr/iotmc/brunofranco/#')
client.loop_start()

# Comportamento do Sistema
while True:
    client.publish('pucpr/iotmc/brunofranco/temperatura', temperatura())
    client.publish('pucpr/iotmc/brunofranco/umidade', umidade())
    time.sleep(5)

# client.disconnect()