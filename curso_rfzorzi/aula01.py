from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_cidade.delete(0, END)
    def conecta_db(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_db(self):
        self.conn.close(); print("Banco de dados desconectado")
    def montaTabelas(self):
        self.conecta_db()
        ### Criar tabela
        self.cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
                );
            """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_db();
    def add_cliente(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.telefone = self.entry_telefone.get()
        self.cidade = self.entry_cidade.get()

        self.conecta_db()
        self.cursor.execute(
            """ 
                INSERT INTO clientes (nome_cliente, telefone, cidade) 
                VALUES (?, ?, ?)
            """, (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()

        lista = self.cursor.execute(
            """
                SELECT * FROM clientes ORDER BY nome_cliente ASC;
            """
        )
        for i in lista:
            self.listaCli.insert("", END, values=i)
            print(i)
        self.desconecta_db()


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=600)
        self.root.minsize(width=500, height=400)
    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        ### Criação do Botão Limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação do Botão Buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação do Botão Novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação do Botão Alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação do Botão Apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação de label e entrada do codigo do cliente
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.entry_codigo = Entry(self.frame_1, bg='white')
        self.entry_codigo.place(relx=0.05, rely=0.15, relwidth=0.08)

        ### Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.entry_nome = Entry(self.frame_1, bg='white')
        self.entry_nome.place(relx=0.05, rely=0.45, relwidth=0.85)

        ### Criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.entry_telefone = Entry(self.frame_1, bg='white')
        self.entry_telefone.place(relx=0.05, rely=0.7, relwidth=0.4)

        ### Criação da label e entrada do cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.entry_cidade = Entry(self.frame_1, bg='white')
        self.entry_cidade.place(relx=0.5, rely=0.7, relwidth=0.4)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

Application()