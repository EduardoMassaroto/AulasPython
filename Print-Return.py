
def boas_vindas(nome, quantidade):
    print(f'Ola {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque.')

boas_vindas('Fulano', 5)
boas_vindas('Ciclano', 3)
boas_vindas('Beltrano', 1)

#obs sempre que tiver envolvendo numero converter a integer em string (str)

# o nome e quantidade sao PARAMETROS localizados em def boas_vindas entre parentes().

# o nome inserido e a quantidade inserida sao chamados de ARGUMENTOS 

# deafault = aquele q vc define o valor no parametro
# Non-Default = aquele q vc NAO define o valor no parametro
# Sempre usar o Non_Default primeiro, exemplo :

def teste(quantidade, nome='Fulano'):
    print(f'ola {nome}.')
    print(f'Quer comprar {str(quantidade)} laptops ?')

teste(5)

# Como eu nao defini meu parametro 'quantidade', eu chamei a variavel e acrescentei qual sera o valor do parametro, no caso (5)... na variavel TESTE o parametro nome esta definido como 'Fulano'.

# Diferença entre a funcao PRINT e RETURN :
# Print = imprime na tela (utilizado apenas em tarefa)
# Return = armazena os dados para depois imprimir na tela quando eu chamar essa variavel

# exemplo das anotacoes das linhas 28 a 30 abaixo :

def variavel(nome):
    print(f'Ola {nome}')

variavel('Ciclano')

# exemplo acima utilizacao de print.. exemplo abaixo de Return :

def variavel2(nome):
    return f'Ola {nome}'

print(variavel2('Beltrano'))

