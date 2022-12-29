def apresentacao():
    print('*'*30)
    print('BEM VINDO AO JOGO DE FORCA')
    print('*'*30)
    
def perdeu():
    print('*'*30)
    print('Infelizmente acabou suas tentativas :(')
    print('FIM DE JOGO !!!')
    print('*'*30)
    print()
    
def ganhou():
    print('PARABENS VOCÊ GANHOU !!!')
    print("  ___________ ")
    print(" '._==_==_=_.' ")
    print(" .-\:      /-. ")
    print("| (|:.     |) | ")
    print(" '-|:.     |-' ")
    print("   \::.    / ")
    print("    '::. .' ")
    print("      ) ( ")
    print("    _.' '._ ")
    print('   `"""""""` ')
    print('OBRIGADO POR JOGAR !!!\n')
    print('*'*30)

def errou(erro):
    print()
    print('VOCÊ ERROU')
    print('_____________')
    print('|           |')
    
    if erro == 6:
        print('|           |')
        print('|          ( )')
    elif erro == 5:
        print('|           |')
        print('|          ( )')
        print('|           |')
    elif erro == 4:
        print('|           |')
        print('|          ( )')
        print('|          \|')
    elif erro == 3:
        print('|           |')
        print('|          ( )')
        print('|          \|/')
    elif erro == 2:
        print('|           |')
        print('|          ( )')
        print('|          \|/')
        print('|           |')
    elif erro == 1:
        print('|           |')
        print('|          ( )')
        print('|          \|/')
        print('|           | ')
        print('|          / ')
    elif erro == 0:
        print('|           |')
        print('|          ( )')
        print('|          \|/')
        print('|           | ')
        print('|          / \ ')
        print('|')
        print('|________________')