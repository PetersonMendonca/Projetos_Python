import math
import mensagem

def limpar():
    resu = 0
    return resu

def soma(valor_1,valor_2=0,resu=0):
    if resu == 0:
        resu = valor_1 + valor_2
        return resu
    else:
        valor_temp = resu
        resu = valor_temp + valor_1
        return resu

def subtracao(valor_1,valor_2=0,resu=0):
    if resu == 0:
        resu = valor_1 - valor_2
        return resu
    else:
        valor_temp = resu
        resu = valor_temp - valor_1
        return resu

def multiplicacao(valor_1,valor_2=0,resu=0):
    if resu == 0:
        resu = valor_1 * valor_2
        return resu
    else:
        valor_temp = resu
        resu = valor_temp * valor_1
        return resu

def divisao(valor_1,valor_2=0,resu=0):
    if valor_1 == 0 or valor_2 == 0:
        mensagem.dividir_zero()
        resu = 0
        return resu
    else:
        if resu == 0:
            resu = valor_1 / valor_2
            return resu
        else:
            valor_temp = resu
            resu = valor_temp / valor_1
            return resu

def potenciacao(valor_1,valor_2=0,resu=0):
    if resu == 0:
        resu = valor_1 ** valor_2
        return resu
    else:
        valor_temp = resu
        resu = valor_temp ** valor_1
        return resu

def fatorial(valor_1, resu):
    if resu != 0:
        fat = 1
        i = 2
        while i <= resu:
            fat *= i
            i += 1
        return fat
    else:
        fat = 1
        i = 2
        while i <= valor_1:
            fat *= i
            i += 1
        return fat

def raiz_quadrada(valor_1, resu):
    if resu == 0:
        resu = valor_1 ** (1/2)
        return resu
    else:
        valor_temp = resu
        resu = valor_temp ** (1/2)
        return resu

def raiz_cubica(valor_1, resu):
    if resu == 0:
        resu = valor_1 ** (1/3)
        return resu
    else:
        valor_temp = resu
        resu = valor_temp ** (1/3)
        return resu
    
def coseno(valor_1, resu):
    if resu == 0:
        resu = math.cos(valor_1)
        return resu
    else:
        valor_temp = resu
        resu = math.cos(valor_temp)
        return resu

def seno(valor_1, resu):
    if resu == 0:
        resu = math.sin(valor_1)
        return resu
    else:
        valor_temp = resu
        resu = math.sin(valor_temp)
        return resu

def tangente(valor_1, resu):
    if resu == 0:
        resu = math.tan(valor_1)
        return resu
    else:
        valor_temp = resu
        resu = math.tan(valor_temp)
        return resu

def decisao(escolha,valor_1,valor_2=0,resu=0):
    if escolha == 0:
        return limpar()
    elif escolha == 1:
        return soma(valor_1,valor_2,resu)
    elif escolha == 2:
        return subtracao(valor_1,valor_2,resu)
    elif escolha == 3:
        return multiplicacao(valor_1,valor_2,resu)
    elif escolha == 4:
        return divisao(valor_1,valor_2,resu)
    elif escolha == 5:
        return potenciacao(valor_1,valor_2,resu)
    elif escolha == 6:
        return fatorial(valor_1, resu)
    elif escolha == 7:
        return raiz_quadrada(valor_1, resu)
    elif escolha == 8:
        return raiz_cubica(valor_1, resu)
    elif escolha == 9:
        return coseno(valor_1, resu)
    elif escolha == 10:
        return seno(valor_1, resu)
    elif escolha == 11:
        return tangente(valor_1, resu)