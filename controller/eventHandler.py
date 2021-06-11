from model import gameRules
from view import draw
import tkinter as tk
from tkinter import messagebox 


def escolheDif (esc,cnv,top):    
    global ntentativas,numCores,corSelecionada,tentativas,senha,tabuleiro
    
    numCores=gameRules.defineDiff(esc)

    tentativas=[]
    for i in range(0,numCores-2):
        tentativas.append(0)
    
    
    draw.limpaTelaInit(cnv,top)

    draw.palheta(numCores)
    
    senha=gameRules.geraSenha()
    
    tabuleiro=gameRules.jogadasTab()
    draw.desenhaProgresso(tabuleiro,cnv)
   
    ntentativas=0
    
def drawProsseguir(existe,tentativa,cnv):
    global checaTentativa, senha, tabuleiro, ntentativas
    if (existe==False):
        checaTentativa=tk.Button(cnv,text='Prosseguir',font='Arial 10 bold',height = 4, width = 15, border=5,command=lambda:mostraDicas(tentativas,cnv),state="disabled")
        checaTentativa.place(x=785,y=450)
        salvarJogo= tk.Button(cnv, text='Salvar Partida',font='Arial 10 bold',height = 4, width = 15, border=5, command= lambda: gameRules.salvaJogo(senha,tabuleiro,ntentativas))
        salvarJogo.place(x=785,y=350)
    elif (existe==True):
        if(0 not in tentativa):
            checaTentativa.configure(state= "normal") 


def checkState():
    global state
    return state


def changeState(string):
    global state
    state=string

def tabSave():
    global tabuleiro, ntentativas, tentativas
    tabuleiro[ntentativas]=tentativas.copy()


def mostraDicas(tentativas,cnv):
    global ntentativas, checaTentativa
    dicas=[]
    dicas=gameRules.checaResposta(tentativas)
    draw.desenhaPinos(dicas,cnv,ntentativas)
    checaTentativa.configure(state= "disabled")

    if (False not in dicas and len(dicas)==4):
        popup_window("vitoria")
        changeState("Fim")
        return

    tabSave()

    ntentativas+=1
    
    if (ntentativas==(numCores-2)*2):
        popup_window("derrota")
        changeState("Fim")
        return

    for k in range(numCores-2):
        tentativas[k]=0
 


def popup_window(estado):
    global senha
    window = tk.Toplevel()
     
    draw.desenhaSenha(senha,window)
    if (estado=="vitoria"):
        msg="Parabéns, você ganhou!"
    elif (estado=="derrota"):
        msg="Parabéns, você perdeu!"
    

    label = tk.Label(window, text=msg,font='Calibre 10 bold')

    label.pack(fill='none', padx=50, pady=50,side="top")

    button_close = tk.Button(window, text="Encerrar jogo", command=quit)

    # button_novoJogo = tk.Button(window, text="Jogar novamente", command=lambda:drawTelaInit())

    button_close.pack(fill='x')
    # button_novoJogo.pack(fill='x')

 
def clickEvent(event, cnv):
    global ntentativas
    if (checkState()!="Jogo"):
        return
    cId = event.widget.find_closest(event.x, event.y)
    print("-",ntentativas)#
    init = numCores+2 +ntentativas*(numCores-2+1)  #(numCores+2)*ntentativas
    
    corSelecionada = cnv.gettags(numCores+1)
    print(corSelecionada[0])#

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
        print(tentativas)#
        drawProsseguir(True,tentativas,cnv)
      

    return 

def keyEvent(event, cnv):

    if len(event.char)==1 and  ord(event.char)==27 and checkState()=="Jogo":
        for i in range(1,numCores+1):
            if cnv.itemcget(i,"outline")=="gold":
               cnv.itemconfigure(i, outline = "black") 
        cnv.dtag(numCores+1, cnv.gettags(numCores+1))
        cnv.addtag_withtag("gray", numCores+1)
    return
    
#def getcnv():
    

# def reiniciaJogo():
# cnv=getcnv()
# cnv.destroy()
# cnv = tk.Canvas(top, bg="purple", height=tx, width=ty)
# cnv.pack()

# draw.drawTelaInit(cnv,top,tx,ty)

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



    
