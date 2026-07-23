from TelaBase import TelaBase, tk, ttk
from DataBase import DataBase

class TelaEscolhaTabela(TelaBase):
    y = 0
    lista = []

    def abrirTabela(self, tabela:tuple):
        self.gerenciador.telas["tabelas"].setTabela(tabela[0])
        self.gerenciador.mostrarTela("tabelas")

    def criarTabelas(self):
        self.gerenciador.mostrarTela("criarTabelas")

    def __init__(self, root, gerenciador, db):
        super().__init__(root)


        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.gerenciador = gerenciador
        self.db = db

        self.interface()
        

    def interface(self):
        self.botao()
        self.botaoDasTabela()

    def botaoDasTabela(self):
        tabelas = self.db.MostrarTabelas()
        for nome in tabelas:
            botao = tk.Button(self.frame, text=nome, command=lambda t=nome: self.abrirTabela(t))
            botao.place(relx=0.00,rely=self.y)
            self.y += 0.05

    def atualizar(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.y = 0
        self.interface()

    def botao(self):
        tk.Button(self.frame, text="Criar Tabelas", command=lambda:self.criarTabelas()).place(relx=0.90, rely = 0.81)
        tk.Button(self.frame, text="Remover Tabelas", command=lambda:self.removerTabelas()).place(relx=0.90, rely = 0.84)
        tk.Button(self.frame, text="Alterar Tabelas", command=lambda:self.alterarTabelas()).place(relx=0.90, rely = 0.90)
        tk.Button(self.frame, text="Trocar Banco de Dados", command=lambda:self.database()).place(relx=0.90, rely = 0.87)

    def database(self):
        self.gerenciador.mostrarTela("dataBase")

    def removerTabelas(self):
        self.gerenciador.mostrarTela("removerTabela")

    def alterarTabelas(self):
        self.gerenciador.mostrarTela("alterarTabela")


class RemoverTabela(TelaBase):
    def __init__(self, root, gerenciador, db):
        super().__init__(root)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.gerenciador = gerenciador
        self.db = db

        self.interface()

    def interface(self):
        tk.Label(self.frame, text="Nome da Tabela").place(x= 0, y = 0)
        self.Entrys()
        self.Botao()

    def Entrys(self):
        self.nomeTabela = tk.Entry(self.frame)
        self.nomeTabela.place(x = 100, y = 0)

    def Botao(self):
        tk.Button(self.frame, text="Remover Tabela", command=lambda: self.removerTabela()).place(relx = 0.9, rely = 0.85)
        tk.Button(self.frame, text="Voltar", command=lambda:self.voltar()).place(relx = 0.9, rely = 0.88)

    def voltar(self):
        self.gerenciador.telas["escolhaDeTabelas"].atualizar()
        self.gerenciador.mostrarTela("escolhaDeTabelas")

    def removerTabela(self):
        info = self.nomeTabela.get()

        self.db.removerTabela(info)
    
class AlterarTabela(RemoverTabela):
    def __init__(self, root, gerenciador, db):
        super().__init__(root, gerenciador, db)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        self.gerenciador = gerenciador
        self.db = db

        self.interface()

    def interface(self):
        tk.Label(self.frame, text="Nome da Tabela Antiga").place(x= 0, y = 0)
        tk.Label(self.frame, text="Nome da Tabela Nova").place(x= 0, y = 50)
        self.Entrys()
        self.Botao()

    def Entrys(self):
        self.nomeTabela = tk.Entry(self.frame)
        self.nomeTabela.place(x = 150, y = 0)

        self.nomeTabelaAtual = tk.Entry(self.frame)
        self.nomeTabelaAtual.place(x = 150, y = 50)

    def Botao(self):
        tk.Button(self.frame, text="Alterar Tabela", command=lambda: self.alterarTabela()).place(relx = 0.9, rely = 0.85)
        tk.Button(self.frame, text="Voltar", command=lambda:self.voltar()).place(relx = 0.9, rely = 0.88)

    def alterarTabela(self):
        info = [self.nomeTabela.get(), self.nomeTabelaAtual.get()]

        self.db.alterarTabela(info)

class Coluna:
    y=40
    nomeTabela = ""
    autoIncrement = None
    instancias = []
    
    
    def __init__(self, frame, db):
        self.frame = frame
        self.db = db
        self.nomeTabela = tk.Entry(frame, width=15)
        self.nomeColuna = tk.Entry(frame, width=15)
        self.tipo = tk.StringVar(value=False)
        self.tamanho = tk.Entry(frame, width=15)
        self.primary = tk.BooleanVar()
        self.default = tk.BooleanVar()
        self.comment = tk.BooleanVar()
        self.unsigned = tk.BooleanVar()
        self.unique = tk.BooleanVar()
        self.auto = tk.BooleanVar()
        self.null = tk.BooleanVar()
        self.instancias.append(self)
        
    def printData(self):
        for i in range(len(self.instancias)):
            '''print(f"primary {self.instancias[i].primary} instancia: {i}", end="\n")
            print()
            print(f"default {self.instancias[i].default} instancia: {i}", end="\n")
            print()
            print(f"comment {self.instancias[i].comment} instancia: {i}", end="\n")
            print()
            print(f"unsigned {self.instancias[i].unsigned} instancia: {i}", end="\n")
            print()
            print(f"unique {self.instancias[i].unique} instancia: {i}", end="\n")
            print()
            print(f"null {self.instancias[i].null} instancia: {i}", end="\n")
            print(f"AI {self.instancias[i].auto.get()} instancia: {i}")
            print(f"AI {self.instancias[i].tipo} instancia: {i}")
            print(f"AI {self.instancias[i].unique} instancia: {i}")
            print(f"AI {self.instancias[i].primary} instancia: {i}")'''
            print(f"Nome Tabela {self.instancias[i].nomeTabela} instancia: {i}")
            print(f"Nome Coluna {self.instancias[i].nomeColuna} instancia: {i}")
            print(f"tamanho {self.instancias[i].tamanho} instancia: {i}")

    def transformQuery(self):
        #nomeColuna tipo valores atribultos
        query = ""
        for obj in self.instancias:
            query += obj.nomeColuna.get()
            query += f" {obj.tipo.get()}"
            query += f"({obj.tamanho.get()})"

            if obj.null.get():
                query += " NULL"

            if obj.default.get():
                query += " DEFAULT """

            if obj.auto.get():
                query += " AUTO_INCREMENT PRIMARY KEY UNIQUE"
            
            if obj.unique.get() and not obj.auto.get():
                query += " UNIQUE"

            if obj.comment.get():
                query += " COMMENT """
        
            query += ",\n"

        query = query.removesuffix("\n")
        query = query.removesuffix(",")
        self.db.CriarTabelas(self.nomeTabela.get(), query)
        
        

    def getCheckBox(self):
        x = 0
        for obj in self.instancias:
            print(f"{obj.nomeTabela.get()} instancia: {x}")
            print(f"{obj.nomeColuna.get()} instancia: {x}")
            print(f"{obj.tamanho.get()} instancia: {x}")
            print(f"{obj.tipo.get()} instancia: {x}")
            print(f"{obj.primary.get()} instancia: {x}")
            print(f"{obj.default.get()} instancia: {x}")
            print(f"{obj.comment.get()} instancia: {x}")
            print(f"{obj.unsigned.get()} instancia: {x}")
            print(f"{obj.unique.get()} instancia: {x}")
            print(f"{obj.auto.get()} instancia: {x}")
            print(f"{obj.null.get()} instancia: {x}")
            print("--------------------------------------")

            x += 1


    def getEntrys(self):

        print(f"tabela {self.nomeTabela.get()} instancia: ")
        print(f"coluna {self.nomeColuna.get()} instancia: ")
        print(f"tamanho {self.tamanho.get()} instancia: ")
        
    def verificar(self):
        for obj in self.instancias:
            if obj.auto.get():
                obj.primary.set(True)
                obj.unique.set(True)
                obj.null.set(False)
                obj.tipo.set("INT")
                obj.deixarAutoIncrementTrue()
                #obj.printData()
            else:
                obj.auto.set(False)
                obj.primary.set(False)
                obj.unique.set(False)
                obj.null.set(False)
                obj.tipo.set(False)
        self.getCheckBox()

    def deixarAutoIncrementTrue(self):
        if Coluna.autoIncrement is not None:
            Coluna.autoIncrement.auto.set(False)
        
        Coluna.autoIncrement = self
        self.auto.set(True)
        

    def to_sql(self):
        pass

class CriarTabelas(TelaBase):
    def __init__(self, root, gerenciador, db):
        super().__init__(root)
        self.y = 40
        self.gerenciador = gerenciador
        self.db = db

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.botoes()
        self.Labels()

        self.Interface()

    def botoes(self):
        tk.Button(self.frame, text="Voltar", command=lambda: self.voltar()).place(relx=0.9, rely=0.88)
        tk.Button(self.frame, text="Criar nova tabela", command=lambda: self.criarTabelas()).place(x=1250, y=700)
        tk.Button(self.frame, text="Nova coluna", command=lambda:self.Interface()).place(x=1250, y=40) 
        tk.Button(self.frame, text="Excluir coluna", command=lambda:self.ExcluirColuna()).place(x=1350, y=40) 

    def ExcluirColuna(self):
        pass

    def destroy(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.y = 40
        self.Interface()

    def voltar(self):
        self.destroy()
        self.gerenciador.mostrarTela("escolhaDeTabelas")


    def criarTabelas(self):
        self.coluna.transformQuery()

    def Interface(self):
        self.coluna = Coluna(self.frame, self.db)
        if self.coluna.nomeTabela.winfo_children == 1:
            pass
        else:
            self.EntrysNomeTabela()
            self.botoes()
            self.Labels()

        self.Entrys()
        self.checkBox()
        self.checkBoxAI()
        self.RadioboxDataType()

        self.y += 40

    def Labels(self):
        lista = ["Nome da Tabela","Nome da Coluna","Inteiro","Texto", "Data", "Tamanho", "Unico","Chave Primaria", "Default", "comment", "Unsigned","Auto incrementar","Null"]
        x = 0
        for nome in lista:
         tk.Label(self.frame, text=nome).place(x = x , y = 0)
         x += 100
        
    
    def EntrysNomeTabela(self):
        self.coluna.nomeTabela.place(x = 0, y = 40)

    def Entrys(self):

        self.coluna.nomeColuna.place(x = 110, y = self.y)
        self.coluna.tamanho.place(x = 500, y = self.y)


    def RadioboxDataType(self):

        tk.Radiobutton(self.frame, variable=self.coluna.tipo, value="INT", command=lambda:self.coluna.getCheckBox()).place(x = 200, y = self.y)
        tk.Radiobutton(self.frame, variable=self.coluna.tipo, value="VARCHAR", command=lambda:self.coluna.getCheckBox()).place(x = 300, y = self.y)
        tk.Radiobutton(self.frame, variable=self.coluna.tipo, value="DATA", command=lambda:self.coluna.getCheckBox()).place(x = 400, y = self.y)
    
    def checkBox(self):
        y = self.y

        tk.Checkbutton(self.frame, variable=self.coluna.unique, command=lambda:self.coluna.getCheckBox()).place(x = 600, y = y)
        tk.Checkbutton(self.frame, variable=self.coluna.primary,  command=lambda:self.coluna.getCheckBox()).place(x = 700, y = y)
        tk.Checkbutton(self.frame, variable=self.coluna.default,  command=lambda:self.coluna.getCheckBox()).place(x = 800, y = y)
        tk.Checkbutton(self.frame, variable=self.coluna.comment, command=lambda:self.coluna.getCheckBox()).place(x = 900, y = y)
        tk.Checkbutton(self.frame, variable=self.coluna.unsigned,  command=lambda:self.coluna.getCheckBox()).place(x = 1000, y = y)
        tk.Checkbutton(self.frame, variable=self.coluna.null,  command=lambda:self.coluna.getCheckBox()).place(x = 1200, y = y)

    def checkBoxAI(self):

        tk.Checkbutton(self.frame, variable=self.coluna.auto, command=lambda:self.coluna.verificar()).place(x = 1100, y=self.y)
    
    
        
    
        
        
       
        

        
            
        




        