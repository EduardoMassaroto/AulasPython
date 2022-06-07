#desafio 91. filtrando funcionarios em uma empresa

funcionarios = ['Ana', 'Alice', 'Sophia', 'Melissa']
turno_dia = ['Ana', 'Melissa']
turno_noite = ['Alice', 'Sophia']
tem_carro = ['Ana', 'Sophia']

#lista1
lista1 = set(tem_carro).intersection(turno_noite)
lista2 = set(tem_carro).intersection(turno_dia)
lista3 = set(funcionarios).difference(tem_carro)
