from view import draw
from controller import eventHandler
from model import gameRules
from functools import partial


import tkinter as tk

# Criação da janela principal

top = tk.Tk()
tx=700
ty=1000
global menu
menu=True

# Criação de um canvas na janela principal

cnv = tk.Canvas(top, bg="purple", height=tx, width=ty)
top.title('Master Mind')
print("cadeira")

if (menu==True):
    
    draw.drawTelaInit(top,tx,ty)

    
    bFacil=tk.Button(top,text='Facil',font='Arial 10 bold',height = 4, width = 30 , border=5, command=partial(eventHandler.escolheDif,1,cnv));bFacil.place(x=90,y=ty/4)
    bMedio=tk.Button(top,text='Medio',font='Arial 10 bold',height = 4, width = 30 , border=5,command=partial(eventHandler.escolheDif,2,cnv));bMedio.place(x=370,y=ty/4)
    bDificil=tk.Button(top,text='Dificil',font='Arial 10 bold',height = 4, width = 30, border=5, command=partial(eventHandler.escolheDif,3,cnv) );bDificil.place(x=650,y=ty/4)

    bJogoSalvo=tk.Button(top,text='Jogo Salvo ',font='Arial 10 bold',height = 4, width = 100, border=5 );bJogoSalvo.place(x=90,y=400)
    





cnv.pack()
if (menu==False):
    top.destroy()



top.mainloop()
cnv.create_rectangle(1000,1000,0,0,fill='blue')
top.quit()





