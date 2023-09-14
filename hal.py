#HAL (Hardware Abstraction Layer/Camada de Abstração de Hardware)

import random

def temperatura():
    return random.randrange(2, 40)

def umidade():
    return random.randrange(10, 95)

def aquecedor(estado: str):
    if estado == 'on':
        print('Aquecedor ligado.')
    
    else:
        print('Aquecedor desligado.')
