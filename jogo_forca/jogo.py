import random
import metodos

def seleciona_palavra():
    fruta = ['banana', 'amora', 'abacaxi', 'framboesa', 'acerola', 'Abacate ', 'açaí ', 'Carambola', 'Cereja', 'Goiaba']
    carro = ['civic', 'opala', 'vectra', 'doge', 'fusca', 'focus', 'fusion', 'gol', 'uno', 'captiva', 'ranger']
    pais = ['Brasil', 'belgica', 'alemanha', 'japão', 'frança', 'america', 'australia', 'mexico', 'russia']

    metodos.apresentacao()
    
    palavra_secreta = ''
    palavra_secreta_temporaria = ''
    repetir = True
    usadas = []
    todas_letras_usadas = []
    erro = 6
    
    try:
        escolha = int(input('\n1) Fruta\n2) carro\n3) pais\nEntre com uma opção: '))
        print('*'*27)
        
        if escolha == 1:
            gerador = random.randint(0, len(fruta)-1)
            palavra_secreta = fruta[gerador]
            palavra_secreta_temporaria = '_' * len(palavra_secreta)
        elif escolha == 2:
            gerador = random.randint(0, len(carro)-1)
            palavra_secreta = carro[gerador]
            palavra_secreta_temporaria = '_' * len(palavra_secreta)
        elif escolha == 3:
            gerador = random.randint(0, len(pais)-1)
            palavra_secreta = pais[gerador]
            palavra_secreta_temporaria = '_' * len(palavra_secreta)
        else:
            print('Entre com valor valido !!!')
            repetir = False
        
        print(f'Palavra secreta -> {palavra_secreta}')    

        while repetir:
            if palavra_secreta_temporaria == palavra_secreta:
                metodos.ganhou()
                break
                
            apresenta_letras = [x for x in todas_letras_usadas]
            print(f'\nVocê tem {erro} tentativas restantes')
            print(f'Letras Usadas até o momento: {apresenta_letras}')
            print('*'*30)
            print(f'\nPalavra secreta -> {palavra_secreta_temporaria}')
            letra_escolhida = input('Entre com 1 letra da sua escolha: ')
            print('*'*30)
            
            if letra_escolhida not in todas_letras_usadas:
                todas_letras_usadas.append(letra_escolhida)
                usadas.append(letra_escolhida)
                
                if len(letra_escolhida) > 1:
                    usadas.pop()
                    todas_letras_usadas.pop()
                    print("\nErro, Isso não vale, entre apenas com uma letra !!!")
                    print('*'*30)
                    
                elif letra_escolhida in palavra_secreta:
                    palavra_secreta_temporaria = ''
                    for letra in palavra_secreta:
                        if letra in usadas:
                            palavra_secreta_temporaria += letra
                        else:
                            palavra_secreta_temporaria += '_'
                        
                else:
                    erro -= 1
                    usadas.pop()
                    metodos.errou(erro)
                    
                    if erro <= 0:
                        metodos.perdeu()
                        break
            else:
                print('Letra Já usada, entre co outra letra !!!')
                print('*'*30)
                
    except ValueError:
        print('Entre com um dos valores validos')
                    
seleciona_palavra()