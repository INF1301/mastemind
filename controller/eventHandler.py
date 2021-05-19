from model import gameRules
from view import draw
import tkinter as tk


def escolheDif (esc,cnv,top):    
    global estado
    estado="menu"
    
    nc=gameRules.defineDiff(esc)
    
    draw.limpaTelaInit(cnv,top)
    draw.palheta(nc)
    
    senha=gameRules.geraSenha()
    draw.desenhaSenha(senha)
    t=gameRules.jogadasTab()
    draw.desenhaProgresso(t)
    
def jogada():
    #Guarda tentativa
    #desenha tentativa atualizando
    #

    
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

    


    