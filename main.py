from view import draw
import tkinter as tk

# André C. de Andrade - 2012498
# Laura M. da Glória Luz -2010709
# Paulo de Tarso Fernandes - 2011077

# Criação da janela principal

draw.criaTopCnv(0)
top = draw.criaTopCnv("t")
cnv = draw.criaTopCnv("c")

# Criação de um canvas na janela principal

top.title('Master Mind')

draw.desenhaMenu()

cnv.pack()

top.mainloop()

