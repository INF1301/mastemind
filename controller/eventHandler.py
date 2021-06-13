from model import gameRules
from view import draw
import tkinter as tk
from string import *
from tkinter import messagebox 


def comecaJogo(esc):    
    global numTentativaAtual, numCores, corSelecionada, tentativaAtual, senha, tabuleiro

    cnv = draw.criaTopCnv("c")
    top = draw.criaTopCnv("t")

    numCores = gameRules.defineDificuldade(esc)

    tentativaAtual = [0 for x in range(0, numCores - 2)]

    if(checkState() != "Salvo"):
        senha = gameRules.geraSenha()
        tabuleiro = gameRules.tabuleiroVazio()
        numTentativaAtual = 0

    draw.limpaMenu()
    draw.desenhaPalheta(numCores)
    draw.desenhaTabuleiro(tabuleiro)
   
    
    
def controleBotoesJogo(existe, tent):
    global botaoProsseguir, botaoSalvarJogo, senha, tabuleiro, numTentativaAtual

    cnv = draw.criaTopCnv("c")

    if (existe == False):
        botaoProsseguir = tk.Button(cnv, text='Prosseguir', font='Arial 10 bold', height=4, width=15, border=5, command=atualizaProgresso,state="disabled")
        botaoProsseguir.place(x=785, y=450)
        botaoSalvarJogo = tk.Button(cnv, text='Salvar Partida', font='Arial 10 bold', height = 4, width = 15, border=5, command=lambda: salvaJogo())
        botaoSalvarJogo.place(x=785, y=350)

    elif (existe == True):
        if(0 not in tent):
            botaoProsseguir.configure(state= "normal") 
            


def checkState():
    global state
    return state

def changeState(string):
    global state
    state=string

def salvaTentativaAtual():
    global tabuleiro, numTentativaAtual, tentativaAtual

    tabuleiro[numTentativaAtual] = tentativaAtual.copy()

def getSenha():
    global senha
    return senha

def atualizaProgresso():
    global numTentativaAtual, botaoProsseguir, botaoSalvarJogo, tentativaAtual
    cnv = draw.criaTopCnv("c")
    dicas = []
    dicas = gameRules.checaResposta(tentativaAtual)
    draw.desenhaPinos(dicas,numTentativaAtual)
    botaoProsseguir.configure(state="disabled")

    if (False not in dicas and len(dicas) == 4):
        botaoSalvarJogo.configure(state="disabled") 
        popup_window("vitoria")
        changeState("Fim")
        return

    salvaTentativaAtual()

    numTentativaAtual += 1
    
    if (numTentativaAtual == (numCores-2) * 2):
        botaoSalvarJogo.configure(state = "disabled") 
        popup_window("derrota")
        changeState("Fim")
        return

    tentativaAtual = [0 for x in tentativaAtual]
 

def popup_window(estado):
    global senha

    window = tk.Toplevel()
     
    draw.desenhaSenha(senha,window)
    if (estado == "vitoria"):
        msg = "Parabéns, você ganhou!"
    elif (estado == "derrota"):
        msg = "Parabéns, você perdeu!"
    

    label = tk.Label(window, text=msg, font='Calibre 10 bold')

    label.pack(fill='none', padx=50, pady=50,side="top")

    button_close = tk.Button(window, text="Encerrar jogo", command=quit)

    button_novoJogo = tk.Button(window, text="Jogar novamente", command= lambda:[voltaMenu(), window.destroy()])
    button_close.pack(fill='x')
    button_novoJogo.pack(fill='x')

def voltaMenu():
    global state,tabuleiro

    cnv = draw.criaTopCnv("c")
    top = draw.criaTopCnv("t")
    cnv.destroy()
    cnv = draw.criaTopCnv("nc")
    tabuleiro = [0 for x in tabuleiro]
    draw.desenhaMenu()
 
def clickEvent(event):
    global numTentativaAtual

    cnv = draw.criaTopCnv("c")

    if (checkState() != "Jogo"):
        return

    cId = event.widget.find_closest(event.x, event.y)

    init = (numCores + 2) + numTentativaAtual * (numCores - 2 + 1)  #(numCores+2) * numTentativaAtual
    
    corSelecionada = cnv.gettags(numCores+1)

    if(cId[0] > 0 and cId[0] <= numCores): #
        for i in range(1,numCores+1):
            if cnv.itemcget(i,"outline")=="gold":
               cnv.itemconfigure(i, outline = "black") 
        cnv.itemconfigure(cId[0], outline = "gold")
        cnv.dtag(numCores+1, corSelecionada[0])
        cnv.addtag_withtag(retCor(cId[0]), numCores+1)
        return
       
    #Verifica se o id do objeto clicado esta na fileira correspondente a tentativa
    if cId[0] >= init and cId[0] <= init + numCores - 3 and corSelecionada[0]!="gray":
        cnv.itemconfigure(cId[0], fill = corSelecionada[0])
        tentativaAtual[cId[0]-init] = retCor(corSelecionada[0])
        controleBotoesJogo(True, tentativaAtual)

    return

def keyEvent(event):
    cnv = draw.criaTopCnv("c")
    if len(event.char) == 1 and ord(event.char) == 27 and checkState() == "Jogo":
        for i in range(1,numCores+1):
            if cnv.itemcget(i,"outline") == "gold":
               cnv.itemconfigure(i, outline = "black") 
        cnv.dtag(numCores + 1, cnv.gettags(numCores + 1))
        cnv.addtag_withtag("gray", numCores + 1)
    return

def salvaJogo():
    global senha, numTentativaAtual, tabuleiro
                                                            # padrao do arquivo
    jogoSalvo = open("save.txt","w")                        #1 numero da tentativa atual
    jogoSalvo.write(str(numTentativaAtual)+"\n")            #2 senha
                                                            #... 1 fileira do tabuleiro pra cada linha
    for i in senha:
        jogoSalvo.write(str(i))
        jogoSalvo.write(" ")
    jogoSalvo.write("\n")

    for tent in tabuleiro:

        for slot in tent:
            jogoSalvo.write(str(slot))
            jogoSalvo.write(" ")
        jogoSalvo.write("\n")

    messagebox.showinfo(message="O jogo foi salvo!")
    jogoSalvo.close()
    
def carregaJogo():
    global senha, tabuleiro, numTentativaAtual

    jogoSalvo = open("save.txt", "r")
    numTentativaAtual = int(jogoSalvo.readline())
    senha = jogoSalvo.readline().strip().split(" ")

    for i in range(len(senha)):
        senha[i] = int(senha[i])

    tabuleiro = [[] for x in range(2 * len(senha))]
    pinos = []

    count = 0
    for linha in jogoSalvo:
        aux = linha.strip().split(" ")
        for j in range(len(aux)):
            aux[j] = int(aux[j])
        tabuleiro[count] = aux.copy()
        pinosAux = gameRules.checaResposta(aux)
        pinos.append(pinosAux)
        count += 1
    
    changeState("Salvo")

    comecaJogo(len(senha) - 3)
    count = 0
   
    for dicas in pinos:
        draw.desenhaPinos(dicas,count)
        count += 1

    jogoSalvo.close()


def retCor(cor): #recebe string -> retorna int // recebe int -> retorna string

    if cor == 1:
        return "red"
    elif cor == 2:
        return "green"
    elif cor == 3:
        return "blue"
    elif cor == 4:
        return "yellow"
    elif cor == 5:
        return "pink"
    elif cor == 6:
        return "deep sky blue"
    elif cor == 7:
        return "brown"
    elif cor == 8:
        return "khaki3"

    elif cor == "red":
        return 1
    elif cor == "green":
        return 2
    elif cor == "blue":
        return 3
    elif cor == "yellow":
        return 4
    elif cor == "pink":
        return 5
    elif cor == "deep sky blue":
        return 6
    elif cor == "brown":
        return 7
    elif cor == "khaki3":
        return 8

