import funcoes
import mensagem

resultado = 0
valor_1 = 0
valor_2 = 0

while True:
    mensagem.bem_vindo()
    try:
        escolha_funcao = int(input('Escolha uma função: '))
        
        valor_1 = float(input('Entre com o primeiro valor: '))
        valor_2 = float(input('Entre com o segundo valor: '))
        
        funcoes.decisao(escolha_funcao,valor_1,valor_2, resultado)
    except:
        mensagem.mensagem_erro()