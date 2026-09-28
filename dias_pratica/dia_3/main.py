# Estrutras de dados 

# strings  



def strings():

    nome = "Philleas"
    sobre_nome = "Fogg"

    texto = "O meu nome é " + nome + " " + sobre_nome

    # texto[0] = "O meu nome é "

    texto += "\nUm viajante da ficção britânica."
    print(texto)


    # Métodos de string 

    print(f"Todas as letras maiúsculas: {texto.upper()}")

    print(f"\nOs inícios das palavras são maiúsculos: {texto.title()}")

    print("\nApenas a primeria palavra da frase se inícia com a letra maiúscula: {}".format(texto.capitalize()))


    print("Todas As letras são minúsculas: " + texto.lower())

    print("""Verificando informações sobre a grafia, escrita, utilizada na representação textual. 
    
É minúscula?: {}""".format(texto.islower()))

def main():


    strings()


if __name__ == '__main__':
    main()