from datetime import datetime

#irei importar a funcao datetime para fazer o calculo do ano atual - a data de nascimento dos funcionarios ( essa funcao ela sempre ira puxar o ano em que vc esta e futuramente mudara sozinha assim q mudar o ano tambem..)

# para criar classes sempre a primeira letra da classe tem q ser maiuscula ( Funcionarios por exemplo sera minha classe criada)

class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):

     self.nome = nome 
     self.sobrenome = sobrenome 
     self.data_nascimento = data_nascimento
 
 # criando outra funcao para a classe, funcao para retornar nome e sobrenome : 
    def nome_completo(self):
        return self.nome +  ' ' + self.sobrenome
     # para acrescentar um espaco entre o nome e o sobrenome colocar ' 
     
    # essa bosta de codigo abaixo deu erro, nao consegui resolve-lo
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.data_nascimento = int(ano_atual - self.data_nascimento)
        return self.data_nascimento

# criar objeto :
usuario1 = Funcionarios('Eduardo', 'Massaroto', '16/12/1998')
usuario2 = Funcionarios('Marcos', 'Massaroto', '10/10/1998')

print(usuario1.nome)
print(usuario2.nome)
# sempre que for chamar a funcao dentro de uma funcao self colocar () e fechar )
print(usuario1.nome_completo())
# existem 2 jeitos de chamar uma funcao dentro de outra funcao, exemplo 1 acima e exemplo 2 abaixo :
print(Funcionarios.nome_completo(usuario1))


# abaixo tenho o exemplo de uma classe com os objetos e os parametros sem estar em uma funcao, utilizando a funcao o codigo fica melhor e menor..
''''
# criar os parametros :
usuario1.nome = 'Eduardo'
usuario1.sobrenome = 'Massaroto'
usuario1.data_nascimento = '16/12/1998'

usuario2.nome = 'Marcos'
usuario2.sobrenome = 'Massaroto'
usuario2.data_nascimento = '10/10/1998'

print(usuario1.nome)
'''
