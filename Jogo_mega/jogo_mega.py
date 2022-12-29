import random

# GERA JOGOS
def gera_numeros(tipo_jogo):
    gerados = []
    
    while(len(gerados) != tipo_jogo):
        numero = random.randint(1,60)
        
        if numero not in gerados:
            gerados.append(numero)
            
    gerados.sort()  
    return f'JOGO GERADO -> {gerados}'

mensagem_erro = 'Valor não aceito, entre com valor valido !!!'

while True:
    try:
        print('\nMENU DE JOGOS\n\t1) MEGA-SENA\n\t2) QUINA\n\t3) QUADRA\n\t0) SAIR')
        escolha_jogo = int(input('Escolha uma opção: '))
        
        if escolha_jogo == 0:
            print('Obrigado por usar o gerador !!!')
            break
        elif escolha_jogo < 0 or escolha_jogo > 3:
            print(mensagem_erro)
        else:
            qtd_jogos = int(input('Entre com a quantidade de jogos: '))
            print()
            
            for i in range(qtd_jogos):
                if escolha_jogo == 1:
                    print(gera_numeros(6))
                elif escolha_jogo == 2:
                    print(gera_numeros(5))
                elif escolha_jogo == 3:
                    print(gera_numeros(4))
    except ValueError:
        print(mensagem_erro)
