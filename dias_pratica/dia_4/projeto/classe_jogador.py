class Jogador:

    def __init__(self, id_, nome):
        # self.id = id_
        self.nome = nome 
        self.score = 0

    
    def aumentar_score(self):
        self.score += 1



def main():

    jogador_1 = Jogador("001", "Marcos")

    print(jogador_1.nome)
    print(f"Placar: {jogador_1.score}")

    for a in range(5):
        jogador_1.aumentar_score()

    print(f"Placar: {jogador_1.score}")


if __name__ == '__main__':
    main()
    