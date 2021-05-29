from model import gameRules
from view import draw
import tkinter as tk


def escolheDif (esc,cnv,top):    
    global ntentativas,numCores,corSelecionada,tentativas
    
    numCores=gameRules.defineDiff(esc)

    tentativas=[]
    for i in range(0,numCores-2):
        tentativas.append(0)
    
    
    draw.limpaTelaInit(cnv,top)
    draw.palheta(numCores)
    
    senha=gameRules.geraSenha()
    
    tab=gameRules.jogadasTab()
    draw.desenhaProgresso(tab,cnv)
   
    ntentativas=0
    
def drawProsseguir(existe,tentativa,cnv):
    global checaTentativa
    if (existe==False):
        checaTentativa=tk.Button(cnv,text='Prosseguir',font='Arial 10 bold',height = 4, width = 15, border=5,command=lambda:mostraDicas(tentativas,cnv),state="disabled");checaTentativa.place(x=785,y=350)
    elif (existe==True):
        if(0 not in tentativa):
            checaTentativa.configure(state= "normal")
        else:
            checaTentativa.configure(state= "disabled")  


def mostraDicas(tentativas,cnv):
    global ntentativas, checaTentativa
    dicas=[]
    dicas=gameRules.checaResposta(tentativas)
    draw.desenhaPinos(dicas,cnv,ntentativas)
    ntentativas+=1
    checaTentativa.configure(state= "disabled")
    
    for k in range(numCores-2):
        tentativas[k]=0
  
def clickEvent(event, cnv):
    global ntentativas
    if draw.statecheck()=="Menu":
        return
    cId = event.widget.find_closest(event.x, event.y)
    print("-",ntentativas)
    init = numCores+2 +ntentativas*(numCores-2+1)  #(numCores+2)*ntentativas
    
    corSelecionada = cnv.gettags(numCores+1)
    print(corSelecionada[0])

    print(cId[0])
    if(cId[0] > 0 and cId[0] <= numCores):
        for i in range(1,numCores+1):
            if cnv.itemcget(i,"outline")=="gold":
               cnv.itemconfigure(i, outline = "black") 
        cnv.itemconfigure(cId[0], outline = "gold")
        cnv.dtag(numCores+1, corSelecionada[0])
        cnv.addtag_withtag(retCor(cId[0]), numCores+1)
        return
       
    if cId[0] >= init and cId[0] <= init + numCores - 3 and corSelecionada[0]!="gray":
        cnv.itemconfigure(cId[0], fill = corSelecionada[0])
        tentativas[cId[0]-init]=retCor(corSelecionada[0])
        print(tentativas)
        drawProsseguir(True,tentativas,cnv)
      

    return 

def keyEvent(event, cnv):

    if len(event.char)==1 and  ord(event.char)==27 and draw.statecheck()=="Jogo":
        for i in range(1,numCores+1):
            if cnv.itemcget(i,"outline")=="gold":
               cnv.itemconfigure(i, outline = "black") 
        cnv.dtag(numCores+1, cnv.gettags(numCores+1))
        cnv.addtag_withtag("gray", numCores+1)
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
    elif cor == "red":
        return 1
    elif cor == "green":
        return 2
    elif cor == "blue":
        return 3
    elif cor == "yellow":
        return 4
    elif cor == "pink":
        return 5
    elif cor == "deep sky blue":
        return 6
    elif cor == "brown":
        return 7
    elif cor == "khaki3":
        return 8



    
