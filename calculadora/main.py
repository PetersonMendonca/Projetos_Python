import funcoes
import mensagem

resultado = 0
valor_1 = 0
valor_2 = 0

while True:
    print(f'RESULTADO -> {resultado}')
    mensagem.bem_vindo()
    try:
        escolha_funcao = int(input('Escolha uma função: '))
        mensagem.divisao_texto()
        
        if escolha_funcao == 0:
            resultado = funcoes.decisao(escolha_funcao,valor_1,valor_2, resultado)
            
        elif escolha_funcao == 99:
            mensagem.agradecimento()
            break
        
        elif escolha_funcao >= 1 and escolha_funcao <= 5:
            valor_1 = float(input('Entre com o primeiro valor: '))
            if resultado == 0:
                valor_2 = float(input('Entre com o segundo valor: '))
            mensagem.divisao_texto()
            resultado = funcoes.decisao(escolha_funcao,valor_1,valor_2, resultado)
            
        elif escolha_funcao >=6 and escolha_funcao <= 11:
            valor_1 = float(input('Entre com o primeiro valor: '))
            mensagem.divisao_texto()
            resultado = funcoes.decisao(escolha_funcao,valor_1, resultado)
            
        else:
            mensagem.mensagem_erro()

    except:
        mensagem.mensagem_erro()