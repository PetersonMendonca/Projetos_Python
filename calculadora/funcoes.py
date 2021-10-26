import math

def limpar():
    resu = 0
    return resu

def soma(valor_1,valor_2,resu):
    if resu == 0:
        resu = valor_1 + valor_2
        return resu
    else:
        resu += valor_1
        return resu

def subtracao(valor_1,valor_2,resu):
    if resu == 0:
        resu = valor_1 - valor_2
        return resu
    else:
        resu -= valor_1
        return resu

def multiplicacao(valor_1,valor_2,resu):
    if resu == 0:
        resu = valor_1 * valor_2
        return resu
    else:
        resu = resu * valor_1
        return resu

def dividir(valor_1,valor_2,resu):
    if resu == 0:
        resu = valor_1 / valor_2
        return resu
    else:
        resu = resu / valor_1
        return resu

def potenciacao(valor_1,valor_2,resu):
    if resu == 0:
        resu = valor_1 ** valor_2
        return resu
    else:
        resu = resu ** valor_1
        return resu

def fatorial(valor_1, resu):
    if resu == 0:
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
        resu = valor_1 ** (1/2)
        return resu

def raiz_cubica(valor_1, resu):
    if resu == 0:
        resu = valor_1 ** (1/3)
        return resu
    else:
        resu = valor_1 ** (1/3)
        return resu
    
def coseno(valor_1, resu):
    if resu == 0:
        resu = math.cos(valor_1)
        return resu
    else:
        resu = math.cos(resu)
        return resu

def seno(valor_1, resu):
    if resu == 0:
        resu = math.sin(valor_1)
        return resu
    else:
        resu = math.sin(resu)
        return resu

def tangente(valor_1, resu):
    if resu == 0:
        resu = math.tan(valor_1)
        return resu
    else:
        resu = math.tan(resu)
        return resu

def decisao(escolha,valor_1,valor_2,resu):
    if escolha == 0:
        limpar()
    elif escolha == 1:
        pass
    else:
        pass




