import time

biblioteca = False

class Jogador:

    """
        Classe Jogador 
        Objeto jogador
    """

    SENHA_DEV = "abcd"

    def __init__(self, user, senha, nome):


        self.__id_ = gerar_id() if biblioteca else 'abcd'
        self.__user = user
        self.__senha = senha 
        self.__nome = nome 
        self.__palavra_selecionada = ""
        self.__letra_selecionada = ""
        self.__score = 0 


    # Métodos Getters e setters 

    # Getters - Leitura 

    @property 
    def id_(self):
        return self.__id_ 

    @property 
    def user(self):
        # Eu poderia utilizar uma lógica para impedir o acesso 
        # já que tenho algo entre o atributo e o usuário que requisita o acesso. 
        # Posso pedir uma senha. 

        return self.__user 

    @property
    def senha(self):

        senha_dev = input("Indique a senha de desenvolvedor: ")

        if self.__class__.SENHA_DEV == senha_dev.lower(): # Verifica se a senha entregue pelo o usuário é igual a senha dev se sim retorna a senha 
            return self.__senha                           #  do usuário, assim o acesso fica restrito a profissionais altorizados.


    @property 
    def nome(self):
        return self.__nome 


    @property 
    def palavra_selecionada(self):
        # Retornando sem critério como se fosse público 

        print("Acessado opção")
        return self.__palavra_selecionada


    @property 
    def score(self):
        return self.__score 


    # setter - alteração 
    # Nós temos algo entre o atributo e a modificação, algo como um guarda de fronteira e 
    # podem impedir ou liberar a alteração.abs

    @id_.setter 
    def id_(self, nv_id: str):
        return self.__id_ == nv_id 


    @user.setter
    def user(self, nv_user):
        self.__user = nv_user 

    @senha.setter
    def senha(self, nv_senha):
        self.__senha == nv_senha


    @nome.setter 
    def nome(self, nv_nome):
        self.__nome = nv_nome         
        print("Nome alterado com sucesso!")



    # Método 

    def jogar(self):


        print("""
        Indique 
        """)


        self.__palavra_selecionada = input("Indique a sua opção: ")

        # if opcao in ["pedra", "papel", "tesoura"]:
        #     self.__opcoes = opcao 

        #     return True # Operação concluída com sucesso 
        # else:
        #     print("Opção não encontrada!")
        #     time.sleep(0.5)

        #     for n in range(0, 10):
        #         print("...")
        #         time.sleep(0.1)

        #     print("Tente novamente...")
        #     time.sleep(0.3)

            # return False
def main():

    """Testando se o código está correto..."""

    jogador = Jogador("marcos_joao", "12345", "Marcos")

    # print(jogador.nome)
    # print(jogador.senha)
    # print(f"ID{jogador.id_}")

    print(f"""Nome do Jogador: {jogador.nome}
ID: {jogador.id_}""")


    jogador.nome = "Mateus"

    print(f"Novo nome: {jogador.nome}")


    python(f"""Opção encontrada: {jogador.jogar()}
    Opção selecionada {jogador.palavra_selecionada}""")


if __name__ == '__main__':
    main()