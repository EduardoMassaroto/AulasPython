
# for loop nested
 # Outer loop (loop de fora)
  #Inner loop (loop de dentro do loop)


for numero1 in range(1,6):
      print('Produto' + str(numero1))
      for numero2 in range(1,6):
          print(numero1, numero2)
        

# Nested Loop em str
# Modificar de FANTASTICO para F A N T A S T I C O 

palavra = 'FANTASTICO'

for espaco in palavra:
    print(f' {espaco}', end='')

# Referente ao exemplo acima: o comando END serve para manter as letras na mesma linha, pois sem o comando END o programa cria em Vertical a palavra..
# O termo '' apos o uso do END= significa para voltar a palavra q estiver acima, q no caso do exemplo seria 'FANTASTICO'..
# Para adicionar o espaco entre as letras necessita Formatar a str ( utilizando f' {}' ) 
