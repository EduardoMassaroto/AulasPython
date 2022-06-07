
# sem o operador ternario

idade = 10
if idade >= 16:
    resultado = print('Voto permitido')
else:
    resultado = print('Voto nao permitido')

# usando o operador ternario

resultado = 'Voto permitido' if idade >= 16 else 'Voto nao permitido'
 
print(resultado)

# multiplos operadores de comparacao
# estabelecendo valor minimo e maximo para produtos
#exemplo simplificado
valor = 20

if 20 <= valor < 40:
 print('Produto aceito')
else:
 print('Produto nao aceito')


#exemplo sem simplificar

valor = 45

if valor >= 20 and valor < 40:
 print('Produto aceito')
else: 
 print('Produto nao aceito')


