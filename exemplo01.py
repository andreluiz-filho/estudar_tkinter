"""Exemplo 01."""
from tkinter import Tk, Label, Button

#-------------------------------------------
#------------------Funções------------------

def fui_clicado():
    print("Fui clicado!!! ")

#-------------------------------------------

janela = Tk()

texto = Label(
    text='Live de Python',
    font=('Arial', 50)
)
texto.pack()

botao = Button(
    text='Click here',
    font=('Arial', 50),
    command=fui_clicado
)
botao.pack()

def muda_label(event):
    print('Apertei 1')
    texto.config(text = 'Apertei 1')

janela.bind('1', muda_label)
janela.mainloop()