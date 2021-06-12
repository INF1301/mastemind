__all__ = ['dificuldade', 'geraSenha', 'checaResposta']

import random
from view import draw 
from tkinter import messagebox
from controller import eventHandler

##cores:  vermelho = 1, verde = 2, azul = 3, amarelo = 4, rosa = 5, azul-ciano = 6, marrom = 7, roxo = 8

def defineDiff(n):
    global numPedras, numCores, limitJogadas

    if (n == 1):
        numPedras = 4
        numCores = 6
        limitJogadas = 8

    elif (n == 2):
        numPedras = 5
        numCores = 7
        limitJogadas = 10

    else:
        numPedras = 6
        numCores = 8
        limitJogadas = 12
       
    return numCores
    
def jogadasTab():
    tabSlots = []

    for tent in range(limitJogadas):
        preenche = []
        tabSlots.append(preenche)
        for _ in range (numPedras):
            tabSlots[tent].append(0)
    return tabSlots


def geraSenha():
    global senha
    senha = []
    for _ in range(numPedras):
        senha.append(random.randint(1, numCores))
    return senha


def checaResposta(tentativa):
    senha=eventHandler.getSenha()
    dicas = []
    listaAux = []
    for i in range(len(senha)):
        if senha[i] == tentativa[i]:
            if(tentativa[i] in listaAux and False in dicas):
                dicas.remove(False)
            dicas.append(True)
            listaAux.append(tentativa[i])
        elif tentativa[i] in senha and tentativa[i] not in listaAux:
            dicas.append(False)
            listaAux.append(tentativa[i])
            
    return dicas



   