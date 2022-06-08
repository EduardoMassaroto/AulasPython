# map function
# irei criar uma map para calcular o valor que os produtos deverao ser vendidos..

produtos = [40, 85, 135]

def multi(x):
    return x * 2

resultado = map(multi, produtos)

print(list(resultado))

# funcao LAMBDA para esse mesmo codigo segue o exemplo abaixo :

produtos = [40, 85, 135]

print(list(map(lambda x: x * 2, produtos)))

# essa funcao lambda serve para economizar linhas no codigo, porem eh uma funcao sem nome

# FILTER FUNCTION  
# serve para filtrar itens, exemplo abaixo usando a funcao lambda para simplificar o codigo  

valores = [10, 12, 15, 40, 50]

print(list(filter(lambda x: x < 30, valores ))) 

# criando for looping dentro de uma lista adicionando os itens dentro da list1 com a letra x, na list 2.. funcao LIST COMPREHENSION AULA 69

frutas1= ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

frutas2 = [iten for iten in frutas1 if 'k' in iten]
print(frutas2)

# nesse exemplo pedi para adicionar na lista2 (frutas2) todas as frutas com a letra K q estao na lista 1 (frutas1)

# list comprehension com numeros exemplo abaixo :

valores = []

for x in range(6):
    valores.append(x * 10)

print(valores)

# exemplo acima seria o codigo sem a list comprehension... abaixo segue o exemplo do mesmo codigo porem utilizando essa funcao   

valores = [x * 10 for x in range(6)]
print(valores)


#utilizar o GENERATOR EXPRESSION sempre q for gerar varios numeros, pois ele ocupa apenas 112kb de memoria (independente do valor), enquanto a lista sempre ira consumir mais.. exemplo abaixo

# a funcao type() serve para mostrar a classe da funcao 

# para mudar de lista [] para generator () basta mudar o sinal da funcao, exemplos abaixo, o generator sempre ocupara 112kb de memoria (sempre usar esse formato para programas onde irei gerar muitos numeros)

from sys import getsizeof 

# essa funcao acima serve para mostrar o tamanho em KB do comando em q eu chama-la 


numeros = [x * 10 for x in range(10)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

# exemplo abaixo convertendo um comando em lista para generator para usar menas memoria 

numeros = (x * 10 for x in range(10))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))

# converti o comando generator para ser mostrado como se fosse uma lista ( usando a funcao LIST para mostrar o generator como lista)


