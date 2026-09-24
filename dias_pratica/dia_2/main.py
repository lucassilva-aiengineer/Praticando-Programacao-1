def condicionais()-> None:

    print("Indique a sua idade: ")
    idade = int(input(""))

    if idade < 10:
        print("Você é uma criança!")

    elif idade < 17:
        print("Você é um adolescente!")

    elif idade < 50:
        print("Você é um adulto")

    else:
        print("Você é uma pessoa experiente!")



def main():
    condicionais()


if __name__ == '__main__':
    main()