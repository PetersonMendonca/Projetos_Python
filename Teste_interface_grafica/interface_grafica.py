from _typeshed import Self
import tkinter as tk
from tkinter import Entry, Frame
from tkinter import font

class Calculadora:
    def __init__(self, master):
        self.master = master
        
        self.janela_pricipal = Frame(self.master)
        self.janela_pricipal.pack()
        
        self.botoes = Frame(self.master)
        self.botoes.pack
        
        self.entrada = Entry(self.janela_pricipal, width=20, font=('Arial', 23))
        self.entrada.grid(row=0, column=0, columnspan=1)
        
        self.cria_botoes(self)
        
    def cria_botoes(self):
        self.botoes = [
            ["√", "x²", "**", "(", ")", "/"],
            ["sin", "cos" , "7", "8", "9", "+"],
            ["sin-¹", "cos-¹", "4", "5", "6", "-"],
            ["tan", "tan-¹", "1", "2", "3", "*"],
            ["n!", "π", ".", "0", "=", "ac"],   
        ]
        

root = tk.Tk()                              # Permite utilizar os widgets na aplicação
root.title('Calculadora Científica')        # Titulo acima da janela
root.minsize(345,500)                       # Tamanho minimo para a janela
# root.maxsize(345,500)                     # Tamanho maximo para a janela
root.geometry("345x500+800+250")            # Tamanho de inicialização da janela (larguraxaltura+x+y)
Calculadora(root)                           # Acionamento da classe
root.mainloop()                             # Exibição na tela do conteudo completo