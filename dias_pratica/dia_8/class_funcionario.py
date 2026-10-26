# E se eu utiliza-se os conceitos que eu sei para desenvolver e públicar sistemas nestes projetos?
# Conceitos de flask linguagem de programação banco de dados e tudo mais.

import time 

class Funcionario:
    """
        Um objeto que modela os funcionários da empresa 
    """
    def __init__(self, nome: str, idade: int, salario: float, funcao: str, descricao: str, score: int): # Argumentos 

        # Atributos públicos (por enquanto)
        self.nome = nome 
        self.idade = idade 
        self.salario = salario 
        self.funcao = funcao 
        self.descricao = descricao 
        self.score = score 

    # Encapsulamento 
    # Getters e Setters 

    # Métodos 

    def exibir_funcionario(self)-> str:
        return f""" 
            Nome: {self.nome}       Idade: {self.idade}
            Função: {self.funcao}   Salário: {self.salario}
            Descrição: {self.descricao}
            Score: {self.score}

        """

    def salvar_dados(self):
        """Um método que salva os dados em um banco de dados"""


    def alterar_salario(self):

        print("Alterando salário...")
        for n in range(5):
            time.sleep(1)
            print(n)


        # while True:
        #     ... 
        time.sleep(1)
        
        print("Salário Atual: ")



# Testando a função 

def teste():

    """
        Uma função que testa a criação de objetos e a utilização 
        de um método  
    """


    funcionario = Funcionario("Lucas", 
    22, 50000, "Head de Inteligência Artificial", "O Lucas é um excelente funcionário, trabalha muito e merece ser bem remunerado por isso.", 98)

    print(funcionario.nome)
    print(funcionario.idade)

    print(funcionario.exibir_funcionario())

    funcionario.alterar_salario()

def main():

    print("Testando função...")
    time.sleep(2)

    teste()



if __name__ == '__main__':
    main()
