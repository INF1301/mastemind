from model import gameRules
from controller import eventHandler
import tkinter as tk
from functools import partial

x0 = 250
y0 = 30

palhetaCores = [1, 2, 3, 4, 5, 6, 7, 8]

def drawTelaInit(cnv,t,tx,ty):
    global titulo,novoJogo,bJogoSalvo,bFacil,bMedio,bDificil
   
    titulo = tk.Label (t, text='Master Mind')
    titulo.place (x=300,y=10)

    titulo.configure( font='Arial 50 bold',background='green')
    novoJogo=tk.Label(t,text='Novo jogo',font='Calibre 30 bold', bg="purple");novoJogo.place(x=400,y=150)
    bJogoSalvo=tk.Button(t,text='Jogo Salvo ',font='Arial 10 bold',height = 4, width = 100, border=5,state="disabled");bJogoSalvo.place(x=90,y=400)
    bFacil=tk.Button(cnv,text='Facil',font='Arial 10 bold',height = 4, width = 30 , border=5, command=lambda:eventHandler.escolheDif(1,cnv,t));bFacil.place(x=90,y=ty/4)
    bMedio=tk.Button(cnv,text='Medio',font='Arial 10 bold',height = 4, width = 30 , border=5,command=lambda:eventHandler.escolheDif(2,cnv,t));bMedio.place(x=370,y=ty/4)
    bDificil=tk.Button(cnv,text='Dificil',font='Arial 10 bold',height = 4, width = 30, border=5, command=lambda:eventHandler.escolheDif(3,cnv,t));bDificil.place(x=650,y=ty/4)
    
 
def limpaTelaInit(cnv,top):
    global tela
    bFacil.destroy()
    bMedio.destroy()
    bDificil.destroy()
    titulo.destroy()
    novoJogo.destroy()
    bJogoSalvo.destroy()
    tela=cnv

    
    
def desenhaSenha(senha):
    ly=y0
    xL = 700
    yL=100
    
    for i in senha:
        
        poscor=eventHandler.retCor(i)
        tela.create_oval(xL,yL,xL+40,yL+40,fill=poscor)
        xL+=50
 
def palheta(numCores):
    xCores = x0 - 5
    yCores = 600
    for cor in range(numCores):
        corAtual = eventHandler.retCor(palhetaCores[cor])
        tela.create_oval(xCores, yCores, xCores + 40, yCores + 40, fill=corAtual)
        xCores += 54

    
def desenhaProgresso(tabSlots):
    ly=y0
    xL = 200
    yL = ly + 37.5
    for linha in tabSlots:
        xAux = x0
        for slot in linha:
            if(slot == 0):
                tela.create_oval(xAux, ly, xAux + 30, ly + 30, fill="gray")
            else:
                cor = eventHandler.retCor(slot)
                tela.create_oval(x0, ly, x0 + 50, ly + 50, fill=cor)
            xAux += 55
        tela.create_line(xL, yL, xL + 500, yL, width = 2)
        yL += 45
        ly += 45
    tela.create_oval(30, 400, 60, 430, fill="yellow", tag="gray", state = 'hidden')

