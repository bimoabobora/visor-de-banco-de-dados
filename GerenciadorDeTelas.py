import tkinter as tk
from tkinter import ttk

from DataBase import DataBase
from TelaDeEntrada import TelaDeEntrada
from TelaEscolhaDeTabelas import TelaEscolhaTabela, CriarTabelas
from TelaTabelas import TelaTabelas, AdicionarInfoTela, ExcluirInfo, AlterarInfo


class GerenciadorDeTelas:
    def __init__(self):
        self.root = tk.Tk()
        self.db = DataBase()
        self.telas= {
            "entrada": TelaDeEntrada(self.root, self, self.db),
            "escolhaDeTabelas": TelaEscolhaTabela(self.root, self, self.db),
            "tabelas": TelaTabelas(self.root, self, self.db),
            "telaAdicionarInfo": AdicionarInfoTela(self.root, self, self.db),
            "telaRemoverInfo": ExcluirInfo(self.root, self, self.db),
            "telaAlterarInfo": AlterarInfo(self.root, self, self.db),
            "criarTabelas": CriarTabelas(self.root, self, self.db)
        }

    def mostrarTela(self, nome: str):
        self.telas[nome].frame.tkraise()


    def Mainloop(self, nome = "entrada"):
        self.mostrarTela(nome)
        self.root.mainloop()

obj = GerenciadorDeTelas()
obj.Mainloop(nome = "criarTabelas")