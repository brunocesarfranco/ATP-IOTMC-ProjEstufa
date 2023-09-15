import random
from time import time

# Camada de Abstração de Hardware


def aquecedor(estado: str):
    if estado == 'on':
        print('Aquecedor LIGADO..')
        print('')
    else:
        print('Aquecedor DESLIGADO..')
        print('')


def temperaturaEstufa1():
    return random.randrange(15, 45)


def temperaturaEstufa2():
    return random.randrange(15, 45)


def aumentarTemp(temp):
    temp += 1
    return temp


def diminuirTemp(temp):
    temp -= 1
    return temp


def quebraLinha():
    print('')
    print('====================================================')