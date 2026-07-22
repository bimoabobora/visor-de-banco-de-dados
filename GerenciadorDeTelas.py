import tkinter as tk
from tkinter import ttk

from DataBase import DataBase
from TelaDeEntrada import TelaDeEntrada, TelaDatabase
from TelaEscolhaDeTabelas import TelaEscolhaTabela, CriarTabelas
from TelaTabelas import TelaTabelas, AdicionarInfoTela, ExcluirInfo, AlterarInfo
import json

class GerenciadorDeTelas:
    def __init__(self):
        self.root = tk.Tk()
        
        if self.getDatabase():

            self.db = DataBase()
            
            self.telas= {
                "entrada": TelaDeEntrada(self.root, self, self.db),
                "dataBase": TelaDatabase(self.root, self),
                "escolhaDeTabelas": TelaEscolhaTabela(self.root, self, self.db),
                "tabelas": TelaTabelas(self.root, self, self.db),
                "telaAdicionarInfo": AdicionarInfoTela(self.root, self, self.db),
                "telaRemoverInfo": ExcluirInfo(self.root, self, self.db),
                "telaAlterarInfo": AlterarInfo(self.root, self, self.db),
                "criarTabelas": CriarTabelas(self.root, self, self.db)
        }
            self.Mainloop()

    def getDatabase(self):
        try:
            with open("config.json", "r"): 
                return True
        except:
            TelaDatabase(self.root, self).frame.tkraise()
            self.root.mainloop()
            

    def mostrarTela(self, nome: str):
        self.telas[nome].frame.tkraise()


    def Mainloop(self, nome = "entrada"):
        self.mostrarTela(nome)
        self.root.mainloop()

obj = GerenciadorDeTelas()

