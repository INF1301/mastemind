from model import gameRules
from view import draw
import tkinter as tk


def escolheDif (esc,cnv,top):    
    global ntentativas,numCores,corSelecionada
    
    numCores=gameRules.defineDiff(esc)
    
    draw.limpaTelaInit(cnv,top)
    draw.palheta(numCores)
    
    senha=gameRules.geraSenha()
    draw.desenhaSenha(senha)##esconder senha
    tab=gameRules.jogadasTab()
    draw.desenhaProgresso(tab)  
    bCheck=tk.Button(cnv,text='Check',font='Arial 10 bold',height = 4, width = 10, border=5,command=lambda:checkButton());bCheck.place(x=650,y=500)
    ##melhorar botão
    ntentativas=0

def clickEvent(event, cnv):
    cId = event.widget.find_closest(event.x, event.y)
    ##resolver proximidade click
    
    init = numCores*2#+ntentativas+1   (lembrar da linha)
    ##inserir cor em tentativa
    
    corSelecionada = cnv.gettags(numCores+1)
    print(corSelecionada[0])

    print(cId[0])
    if(cId[0] > 0 and cId[0] <= numCores):
        cnv.dtag(numCores+1, corSelecionada[0])
        cnv.addtag_withtag(retCor(cId[0]), numCores+1)
        return
       
    if cId[0] >= init and cId[0] <= init + numCores - 3:
        cnv.itemconfigure(cId[0], fill = corSelecionada[0])
    return 
 
##def checkButton(ntentativas?):
    ##ntentativas+=1
    ##gameRules.checaResposta()
    ##inserir em tabslots(em checaResposta?)
    ##draw tentativa
    
    ##tabela dicas
    
##def drawDica(tab) draw

##def limpaTentativa() #ESC
   
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



    