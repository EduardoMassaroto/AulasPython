
# no exemplo abaixo irei pedir para imprimir o index 3 q no caso nao existe na lista..

try:
 letras = ['a', 'b', 'c']
 print(letras[3])
except IndexError:
    print('Index nao existe')

# no exemplo acima a funcao try referese a tentar executar essa funcao, caso der erro (no nosso exemplo o erro que estava dando era IndexError), eu converti esse erro, para um print de uma frase onde o usuario nao se assuste, apenas seja informado.. e para converter o erro em uma msg usa o comando EXCEPT + NOME DO ERRO   ..
''''
# no exemplo abaixo irei usar o try e except com o input

try:
 valor = int(input('Digite o valor do seu produto: '))
 print(valor)
except ValueError:
    print('Insira apenas numeros')

# acima convertir o input para uma int pois irei trabalhar com numeros e calculos, sem o int esse input seria uma stry

'''
# o codigo acima esta desativado ( usando ''') para reativar basta apagar os '''

# utilizando else e finally :

try:
 valor = int(input('Digite o valor do seu produto: '))
 print(valor)
except ValueError:
    print('Insira apenas numeros')
else:
    resultado = valor + 10
    print(resultado)
finally:
    print('codigo ok')

# a funcao finally serve para executar o codigo abaixo do erro, mesmo se aparecer o erro..

