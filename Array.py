
# agregando duas listas com a funcao ZIP

cores = ['amarelo', 'verde', 'preto']
valores = [20, 30, 40]
duas_listas = zip(cores, valores)

print(list(duas_listas))

# Criando lista com input :

frutas_usuario = input ('Digite os nomes das frutas separadas por virgulas: ')

frutas_lista = frutas_usuario.split(', ')
# funcao split serve para o programa identificar onde tem q separar os itens das listas, no caso do exemplo pedi para q separe apos a (virgula) q o usuario acrescentar na hora de montar a lista de frutas..

print(frutas_lista)

#Criando set (listas)
 #similar a listas
 #evita itens duplicados
 #N utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)
# a funcao | retira os numeros duplicados, inserindo apenas 1 ao invez de inserir os 2 valores iguais
print(num1 - num2)
# a funcao acima retira os numeros iguais, e mostra somente os q nao se repetem na list2 ( no caso sera o 30, 40, 50)
print(num1 ^ num2)  
#mostra todos os numeros q n se repetem
print(num1 & num2)  
# mostra somente os numeros repetidos

