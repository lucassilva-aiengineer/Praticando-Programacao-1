# Um sistema voltado para pizzarias 
# from faker import Faker


class Pizza:

    def __init__(self, nome_sabor, descricao, preco, igredientes):
        self.nome_sabor = nome_sabor 
        self.descricao = descricao 
        self.preco = preco
        self.igredientes = igredientes 
        self.custo_pizza = [igrediente.custo for igrediente in self.igredientes].sum()



    def exibir_pizza(self): 
        print(f"""
        Nome: {self.nome_sabor}
        Descrição: {self.descricao}
        Preco: {self.preco}
        Igredientes: {self.igredientes}
        """)





def teste():

    
    
    pizza1 = Pizza("Muçarella", "Pizza Saborosa 8 fatias", igredientes)