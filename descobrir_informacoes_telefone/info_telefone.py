"""
# Autor: Peterson Mendonça de Oliveira
"""

from phonenumbers import geocoder, carrier, timezone
import phonenumbers

def menu():
    print('*'*30)
    print('DETERMINADOR DE INFORMAÇÕES DE TELEFONE')
    print('0) Sair')
    print('1) Entre com o numero')
    print('*'*30)

while True:
    try:
        menu()
        escolha = int(input('Escolha uma opção: '))
        
        if escolha == 0:
            print('Obrigado por usar!!!')
            break
        
        elif escolha == 1:
            numero = input('Entre com o Numero de Telefone: ')
            number_phone = phonenumbers.parse(numero, 'pt-br')
            print('*'*30)
            print(f'Numero de Telefone: {numero}')
            local = geocoder.description_for_number(number_phone, 'pt-br')
            operadora = carrier.name_for_number(number_phone, 'pt-br')
            regiao = timezone.time_zones_for_number(number_phone)
            print(f'\n\tNumero: {numero}\n\tLocal: {local}\n\tOperadora: {operadora}\n\tRegião Geografica: {regiao}\n')
            
        else:
            print('Valor não aceito error!!!')
            
    except ValueError:
        print('Valor informado é invalido')
