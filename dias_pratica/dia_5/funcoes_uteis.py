import csv 
import time 


ARQUIVO = "dados\\meu_arquivo.csv"

def salvar(funcionario):

    nome = funcionario.nome 
    idade = funcionario.idade
    salario = funcionario.salario

    with open(ARQUIVO, "a", newline= '', encoding= "utf-8") as arquivo: 
        
        # file.write()
        # writer = csv.writer(arquivo)
        # writer.writerow([nome, idade, salario])

        # Utilizando uma Arquitetura 

        writer = csv.DictWriter(arquivo, fieldnames= ["nome", "idade", "salario"])

        writer.writerow({
            "nome": nome, 
            "idade": idade,
            "salario": salario 
        })


    time.sleep(0.5)
    for n in range(5):
        time.sleep(0.1)
        print("..." * n)


    print("Salvando...")