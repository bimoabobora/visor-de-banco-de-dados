from TelaBase import TelaBase, tk, ttk

class TelaTabelas(TelaBase):
    xColuna = 0.00
    def __init__(self, root: tk, gerenciador, db):
        super().__init__(root)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        
        self.gerenciador = gerenciador
        self.tabela = None
        self.db = db
        
        if self.tabela == None:
            pass
        else:
            self.Interface()

    

    def botoes(self):
        tk.Button(self.frame, text="voltar", command=lambda: self.voltar(self.gerenciador)).place(relx=0.94, rely=0.86)
        tk.Button(self.frame, text="Adicionar Informações", command=lambda: self.adicionarInfo(self.gerenciador)).place(relx=0.91, rely=0.83)
        tk.Button(self.frame, text="Excluir Informações", command=lambda: self.ExcluirInfo(self.gerenciador)).place(relx=0.92, rely=0.80)
        tk.Button(self.frame, text="Alterar Informações", command=lambda: self.AlterarInfo(self.gerenciador)).place(relx=0.92, rely=0.77)
        
        
    def Interface(self):
        self.botoes()
        self.showColunas()
        self.showInfo()

    def ColunasInfo(self):
        colunas = self.db.getColunas(self.tabela, comId= True)
        info = self.db.getInfo(self.tabela)
        return colunas, info

    def showColunas(self):
        colunas = self.ColunasInfo()
        for nome in colunas[0]:
            tk.Label(self.frame, text=nome).place(relx=self.xColuna,rely=0.00)
            self.xColuna += 0.05
        self.xColuna = 0

    def showInfo(self):
        info = self.ColunasInfo()[1]
        i = 0
        j = 0
        x = 0.0
        y = 0.05
        if info == False:
            tk.Label(self.frame, text="Sem informações").place(relx=0.0, rely=0.05)
            return
        while i <= len(info) - 1:
            tk.Label(self.frame, text=info[i][j]).place(relx=x, rely=y)
            j += 1
            x += 0.05
            if j == len(info[i]):
                i += 1
                y += 0.05
                j = 0
                x = 0

    def adicionarInfo(self, gerenciador):
        gerenciador.telas["telaAdicionarInfo"].getTabela()
        gerenciador.telas["telaAdicionarInfo"].atualizar()
        gerenciador.mostrarTela("telaAdicionarInfo")

    def ExcluirInfo(self, gerenciador):
        gerenciador.telas["telaRemoverInfo"].getTabela()
        gerenciador.telas["telaRemoverInfo"].atualizar()
        gerenciador.mostrarTela("telaRemoverInfo")
    
    def AlterarInfo(self, gerenciador):
        gerenciador.telas["telaAlterarInfo"].getTabela()
        gerenciador.telas["telaAlterarInfo"].atualizar()
        gerenciador.mostrarTela("telaAlterarInfo")

    def voltar(self,gerenciador):
        gerenciador.mostrarTela("escolhaDeTabelas")
        
    def atualizar(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.Interface()
        
       

    def setTabela(self, tabela): 
        self.tabela = tabela
        self.atualizar()

class AdicionarInfoTela(TelaBase):
    
    def __init__(self, root: tk, gerenciador:tk, db):
        super().__init__(root)
        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.gerenciador = gerenciador
        self.db = db
        self.tabela = None
        self.listaDeObjetos = []

       
        if self.tabela == None:
            pass
        else:
            self.Interface()

    
    def getTabela(self):
        self.tabela = self.gerenciador.telas["tabelas"].tabela
        
    def Interface(self):
        self.botoes()
        self.showColunas()
        self.Labels()

    def botoes(self):
        botao = tk.Button(self.frame, text="inserir dados", command=lambda: self.db.AdicionarInfo(self.getTextoDosLabels(), self.tabela, self.db.getColunas(self.tabela, comId=False)))
        botao.place(relx= 0.9, rely = 0.85)

        botao = tk.Button(self.frame, text="Voltar", command=lambda: self.voltar(self.gerenciador))
        botao.place(relx = 0.9 , rely=0.88)

    def atualizar(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.Interface()

    def voltar(self, gerenciador):
        self.listaDeObjetos = []
        gerenciador.telas["tabelas"].atualizar()
        gerenciador.mostrarTela("tabelas")

    def showColunas(self):
        yColuna = 0.00
        colunas = self.db.getColunas(self.tabela, comId=False)     
        for coluna in colunas:
            tk.Label(self.frame, text=coluna).place(relx=0.00,rely=yColuna)
            yColuna += 0.05
    
    def Labels(self):
        x,y = 0.05, 0.00
        colunas = self.db.getColunas(self.tabela, comId=False)
        for _ in colunas:
            dados = tk.Entry(self.frame)
            dados.place(relx = x, rely=y)
            y += 0.05
            self.listaDeObjetos.append(dados)
        return self.listaDeObjetos
    
    def getTextoDosLabels(self):
        lista = []
        for obj in self.listaDeObjetos:
            resultado = obj.get()
            lista.append(resultado)
        return lista

   
class ExcluirInfo(AdicionarInfoTela):
    def __init__(self, root, gerenciador, db):
        super().__init__(root, gerenciador, db)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)


    def botoes(self):
        botao = tk.Button(self.frame, text="Excluir dados", command=lambda: self.Excluir())
        botao.place(relx=0.9, rely=0.82)

        botao = tk.Button(self.frame, text="Pesquisar", command=lambda: self.mostrarInfo())
        botao.place(relx=0.9, rely=0.85)

        botao = tk.Button(self.frame, text="Voltar", command=lambda: self.voltar(self.gerenciador))
        botao.place(relx=0.9, rely=0.88)
        
    def Labels(self):
    
        condicao = tk.Entry(self.frame)
        condicao.place(x = 80, y = 0)

        valor = tk.Entry(self.frame)
        valor.place(x = 50 , y = 25)

        self.listaDeObjetos.append(condicao)
        self.listaDeObjetos.append(valor)
        return self.listaDeObjetos
        
    def getTextoDosLabels(self):
        lista = []
        for obj in self.listaDeObjetos:
            resultado = obj.get()
            lista.append(resultado)
        return lista        
    
    def showColunas(self):
        tk.Label(self.frame, text="Identificador").place(x = 0, y = 0)
        tk.Label(self.frame, text="Valor").place(x = 0 , y= 25)

    def Excluir(self):
        info = self.getTextoDosLabels()
        self.db.ExcluirInfo(self.tabela, info[0], int(info[1]))

    def mostrarInfo(self):
        x = 250
        info = self.getTextoDosLabels()
        retorno = self.db.MostrarInfo(self.tabela, info[0], int(info[1]))
        tk.Label(self.frame, text="Resultado da pesquisa:").place(x = 100, y = 200)
        for informacao in retorno[0]:
            tk.Label(self.frame, text=informacao).place(x = x, y = 200)
            x += 20

class AlterarInfo(ExcluirInfo):
    def __init__(self, root, gerenciador, db):
        super().__init__(root, gerenciador, db)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def botoes(self):
        botao = tk.Button(self.frame, text="Alterar dados", command=lambda: self.Alterar())
        botao.place(relx=0.9, rely=0.82)

        botao = tk.Button(self.frame, text="Pesquisar", command=lambda: self.mostrarInfo())
        botao.place(relx=0.9, rely=0.85)

        botao = tk.Button(self.frame, text="Voltar", command=lambda: self.voltar(self.gerenciador))
        botao.place(relx=0.9, rely=0.88)
    
    def showColunas(self):
        tk.Label(self.frame, text="Identificador").place(x = 0, y = 0)
        tk.Label(self.frame, text="Valor do identificador").place(x = 0 , y= 25)
        tk.Label(self.frame, text="Coluna de alteração").place(x = 0 , y= 50)
        tk.Label(self.frame, text="Valor da coluna de alteração").place(x = 0 , y= 75)


    def Labels(self):
        
        colunaIdentificador = tk.Entry(self.frame)
        colunaIdentificador.place(x = 160, y = 0)

        valorIdentificador = tk.Entry(self.frame)
        valorIdentificador.place(x = 160 , y = 25)

        alternaColuna = tk.Entry(self.frame)
        alternaColuna.place(x = 160 , y = 50)

        alternaValor = tk.Entry(self.frame)
        alternaValor.place(x = 160 , y = 75)

        self.listaDeObjetos = [colunaIdentificador, valorIdentificador, alternaColuna, alternaValor]
        return self.listaDeObjetos

    def Alterar(self):
        info = self.getTextoDosLabels()
        self.db.AlterarInfo(self.tabela, info[0], info[1], info[2], info[3])

        
