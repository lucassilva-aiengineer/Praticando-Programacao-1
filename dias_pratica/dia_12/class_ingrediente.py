
class Ingrediente:

    """
        Modelando a classe Ingrediente 

            - Atributos: 
                nome             : Nome do igrediente 
                custo            : Custo do igrediente por unidade de medida 
                quantidade       : Quantidade x unidade de medida 
                unidade de medida: Kg, gramas, ml, litros.
    """

    def __init__(self, nome, custo, quantidade, unidade_medida):

        self.nome = nome 
        self.custo = custo 
        self.quantidade = quantidade 
        self.unidade_medida = unidade_medida



    def exibir_igrediente(self):
        
        return f"""

Nome: {self.nome}
Custo unitário: {self.custo} x {self.unidade_medida}
Unidade de Medida: {self.unidade_medida}
Custo: {self.custo * self.quantidade}
Quantidade: {self.quantidade} {self.unidade_medida}
"""

ingrediente_1 = Ingrediente(
    "Mussarela", 
    28.90,
    0.300, 
    "Kg" 
)


print(ingrediente_1.exibir_igrediente())