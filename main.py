from view import draw
from controller import eventHandler
from model import gameRules
##from functools import partial
import tkinter as tk

# Criação da janela principal

top = tk.Tk()
tx=700
ty=1000


# Criação de um canvas na janela principal

cnv = tk.Canvas(top, bg="purple", height=tx, width=ty)
top.title('Master Mind')


draw.drawTelaInit(cnv,top,tx,ty)

cnv.bind('<Button-1>',lambda event: eventHandler.clickEvent(event,cnv))


cnv.pack()
top.mainloop()

