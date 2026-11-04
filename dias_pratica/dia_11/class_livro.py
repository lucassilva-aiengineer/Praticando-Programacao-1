from dados import base_dados 

class Livro:

    def __init__(self, titulo: str, autor: str, sinopse: str,\
                custo: float, preco_venda: float):


        self.titulo = titulo 
        self.autor = autor 
        self.sinopse = sinopse 
        self.custo = custo
        self.preco_venda = preco_venda 


    # Encapsulamento 
    # Getters e setters 
    

    # Métodos - Alteram ou criam novos atributos 
    def exibir_livro(self)-> None:

        print(f"""  ======= Informações sobre o livro ======== 
Título: {self.titulo}
Autor: {self.autor} 
\nSinopse:
{self.sinopse}
À vista no Pix: R${self.preco_venda:.2f}""")


    def salvar_livro(self):
        base_dados.salvar_livro(self)



def teste_1():

    livro_1 = Livro("Reflexões Cristãs", 
    "C. S. Lewis", 
    "Considerado um apologeta tão brilhante quanto um crítico de seu tempo...", 
    12.00, 40.00)

    print(livro_1.autor)
    print(livro_1.titulo)

    livro_1.exibir_livro()

    livro_1.salvar_livro()

def main():

    teste_1()


if __name__ == "__main__":
    main()