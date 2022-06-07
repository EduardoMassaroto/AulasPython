
altura = float(input('Qual sau altura ?'))
peso = float(input('Qual seu peso ?'))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print('Magreza')
elif IMC >= 18.5 and IMC < 25:
    print('Peso ideal')
if IMC > 25.01:
    print('Sobre peso')

    
