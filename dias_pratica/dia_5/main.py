import class_funcionario 
import funcoes_uteis
import time 
import random

def main():


    while True:

        frases = ["Para adicionar um funcionário digite 1", 
        "Para Sair digite 2"]

        for frase in frases:
            time.sleep(0.1)
            print("..." if random.randint(0, 1) == 0 else "..")
            print(frase)


        print("Indique a sua opcao:")
        opcao = int(input(""))


        if opcao == 1:

            nome, idade, salario = input("Indique o nome: "),\
            input("Indique a idade: "), input("Indique o salário: ")
            
            nv_funcionario = class_funcionario.Funcionario(nome, idade, salario)

            funcoes_uteis.salvar(nv_funcionario)

        elif opcao == 2:
            print("Saindo...")
            time.sleep(2)
            break 

        
    
    # Um bloco de execução Try - Except  


if __name__ == '__main__':
    main()