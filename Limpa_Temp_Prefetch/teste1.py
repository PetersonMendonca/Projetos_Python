"""
    Realiza o procedimento de limpeza das pastas Prefetch e Temp do Windows
"""

import os
import shutil

caminho_temp = 'C:\\Windows\\Temp'
caminho_prefetch = 'C:\\Windows\\Prefetch'

# Exclui arquivos da temp e Prefetch do windows
def exclui_temporarios(nome_pasta_temp):
    for caminho, pastas, arquivos in os.walk(nome_pasta_temp):
        for arquivo in arquivos:
            try:
                caminho_arquivo = caminho + '\\' + arquivo
                os.remove(caminho_arquivo)
            except:
                continue
        for pasta in pastas:
            try:
                caminho_arquivo = caminho + '\\' + pasta
                shutil.rmtree(caminho_arquivo)
            except:
                continue

def verifica_windows():
    verifica_ativacao = os.system('slmgr /xpr')
    if verifica_ativacao == 0:
        print(f'O Windows está Ativado')
    else:
        print(f'O Windows não está Ativado')

if __name__ == '__main__':
    exclui_temporarios(caminho_temp)
    exclui_temporarios(caminho_prefetch)
    print('Pastas e Arquivos temporarios excluidos!!!')
    verifica_windows()
    
    vari = input('Apeter "ENTER" para fechar:')
    print('Obrigado por usar!!!')