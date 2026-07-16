from TelaBase import TelaBase, tk, ttk

class TelaEscolhaTabela(TelaBase):
    y = 0
    lista = []

    def abrirTabela(self, gerenciador, tabela:tuple):
        gerenciador.telas["tabelas"].setTabela(tabela[0])
        gerenciador.mostrarTela("tabelas")

    def criarTabelas(self, gerenciador):
        gerenciador.mostrarTela("criarTabelas")

    def __init__(self, root, gerenciador, db):
        super().__init__(root)


        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.db = db
        tabelas = db.MostrarTabelas()

        for nome in tabelas:
           
           botao = tk.Button(self.frame, text=nome, command=lambda t=nome: self.abrirTabela(gerenciador,t))
           botao.place(relx=0.00,rely=self.y)
           self.y += 0.05
        
        tk.Button(self.frame, text="Criar Tabelas", command=lambda:self.criarTabelas(gerenciador))
    
    


class CriarTabelas(TelaBase):
    def __init__(self, root, gerenciador, db):
        super().__init__(root)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.checkBox()

    def RadioboxDataType(self):
        var = tk.StringVar(value="")

        tk.Radiobutton(self.frame, variable=var, value="INT", command=lambda:self.valor(var)).place(x = 0, y = 0)
        tk.Radiobutton(self.frame, variable=var, value="VARCHAR", command=lambda:self.valor(var)).place(x = 30, y = 0)
        tk.Radiobutton(self.frame, variable=var, value="DATA", command=lambda:self.valor(var)).place(x = 50, y = 0)
    
    def RadioboxAtribultos(self):
        var = tk.StringVar(value="")

        tk.Radiobutton(self.frame, variable=var, value="NULL", command=lambda:self.valor(var)).place(x = 0, y = 0)
        tk.Radiobutton(self.frame, variable=var, value="NOT NULL", command=lambda:self.valor(var)).place(x = 0, y = 0)

    def checkBox(self):
        self.unique = tk.StringVar()
        self.primaryKey = tk.StringVar()
        self.default = tk.StringVar()
        self.comment = tk.StringVar()
        self.unsigned = tk.StringVar()

        tk.Checkbutton(self.frame, variable=self.unique, onvalue="UNIQUE", command=lambda:self.getValor(1)).place(x = 0, y = 100)
        tk.Checkbutton(self.frame, variable=self.primaryKey, onvalue="PRIMARY KEY", command=lambda:self.getValor(2)).place(x = 20, y = 100)
        tk.Checkbutton(self.frame, variable=self.default, onvalue="DEFAULT", command=lambda:self.getValor(3)).place(x = 40, y = 100)
        tk.Checkbutton(self.frame, variable=self.comment, onvalue="COMMENT", command=lambda:self.getValor(4)).place(x = 55, y = 100)
        tk.Checkbutton(self.frame, variable=self.unsigned, onvalue="UNSIGNED", command=lambda:self.getValor(5)).place(x = 80, y = 100)

    def getValor(self, botao: int):
        query = ""
        match botao:
            case 1:
                query += self.unique.get()
            case 2:
                query += self.primaryKey.get()
            case 3:
                query += self.default.get()
            case 4:
                query += self.comment.get()
            case 5:
                query += self.unsigned.get()
            case 0:
                print("nada")
        print(query)
        return query
            

    def valor(self, var):
        print(var.get())

        
            
        




        