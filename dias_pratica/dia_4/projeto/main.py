import random 
import time
from typing import List
from classe_jogador import Jogador
from faker import Faker
from funcoes_uteis import salvar_score

def run():

    """
        A função que executa o jogo
    """
    print("Bem vindo ao Brasil Game!")

    
    cores = [
        "Azul", "Verde", "Vermelho", "Amarelo", "Lilás", "Laranja", "Branco"
    ]

# Conforme os níveis vão aumentando eu posso aumentar a dificuldade como aumenta o tamanho das 
# combinais.


    faker = Faker('en_US')
    jogador = Jogador(faker.name())
    

    print("Indique o seu nome: ")
    jogador.nome = input("nome: ")
    while True:

        print("Para jogar uma partidade digite 1")
        print("Para encerrar o jogo digite 2")

        print("Digite a sua opção: ")
        opcao = int(input())

        if opcao == 1:
            cores_selecionadas = [random.choice(cores) for a in range(4)]

            print("Decore se puder!\n")

            for cor in cores_selecionadas:
                print(cor)

            time.sleep(5)
            print("...")
            time.sleep(1)

            for a in range(1000):
                print("_" * random.randint(0, 1000)) 
                time.sleep(0.01)

            for a in range(5, -1):
                print(str(a))

            respostas: List[str] = []

            n = 1
            for palavra in cores_selecionadas:
                respostas.append(input(f"Indique a cor n°{n}: "))
                n += 1

            
            if cores_selecionadas == respostas:
                print("Você venceu!")
                jogador.aumentar_score()


            print("Retornando ao Menu...")
            time.sleep(3)

        elif opcao == 2:
            print("Que pena...")
            time.sleep(2)            
            print("Até logo...")
            time.sleep(2)
            print("Encerrando Jogo...")
            time.sleep(2)       

            print(f"""ID: {jogador.id_}
Nome: {jogador.nome}
Score: {jogador.score}""")


            salvar_score(jogador)

            break # Encerrando o loop

        else:
            print("Opção Inválida")
            print("Tentando novamente...")
            time.sleep(2)



def teste():

    letras = ["a", "b", "c", "d"]
    print([random.choice(letras) for a in range(2)])


    letras = ["a", "b", "c"]
    letras_b = ["a", "c", "b"]

    print(letras == letras_b)

def main():
    # teste()

    run()


if __name__ == '__main__':
    main()