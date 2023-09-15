import paho.mqtt.client as mqtt
import time
from hal import temperaturaEstufa1, aquecedor, aumentarTemp, diminuirTemp, quebraLinha
from definitions import user, password, client_id, server, port, tempIdeal


def mensagem(client, userdata, msg):
    # cria um vetor com o parâmetro que é recebido do cayenne. O split serve para dividir o vetor em duas informações separadas por vírgula.
    vetor = msg.payload.decode().split(',')
    print(f'Temperatura atual da Estufa 1: {temp} graus Celsius.')
    # se o vetor for 1 ele liga se não ele desliga
    aquecedor('on' if vetor[1] == '1' and temp < tempIdeal else 'off')
    # confirma que o comando foi processado para o cayenne e para o botão
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor [0]}')
    # print (vetor)


# Conexão inicial para o device1 (Estufa1)
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

# Publish
# método que sera evocado quando receber uma mensagem do servidor
client.on_message = mensagem
# tópico que queremos do servidor
client.subscribe(f'v1/{user}/things/{client_id}/cmd/1')
client.loop_start()  # serve para ficar monitorando o servidor


# Comportamento do sistema
while True:
    temp = temperaturaEstufa1()
    quebraLinha()
    print(f'Temperatura inicial da Estufa 1: {temp} graus Celsius.')
    client.publish('v1/'+user+'/things/'+client_id+'/data/0',
                   'temp,c=' + str(temp))  # mandando a mensagem de temperatura

    # Valida se temperatura precisa ser aumentada
    if temp < tempIdeal:
        while temp <= tempIdeal:
            temp = aumentarTemp(temp)
            if temp == tempIdeal:
                print(f'Temperatura da Estufa 1 está ideal.')
                break

            print(f'Temperatura atual da Estufa 1: {temp} graus Celsius.')
            client.publish(
                f'v1/{user}/things/{client_id}/data/0', 'temp,c=' + str(temp))
            aquecedor('on')
            time.sleep(3)

    # Valida se temperatura precisa ser diminuida
    if temp > tempIdeal:
        while temp >= tempIdeal:
            temp = diminuirTemp(temp)
            if temp == tempIdeal:
                print(f'Temperatura da Estufa 1 está ideal.')
                break

            print(f'Temperatura atual da Estufa 1: {temp} graus Celsius.')
            client.publish(
                f'v1/{user}/things/{client_id}/data/0', 'temp,c=' + str(temp))
            aquecedor('off')
            time.sleep(3)

    time.sleep(3)

# client.disconnect()
