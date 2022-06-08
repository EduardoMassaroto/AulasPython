
# For loops (looping)
#vou imprimir de 0 a 100
#vou chamar minha variavel de numero

for numero in range(101):
    print(numero)

#obs: adicionei 101 pois o phyton numera em index ou seja o 0 conta como um numero

#caso eu nao queira que comece pelo 0, tenho q especificar na range os numero q quero q aparecem, exemplo:

for numero in range(1, 101):
    print(numero)

#obs: mas mesmo assim necessito acrescentar um numero a mais por conta de sempre comecar no 0.. porem o 101 nao sera mostrado, apenas do 1 ao 100..

#com a range tambem da para utilizar o STEP (escolher quantos numeros quero q pule) o STEP sera sempre o ultimo numero apos a ultima virgula, exemplo :

for numero in range(0, 10, 2):
    print(numero)

#FOR LOOPS PARA STR (TEXTO)
for letra in 'Google':
    print(letra)

#FOR LOOPS PARA STR especificando onde esta a letra.. exemplo :

palavra = 'Google'

for letra in palavra:
    print(f'{letra} esta dentro da palavra Google')

#obs: adicionei uma variavel (palavra) e formatei a str usando o F' e referi a qual variavel eu queria formatar q no caso foi a {letra} .. obs usar os{ } para especificar oq quer formatar.

#irei formatar a variavel palavra e a variavel letra, exemplo :

palavra = 'Jogos'

for letra in palavra:
    print(f'{letra} Esta dentro da palavra {palavra}')
