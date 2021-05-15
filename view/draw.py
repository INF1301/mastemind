from model import gameRules
from controller import eventHandler
import tkinter as tk
from functools import partial


def drawTelaInit(t,tx,ty):
    titulo = tk.Label (t, text='Master Mind')
    titulo.place (x=300,y=10)

    titulo.configure( font='Arial 50 bold',background='green')
    novoJogo=tk.Label(t,text='Novo jogo',font='Calibre 30 bold', bg="purple");novoJogo.place(x=400,y=150)



def limpaTelaInit(cnv):
    print("lambda")
    menu=False
    cnv.delete("all")
    cnv.create_rectangle(1000,1000,0,0,fill='blue')
