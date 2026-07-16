from TelaDeEntrada import TelaDeEntrada
from TelaTabelas import TelaTabelas, AdicionarInfoTela
from DataBase import DataBase
import tkinter as tk
from tkinter import ttk

db = DataBase()

'''info = db.getInfo("testes")
db.AdicionarInfo(["Roberto1"], "testes", ["nome"])
print(info)'''

def test(*teste):
    string = ""
    for char in teste:
        string += char
        string += "\n"
    print(string)

colum1 = "id INT AUTO_INCRIMENT PRIMARY KEY"
colum2 = "nome VARCHAR(255)"
test(colum1, colum2)
