import tkinter as tk
from tkinter import ttk
from TelaBase import TelaBase

root = tk.Tk()

class AdicionarInfoTela(TelaBase):

    tamanhoJanela = "683x384"

    def __init__(self, root, tabela, colunas):
        super().__init__(root)
        
        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.colunas = colunas
        self.tabelas = tabela

        tk.Button(self.frame, command=lambda: self.test(lista)).place(relx=0.34,rely=0.22)
        x = 0.38
        y = 0.24
        lista = []
        for i in range(3):
            self.dadosNome = tk.Entry(self.frame,width=50)
            self.dadosNome.place(
                relx=x,
                rely=y
            )
            lista.append(self.dadosNome)
            y += 0.05

    def test(self, lista):
        for dados in lista:
            print(dados.get())

       

obj = AdicionarInfoTela(root, "testes", ["nome", "id"])
obj.root.mainloop()
   

