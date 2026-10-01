import string 
import random
import time 

def gerar_id():

    """
        Uma função que Gera um ID para cada objeto jogador criado
    """

    # Letras maiúsculas 
    lista_letras = []
    
    lista_letras += string.ascii_uppercase
    lista_letras += string.ascii_lowercase

    # print(lista_letras)

    id_ = ""


    caracteres_adicionados, caracteres_adicionar = 0, 5
    while caracteres_adicionados < caracteres_adicionar:


        if random.randint(0, 1) == 0:
            id_ += str(random.randint(100, 999))

        else:

            random.shuffle(lista_letras)
            id_ += random.choice(lista_letras)

        # Condição de parada implícita
        caracteres_adicionados += 1

    
    return id_



def testes():

    letras_maiusculas = [] # Quebremos a string como sendo uma lista de caracteres 

    letras_maiusculas += string.ascii_uppercase # Lista só junta com lista, se esta string é uma lista 
    # Então é, ou passa ser uma lista de carcteres.

    letras_maiusculas += string.ascii_lowercase

    print(letras_maiusculas)



def salvar_score(objeto):

    NOME_ARQUIVO = "dias_pratica/dia_4/projeto/dados_partidas/arquivos.txt"
    with open(NOME_ARQUIVO, "a", encoding= 'utf-8') as arquivo:
        arquivo.write(f"{objeto.id_}, {objeto.nome}, {objeto.score}")

    print("Dados armazenados com sucesso!")
    time.sleep(2)
    

def main():
    # testes()

    print(f"ID teste: {gerar_id()}")


if __name__ == '__main__':
    main()