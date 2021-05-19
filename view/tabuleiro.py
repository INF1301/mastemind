import tkinter as tk

def checkButton(cnv):
    bcheck=cnv.create_polygon(600,900,650,900,600,890,fill="green")
   
def retCor(cor):

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
    else:
        return "khaki3"


tabuleiro = tk.Tk()

palhetaCores = [1, 2, 3, 4, 5, 6, 7, 8]

limiteJogadas = 12
numPedras = 6
numCores = 8

tabSlots = []

for tent in range(limiteJogadas):
    preenche = []
    tabSlots.append(preenche)
    for _ in range (numPedras):
        tabSlots[tent].append(0)


tx = 700
ty = 1000


cnv = tk.Canvas(tabuleiro, bg="purple", height=tx, width=ty)
tabuleiro.title("Master Mind")


x0 = 250
y0 = 30

xLinhas = 200
yLinhas = y0 + 37.5



for linha in tabSlots:
    xAux = x0
    for slot in linha:
        if(slot == 0):
            cnv.create_oval(xAux, y0, xAux + 30, y0 + 30, fill="gray")
        ##else:
            ##cor = funcRetornaStringCor(slot)
            ##cnv.create_oval(x0, y0, x0 + 50, y0 + 50, fill=cor)
        xAux += 55
    cnv.create_line(xLinhas, yLinhas, xLinhas + 500, yLinhas, width = 2)
    yLinhas += 45
    y0 += 45


xCores = x0 - 5
yCores = 600
for cor in range(numCores):
    corAtual = retCor(palhetaCores[cor])
    cnv.create_oval(xCores, yCores, xCores + 40, yCores + 40, fill=corAtual)
    xCores += 54


cnv.pack()
tabuleiro.mainloop()
