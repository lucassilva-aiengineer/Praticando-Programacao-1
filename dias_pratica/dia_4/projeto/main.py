import random 
import time
from typing import List



def run():

    print("Bem vindo ao Brasil Game!")

    
    cores = [
        "Azul", "Verde", "Vermelho", "Amarelo"
    ]

    

    while True:

        print("Para jogar uma partidade digite 1")
        print("Para encerrar o jogo digite 2")

        print("Digite a sua opção: ")
        opcao = int(input())

        if opcao == 1:
            cores_selecionadas = [random.choice(cores) for a in range(2)]

            print("Decore se puder!\n")

            for cor in cores_selecionadas:
                print(cor)

            time.sleep(5)
            print("...")
            time.sleep(1)

            for a in range(1000):
                print("_" * a) 
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


            break 




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