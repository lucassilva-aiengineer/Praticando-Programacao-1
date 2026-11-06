from typing import List 
import funcoes_uteis as fc


class Pizza:

    def __init__(self, sabor:str, ingredientes: list):

        self.sabor = sabor 
        self.ingredientes = ingredientes
        self.custo = 0
        self.preco = 0
        self.comentarios: List[dict] = []



    def calcular_custo(self):

        self.custo = fc.calcular_custo(self.ingredientes)


    def adicionario_ingredientes(self):
        
        nome = input("Indique o nome do ingrediente: ")
        custo = float(input("Indique o custo do igrediente: "))

        self.ingredientes.append({
            "ingrediente_nome": nome, 
            "ingrediente_custo": custo
        })

def testes_1():

    ingredientes = [

    {
        "ingrediente_nome": "farinha de trigo",
        "ingrediente_custo": 4.50
    },
    {
        "ingrediente_nome": "tomate",
        "ingrediente_custo": 4.59 
    }
]


    pizza_1 = Pizza("Mussarela", ingredientes)

    pizza_1.calcular_custo()

    print(f"Custo de produção: {pizza_1.custo}")




    # Acrescentando ingredientes 

    pizza_1.adicionario_ingredientes()

    pizza_1.calcular_custo()
    print(f"Novo custo: {pizza_1.custo}")

def main():

    testes_1()


if __name__ == '__main__':
    main() 
    
