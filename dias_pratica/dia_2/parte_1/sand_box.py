import random 

def main():


    palavras = [    
                    {   "palavra":"escrivaninha",
                        "pista": "escritório"
                    }, 
                    {
                        "palavra": "mochila",
                        "pista": "escola"
                    },
                    {
                        "palavra": "cadeira",
                        "pista": "escritório"
                    }
                ]

    palavra = random.choice(palavras)

    opcao = "a"


    palavra_secreta = ""
    if opcao in palavra['palavra']:
        for letra in palavra['palavra']:
            if letra != opcao:
                palavra_secreta += " __ "

            else:
                palavra_secreta += opcao 


    print(f"""
Pista: {palavra['pista']}
Palavra Atual: {palavra_secreta}""")



if __name__ == '__main__':
    main()
