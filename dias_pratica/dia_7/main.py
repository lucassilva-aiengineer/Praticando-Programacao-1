from class_jogador import Jogador
import numpy as np 
from typing import Optional

# p1, p2, p3, p4, p5, p6, p7, p8, p9 = 0, 0, 0, 0, 0, 0, 0, 0, 0

# print(f"""{p1}|{p2}|{p3}\n{p4}|{p5}|{p6}\n{p7}|{p8}|{p9}""")


Matriz = np.array([["---", "---", "---"],
                    ["---", "---", "---"],
                    ["---", "---", "---"]])


# print(Matriz[0][0])
# print(Matriz[0][1])

# # Matriz[0][0] = 10

# # print(Matriz)


# print(Matriz[])

def play(jogadores)-> None:
    linha = int(input("Indique a linha: "))
    coluna = int(input("Indique a coluna: "))

    # Matriz[linha, coluna] = "O" if time % 2 == 0 else "X"

    # Matriz[linha, coluna] = "O" if jogador  else "X"

# print(Matriz)

def main():

    print("Bem vindo ao Jogo da velha animado!")

    def salvar_jogador()-> Jogador:
        nome = input("Indique o seu nome: ")
        jogador = Jogador(nome)

        return jogador

    jogador_1 = salvar_jogador()
    jogador_2 = salvar_jogador()


    jogadores = [jogador_1, jogador_2]
    jogador_nome = jogador_1.nome 
    while rodadas <= 9:

        if jogador_nome == jogador_1.nome:
            jogador_nome == jogador_2.nome 

        else:
            jogador_nome == jogador_1.nome 


        play(jogadores)
        
