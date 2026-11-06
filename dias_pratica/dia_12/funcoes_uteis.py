from typing import Dict

def calcular_custo(ingredientes):

    """
            Uma função que calcula o custo dos ingredientes das 
            pizzas.  
    """

    custo_total = 0
    for ingrediente in ingredientes:
        custo_total += ingrediente["ingrediente_custo"]  


    return custo_total