
# Publicar um produto com comissao de 120% se for acima de R$ 10 reais

# Usar o INT para converter a str para valor (exemplo abaixo)

valor = int(input('Digite o valor do seu produto em R$: '))

while valor > 10:
    valor = (valor * 1.20) + valor
    print(f'O valor final do seu produto será de R$ {valor}')
    break
