from typing import Dict, List, Union
import time

def teste1():


    # def cadastrar_colaborador()-> Dict[Union[str, float]]:
    def cadastrar_colaborador():

        """
            Um função que cria um dicionário com as informações de uma pessoa 
            específica.
        """

        # Identificador 
        id_ = input("Indique um id numérico: ")

        # Informações pessoais 
        nome, cpf, data_nascimento = input("Indique o seu Nome: "),\
        input("Indique o seu cpf: "), input("Indique a sua data de nascimento: ")
        

        # Informações de cargo
        funcao, salario = input("Indique a função: "), float(input("Indique o salário: "))


        pessoa = {
            "id": id_,
            "nome": nome, 
            "cpf": cpf, 
            "data_nascimento": data_nascimento,
            "funcao": funcao, 
            "salario": salario
        }

        return pessoa 


    pessoas: List[str, Dict[Union[str, float]]] = []


    while True:
        print("===== MENU =====")
        time.sleep(1)

        print("Para ADICIONAR Uma Pessoa Digite 1")
        print("Para REMOVER uma Pessoa Digite 2")
        print("Para Sair Digite 3")


        opcao = int(input("Indique a sua opção: "))

        if opcao == 1:
            print("Adicionando Colaborador...")
            time.sleep(1.5)

            colaborador = cadastrar_colaborador()
            pessoas.append(colaborador)
            print("Adicionando colaborador...")
            time.sleep(1.5)

        elif opcao == 2:
            print("Removendo Colaborado...")
            time.sleep(1.5)

        elif opcao == 3:
            print("Saindo...")

            time.sleep(1.5)
            break   

        else:
            print("Opção não encontrada...")
            time.sleep(1)

            print("Tentando novamente...")
            for n in range(5, 0, -1):
                time.sleep(0.3)
                print(n)

        

def main():

    try:
        teste1()

    except ValueError as message:
        print(message)
        print("Tipo errado...")
        print("Tentando novamente...")
        time.sleep(1.5) 

        # teste1()
        main()

    else:
        print("Nenhum erro encontrado...")

    finally:
        print("Código finalmente executado...")



if __name__ == '__main__':
    main()