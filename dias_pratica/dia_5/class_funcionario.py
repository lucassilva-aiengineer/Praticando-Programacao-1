class Funcionario:

    def __init__(self, nome, idade, salario):
        self.nome = nome 
        self.idade = idade
        self.salario = salario 




def teste():

    funcionario1 = Funcionario("Marcos", 20, 5000)

    print(funcionario1.nome)
    print(funcionario1.nome)
    print(funcionario1.salario)

def main():
    teste()


if __name__ == '__main__':
    main()
