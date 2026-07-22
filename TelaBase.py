import tkinter as tk
from tkinter import ttk

class TelaBase:
    def __init__(self, root):
        self.root = root
        self.tamanhoJanela = "1600x900"
        root.geometry(self.tamanhoJanela)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)



  