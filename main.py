from view import draw
from controller import eventHandler
from model import gameRules
import tkinter as tk


# Criação da janela principal

draw.criaTopCnv(0)
top = draw.criaTopCnv("t")
cnv = draw.criaTopCnv("c")

# Criação de um canvas na janela principal

top.title('Master Mind')

draw.desenhaMenu()

cnv.pack()

top.mainloop()

