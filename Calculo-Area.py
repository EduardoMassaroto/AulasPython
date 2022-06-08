# criar um programa para calcular quanta tinta irei usar para pintar uma parede  

Rend = int(input('Qual o rendimento da lata ?'))
Altura = int(input('Qual a altura da parede ?'))
Larg = int(input('Qual a largura da parede ?'))

def calculo_tinta():
    area = Altura * Larg
    total = area / Rend
    print(f'Voce precisa de {total} latas de tinta.')

calculo_tinta()
