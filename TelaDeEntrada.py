from TelaBase import TelaBase, tk, ttk
import json


class TelaDatabase(TelaBase):
    def __init__(self, root, gerenciador):
        super().__init__(root)

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.gerenciador = gerenciador
        

        tk.Button(self.frame, text="Conectar a Database", command=lambda: self.getEntrys()).place(relx = 0.45, y = 600)
        tk.Button(self.frame, text="voltar", command=lambda: self.voltar()).place(relx = 0.9, rely = 0.88)
        self.Entrys()
        self.Labels()

    def voltar(self):
       self.gerenciador.mostrarTela("escolhaDeTabelas")

    def Configs(self):
       try:
        with open("config.json", "r"):
            return True
       except:
          return False

    def Labels(self):
       tk.Label(self.frame, text="Host").place(relx = 0.45, y=70)
       tk.Label(self.frame, text="Usuario").place(relx = 0.45, y=170)
       tk.Label(self.frame, text="Senha").place(relx = 0.45, y=270)
       tk.Label(self.frame, text="Banco de dado").place(relx = 0.45, y=370)

    def Entrys(self):
       self.host = tk.Entry(self.frame)
       self.user = tk.Entry(self.frame)
       self.password = tk.Entry(self.frame)
       self.database = tk.Entry(self.frame)

       self.host.place(relx  = 0.45, y = 100)
       self.user.place(relx = 0.45, y = 200)
       self.password.place(relx =0.45, y = 300)
       self.database.place(relx = 0.45, y = 400)

    def getEntrys(self):
       config = {
          "host": self.host.get(),
          "user": self.user.get(),
          "password": self.password.get(),
          "database": self.database.get()
       }
       with open("config.json", "w") as f:
          json.dump(config, f, indent=4)
          

       if self.Configs():
          self.gerenciador.db.database()
          self.root.destroy()
          self.gerenciador.__init__()
       else:
        self.root.destroy()
        self.gerenciador.__init__()
          
          