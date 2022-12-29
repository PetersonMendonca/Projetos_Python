"""
INFORMAÇÕES TKINTER

Container – É uma analogia a um container físico e tem como objetivo organizar e 
guardar objetos. Da mesma forma este conceito serve para um container em interface.
Nesse caso, os objetos que estamos armazenando são os widgets;

Widget – É um componente qualquer na tela, que pode ser um botão, um ícone,
uma caixa de texto, etc.;

Event Handler – São tratadores de eventos. Por exemplo, ao clicarmos
em um botão para executar uma ação, uma rotina é executada. 
Essa rotina é chamada de event handler;

Event Loop – O event loop verifica constantemente se outro evento foi acionado.
Caso a hipótese seja verdadeira, ele irá executar a rotina correspondente.


O módulo Tkinter oferece três formas de trabalharmos
com geometria e posicionamento:

 - Pack;
 - Grid;
 - Place.
 
Vamos ver algumas configurações de estilo mais comuns que podemos definir:

 Width – Largura do widget;
 Height – Altura do widget;
 Text – Texto a ser exibido no widget;
 Font – Família da fonte do texto;
 Fg – Cor do texto do widget;
 Bg – Cor de fundo do widget;
 Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).

"""

# EXEMPLO 1

from tkinter import *

class Application:
    def __init__(self, master=None):
        
    # Frame principal
        self.widget1 = Frame(master)
        self.widget1.pack()
        
        # Fonte padrão utilizada, que sera utilizada nos textos das caixas
        self.fontePadrao = ('Arial', '10')
        
    # Containers
        # Definindo o container 1
        self.primeiroContainer = Frame(master)
        # Definindo area do container
        self.primeiroContainer['pady'] = 10
        # Exibe container na tela
        self.primeiroContainer.pack()

        # Definindo o container 2
        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer.pack()
        
        # Definindo o container 3
        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer.pack()
        
        # Definindo o container 4
        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 20
        self.quartoContainer.pack()
        
        # Label - Label texto não editavel que sera exibido
        # Label Titulo
        self.titulo = Label(self.primeiroContainer, text='Dados do Usuario')
        # Fonte do titulo
        self.titulo['font'] = ('Arial', '10', 'bold')
        # Exibir o titulo
        self.titulo.pack()
        
        # Label Nome, não alteravel
        self.nomeLabel = Label(self.segundoContainer, text='Nome', font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        # Cria e Manipulação da caixa de texto a frente do label nome
        self.nome = Entry(self.segundoContainer)
        # Determina a largura da caixa de texto
        self.nome['width'] = 30
        # Ira utilizar da fonte padão criada acima
        self.nome['font'] = self.fontePadrao
        # apresenta na tela e manda para a esquerda
        self.nome.pack(side=LEFT)
        
        # Label Nome, não alteravel
        self.senhaLabel = Label(self.terceiroContainer, text='Senha', font=self.fontePadrao )
        self.senhaLabel.pack(side=LEFT)
        
        # Cria e Manipulação da caixa de texto a frente do label senha
        self.senha = Entry(self.terceiroContainer)
        # Largura da caixa de texto
        self.senha['width'] = 30
        # Fonte do texto da caixa de texto
        self.senha['font'] = self.fontePadrao
        # Mostra os caracter * no lugar da senha digitada
        self.senha['show'] = '*'
        # apresenta na tela e manda para a esquerda
        self.senha.pack(side=LEFT)
        
        # Campo onde trara a resposta se foi logado ou não
        self.msg = Label(self.quartoContainer, text='', font=self.fontePadrao)
        self.msg.pack(side=TOP)        

        # Criação e configuração do botão autenticar
        self.autenticar = Button(self.quartoContainer)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Calibri', '8')
        self.autenticar['width'] = 12
        # faz botão acionar a função de autenticação
        self.autenticar['command'] = self.verificaSenha
        self.autenticar.pack(side=LEFT)
        
        # Criar botão de sair
        self.sair = Button(self.quartoContainer)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Calibri', '8')
        self.sair['width'] = 12
        self.sair['command'] = self.widget1.quit
        self.sair.pack(side=LEFT)
        
    # Metodo que verifica Usuario e Senha
    def verificaSenha(self):
        # pega valores da caixa de texto e guarda em uma variavel
        usuario = self.nome.get()
        senha = self.senha.get()
        
        if usuario == 'admin' and senha == 'admin':
            self.msg['text'] = 'Autenticado'
        else:
            self.msg['text'] = 'Erro na autenticação'
        
        
# Permite utilizar os widgets na aplicação
root = Tk()
# Passa a variavel root como parametro
Application(root)
# mainloop é o metodo que permite exibir na tela
root.mainloop()

'''
Label(root, text='texto', bg='red').grid(column=0)
Label(root, text='texto', bg='green').grid(column=1)
# determina quantas colunas quer que o widget ocupe
# sticky tira as falhinhas dos cantos 'w' esquerda e 'e' de direita, 'we' dos dois
Label(root, text='texto', bg='blue').grid(columnspan=2, sticky='we') 
'''