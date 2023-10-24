from tkinter import *
from tkinter import messagebox
from requests import *

######### Consumindo API ############

url = get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
url_format = url.json()

dolar_atual = url_format['USDBRL']['bid']
dolar_atual = float(dolar_atual)
dolar_atual = round(dolar_atual,2)

euro_atual = url_format['EURBRL']['bid']
euro_atual = float(euro_atual)
euro_atual = round(euro_atual,2)


########### INTERFACE GRAFICA  ###############

janela_principal = Tk() #Criando a tela principal
janela_principal.title('Conversor de Moedas')  #titulo
janela_principal.geometry('310x430+400+200')  #dimenções 
janela_principal.resizable(False, False)   #Fixando o tamanho da janela
janela_principal.config(background='#90EE90' ) #Adicioando cores

########### FUNÇÕES  ###############

def converter():
    try: 
        if text_real.get() == '' and text_euro.get() == '':                           #Convertando os valores das 3 moedas !! Real , Euro e Dolar.
            dolar = float(text_dolar.get())

            real = dolar * dolar_atual
            text_real.insert(0,round(real,3))

            euro = real / euro_atual
            text_euro.insert(0,round(euro,3))

        elif text_dolar.get() == '' and text_euro.get() == '':    
            real = float(text_real.get())

            dolar = real / dolar_atual
            text_dolar.insert(0,round (dolar,3))

            euro = real / euro_atual
            text_euro.insert(0,round(euro,3))

        elif text_real.get() == '' and text_dolar.get() == '':
            euro = float(text_euro.get())

            real = euro * euro_atual
            text_real.insert(0,round(real,3))

            dolar = real / dolar_atual
            text_dolar.insert(0,round(dolar,3))

    except ValueError:
        messagebox.showerror('ADD um valor!')               #Tratando os erros de não digitar nem um número e digitando letras!! 

def limpar():   
    text_euro.delete(0,END) 
    text_real.delete(0,END)
    text_dolar.delete(0,END)


########### COMPONENTES  ###############



frame_euro= Frame(janela_principal, borderwidth=1.5, relief='solid', bg='#90EE90')
label_euro = Label(janela_principal, text='EURO', bg='#90EE90')
text_euro= Entry(frame_euro, width=34)

frame_dolar = Frame(janela_principal, borderwidth=1.5, relief='solid', bg='#90EE90')
label_dolar= Label(janela_principal, text='DOLAR', bg='#90EE90')
text_dolar= Entry(frame_dolar, width=34)

frame_real = Frame(janela_principal, borderwidth=1.5, relief='solid', bg='#90EE90')
label_real= Label(janela_principal, text='REAL', bg='#90EE90')
text_real= Entry(frame_real, width=34)


botao_converter = Button(janela_principal, text='Converter', font= ('Georgia', 15), highlightthickness=0, bd=0 ,command=converter)
botao_limpar = Button(janela_principal, text='Limpar', highlightthickness=0, bd=0, command=limpar)



########### LAYOUT - POSICIONAMENTO (CSS)  ###############

#campos texto
frame_euro.place(x=5 , y=85 , width=295, height=48)
label_euro.place(x=8 , y=75)
text_euro.place(x=5, y=15)

frame_dolar.place(x=5, y=165 , width=295, height=48)
label_dolar.place(x=8 , y=155)
text_dolar.place(x=5, y=15)

frame_real.place(x=8, y=245 , width=295, height=48)
label_real.place(x=11, y=235)
text_real.place(x=5, y=15)

#botões
botao_converter.place(x=85, y=350)
botao_limpar.place(x=250,y=310)


janela_principal.mainloop() # Faz a tela aparecer