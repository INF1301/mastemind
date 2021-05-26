from model import gameRules
from view import draw
import tkinter as tk


def escolheDif (esc,cnv,top):    
    global ntentativas,numCores,corSelecionada
    
    numCores=gameRules.defineDiff(esc)
    
    draw.limpaTelaInit(cnv,top)
    draw.palheta(numCores)
    
    senha=gameRules.geraSenha()
    draw.desenhaSenha(senha)
    tab=gameRules.jogadasTab()
    draw.desenhaProgresso(tab)
   
    ntentativas=1
 
def clickEvent(event, cnv):
    cId = event.widget.find_closest(event.x, event.y)
    s = 4
    init = (numCores + 1 + s)

    corSelecionada = cnv.gettags(51)
    print(corSelecionada[0])

    print(cId[0])
    if(cId[0] > 0 and cId[0] <= numCores):
        cnv.dtag(51, corSelecionada[0])
        cnv.addtag_withtag(retCor(cId[0]), 51)
        return

    if (numCores == 7):
        init += 2
    elif (numCores == 8):
        init += 4

    if cId[0] >= init and cId[0] <= init + numCores - 3:
        cnv.itemconfigure(cId[0], fill = corSelecionada[0])
    return 
   
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
    elif cor==8:
        return "khaki3"    



    