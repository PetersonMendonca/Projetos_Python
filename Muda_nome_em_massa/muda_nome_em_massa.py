import os
import shutil
from ast import walk

caminho_arquivos = r'C:\Users\petri\OneDrive\Área de Trabalho\Musica_Pendrive'
caminho_novo = r'C:\Users\petri\OneDrive\Área de Trabalho\Musica_Pendrive_Final'

for root, dir, files in os.walk(caminho_arquivos):
    for file in files:
        print('Antes: ',file)
        
        valor = file.replace('00 - ', '').replace('00  - ', '').replace('00 -  ', '').replace('00 -- ', '').replace('00 – ', '')
        
        old_file_path = os.path.join(caminho_arquivos,file)
        new_file_path = os.path.join(caminho_novo, valor)
        
        shutil.copy(old_file_path, new_file_path)
        
        print('Depois: ',valor)
