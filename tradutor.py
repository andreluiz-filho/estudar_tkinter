from tkinter import Tk, ttk, Text, Button
from googletrans import Translator
#from ttkthemes import ThemedTk
#from ttkbootstrap import Style

#---------------------------------------------------------------------

#Janela Tk Default
janela = Tk()

#Janela Tk Themes
#janela = ThemedTk(theme='breeze')

#Janela TTk Bootstrap
#style = Style(theme='pulse')
#janela = style.master

janela.title('Traduza com André!')

#---------------------------------------------------------------------

frame_geral = ttk.Frame()

#---------------------------------------------------------------------

translator = Translator()

#---------------------------------------------------------------------

def traduzir(event=None):
    text = entrada.get('1.0', 'end')
    src  = combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(text=text, src=src, dest=dest)

    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', resultado.text)
    saida.configure(state='disabled')

#---------------------------------------------------------------------

values = ['pt', 'es', 'en']

#---------------------------------------------------------------------

#Entradas
frame_entrada = ttk.Frame(frame_geral)
label_entrada = ttk.Label(frame_entrada, text='Entrada', font=(None, 20))
combo_entrada = ttk.Combobox(frame_entrada, values=values, font=(None, 20))
combo_entrada.set('pt')
entrada = Text(frame_geral, height=5, width=50, font=(None, 15))


label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx=10, pady=10)

frame_entrada.pack()
entrada.pack(padx=20, fill='both', expand=1)

#---------------------------------------------------------------------

#Saidas
frame_saida = ttk.Frame(frame_geral)
label_saida = ttk.Label(frame_saida, text='Saida', font=(None, 20))
combo_saida = ttk.Combobox(frame_saida, values=values, font=(None, 20))
combo_saida.set('en')
saida = Text(frame_geral, height=5, width=50, font=(None, 15), state='disabled')

label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column=1, padx=10, pady=10)

frame_saida.pack()
saida.pack(padx=20, pady=10, fill='both', expand=1)

#---------------------------------------------------------------------
botao = ttk.Button(frame_geral, text='Traduzir', command=traduzir)
botao.pack(padx=20, pady=10, fill='both')
#---------------------------------------------------------------------

frame_geral.pack()

janela.bind('<Return>', traduzir)
janela.mainloop()