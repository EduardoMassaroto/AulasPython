
# Funcoes
 #DRY - Dont repeat yourself
 #varios argumentos (xargs)

#criar uma funcao que soma varios numeros
#quando eu n sei quantos numeros quero somar, acrescento o * na frente do argumento..

def soma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

x= soma(5,10,2,5,10,3)

print(x)

# criando varios argumentos (xargs) identificando o parametro.

#criar uma funcao q armazena numeros e strings (dados) 

# acrescentar dois * na frente do argumento, significa q eu n sei quantos parametros irei ter na minha variavel, exemplo abaixo :

def agencia(**carro):
    return carro

print(agencia(marca= 'Gol', cor= 'Branca'))
print(agencia(marca= 'Gol', cor= 'Branca', placa= '291021'))

# chamando a funcao eu posso acrescentar quantos argumentos ou parametros eu quiser..

import math
print(math.factorial(4)) 

print(math.floor(5.5))

# import math tem varias funcoes, para saber qual funcao quero utilizar basta entrar no google e pesquisar sobre as funcoes de math... 

# (acima tem o exemplo fatorial e o exemplo floor q significa o menor numero inteiro do numero q eu digitar)
    