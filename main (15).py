
# criando lista

cidades = ['Ribeirao Preto, Sao Paulo, Bahia, Amazonia, Aparecida']

print(cidades)

# Quando for criar lista usar os [ ] 

# dentro da funcao lista existe varias funcoes, tais como :

#cidades.append('Santa Catarina') append serve para inserir um novo item

numeros = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c']

exibir = numeros + letras
print(exibir)

# o exemplo acima eu adicionei 2 listas, porem tem como fazer isso utilizando uma funcao, exemplo abaixo :

numeros = [2, 3, 5]
letras = ['c', 'b', 'a']

numeros.extend(letras)
print(numeros)

#For Looping dentro de uma lista, exemplo abaixo :

valores = [20, 40, 70, 100]

for x in valores:
    print(f' O valor final do produto é de R$ {x}.')

    #criando uma lista de cores para site onde o cliente pode consultar para saber se esta disponivel ou nao, exemplo abaixo:

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'azul', 'roxo', 'vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Fora de estoque')
    
#variavel + .lower() significa que o cliente pode digitar em letras MAIUSCULAS ou minusculas q nao ira dar erro na busca..


