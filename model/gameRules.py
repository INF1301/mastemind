__all__ = ['dificuldade', 'geraSenha', 'checaResposta']

from random import randint

##cores:  vermelho = 1, verde = 2, azul = 3, amarelo = 4, rosa = 5, azul-ciano = 6, marrom = 7, roxo = 8

def defineDiff(n):
    global numPedras, numCores, limitJogadas, tentativa 
    tentativa = []

    if (n == 1):
        numPedras = 4
        numCores = 6
        limitJogadas = 8
        print("a")
    elif (n == 2):
        numPedras = 5
        numCores = 7
        limitJogadas = 10
        print("b")
    else:
        numPedras = 6
        numCores = 8
        limitJogadas = 12
        print("c")
    


def geraSenha():
    global senha
    senha = []
    for _ in numPedras:
        senha.append(random.randint(1, numCores))


def checaResposta():
    global dicas

    dicas = []
    listaAux = []

    for i in senha:
        if senha[i] == tentativa[i]:
            if(tentativa[i] in listaAux):
                dicas.remove(False)
            dicas.append(True)
            listaAux.append(tentativa[i])
        elif tentativa[i] in senha and tentativa[i] not in listaAux:
            dicas.append(False)
            listaAux.append(tentativa[i])


