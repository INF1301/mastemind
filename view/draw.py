from model import gameRules
from controller import eventHandler
import tkinter as tk
from functools import partial
top = 0
cnv = 0

x0 = 250
y0 = 510

tx = 700
ty = 1000

palhetaCores=[1, 2, 3, 4, 5, 6, 7, 8]

def criaTopCnv(string):# Cria, retorna ou modifica o Canvas ou Top
    global top,cnv, tx, ty

    if(string=="t"):
        return top

    if (string=="c"):
        return cnv

    elif (string=="nc"):
        cnv = tk.Canvas(top, bg="purple", height=tx, width=ty)
        cnv.bind('<Button-1>',eventHandler.clickEvent)
        cnv.pack()
        return cnv

    else:
        top = tk.Tk()
        cnv = tk.Canvas(top, bg="purple", height=tx, width=ty)
        cnv.bind('<Button-1>',eventHandler.clickEvent)
        top.bind('<Key>', eventHandler.keyEvent)



def desenhaMenu():
    global titulo, novoJogo, bJogoSalvo, bFacil, bMedio, bDificil, tx, ty, cnv, top
    
    titulo = tk.Label (cnv, text='Master Mind')
    titulo.place (x=300, y=10)
    titulo.configure(font='Arial 50 bold', background='green')

    novoJogo = tk.Label(cnv,text='Novo jogo',font='Calibre 30 bold', bg="purple");novoJogo.place(x=400, y=150)

    bJogoSalvo = tk.Button(cnv,text='Jogo Salvo ',font='Arial 10 bold',height = 4, width = 100, border=5,command=lambda: eventHandler.carregaJogo());
    bJogoSalvo.place(x=90, y=400)

    bFacil = tk.Button(cnv,text='Facil',font='Arial 10 bold',height = 4, width = 30 , border=5, command=lambda:eventHandler.comecaJogo(1))
    bFacil.place(x=90, y=ty/4)

    bMedio = tk.Button(cnv,text='Medio',font='Arial 10 bold',height = 4, width = 30 , border=5,command=lambda:eventHandler.comecaJogo(2))
    bMedio.place(x=370, y=ty/4) 

    bDificil = tk.Button(cnv,text='Dificil',font='Arial 10 bold',height = 4, width = 30, border=5, command=lambda:eventHandler.comecaJogo(3))
    bDificil.place(x=650, y=ty/4)

    eventHandler.changeState("Menu")
    

def limpaMenu():

    bFacil.destroy()
    bMedio.destroy()
    bDificil.destroy()
    titulo.destroy()
    novoJogo.destroy()
    bJogoSalvo.destroy()

    eventHandler.changeState("Jogo")


def desenhaSenha(senha,popup):

    cnv = criaTopCnv("c")
    xL = 700
    yL = 100
    msg = tk.Label (cnv, text='Senha',font='Arial 15 bold', background='green')
    msg.place (x=xL+120, y=yL-40)

    for i in senha:
        poscor = eventHandler.retCor(i)
        cnv.create_oval(xL,yL, xL+40, yL+40, fill=poscor) 
        xL+=50
 
def desenhaPalheta(numCores):
    
    xCores = x0 - 5
    yCores = 600
    for cor in range(numCores):
        corAtual = eventHandler.retCor(palhetaCores[cor])
        cnv.create_oval(xCores, yCores, xCores + 40, yCores + 40, fill=corAtual)
        xCores += 54
    cnv.create_oval(30, 400, 60, 430, fill="yellow", tag="gray",state="hidden")
    
    
def desenhaTabuleiro(tabSlots):
    cnv = criaTopCnv("c")
    eventHandler.controleBotoesJogo(False,0)

    ly = y0
    xL = 200
    yL = ly + 37.5

    for linha in tabSlots:
        xAux = x0
        for slot in linha:
            if(slot == 0):
                cnv.create_oval(xAux, ly, xAux + 30, ly + 30, fill="gray")
            else:
                cor = eventHandler.retCor(slot)
                cnv.create_oval(xAux, ly, xAux + 30, ly + 30, fill=cor)
            xAux += 55
        cnv.create_line(xL, yL, xL + 500, yL, width = 2)
        yL -= 45
        ly -= 45
    
def desenhaPinos(dicas,ntent):
    cnv=criaTopCnv("c")
    x = 590
    ly= 510-ntent*45
    count=0
    for i in dicas:
        if (count==3):
            ly+=20
            x=590
        if(i == True):
            cor="black"
        if (i == False):
           cor="white"
        
        cnv.create_oval(x, ly, x + 10,ly+10, fill=cor)
        count+=1
        x+=25

    return
    

