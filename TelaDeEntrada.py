from TelaBase import TelaBase, tk, ttk


class TelaDeEntrada(TelaBase):
    
    def __init__(self,root, gerenciador, db):
        super().__init__(root)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.frame, text="Usuario").place(
            relx=0.46,
            rely=0.20
        )
        
        tk.Label(self.frame, text="Senha").place(
            relx=0.46,
            rely=0.5
        )

        dadosNome = tk.Entry(self.frame,width=50)
        dadosNome.place(
            relx=0.38,
            rely=0.24
        )

        dadosSenha = tk.Entry(self.frame,width=50)
        dadosSenha.place(
            relx=0.38,
            rely=0.54
        )
            
        botao = tk.Button(self.frame, text="confirmar", command=lambda: self.test(gerenciador), width=30)
        botao.place(
            relx=0.40,
            rely=0.65
        )
    
     
    def test(self, gerenciador):
            gerenciador.mostrarTela("escolhaDeTabelas")

        
                

