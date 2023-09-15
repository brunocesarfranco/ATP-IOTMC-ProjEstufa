import random
from time import time
from tkinter import W

#Camada de Abstração de Hardware 

def aquecedor (estado: str):
    if estado == 'on':
        print ('Aquecedor LIGADO')
    else:
        print('Aquecedor DESLIGADO')


def rele(estado: str):
    if estado == 'on':
        print('Rele ligado!')
    else:
        print('Rele desligado!')
    aquecedor(estado)
    print('========================================')


def temperaturaEstufa1 ():
    return random.randrange (0,40)    


def temperaturaEstufa2():
    return random.randrange (0,40)