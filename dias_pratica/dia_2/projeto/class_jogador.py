

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


    # setter - alteração 
    # Nós temos algo entre o atributo e a modificação, algo como um guarda de fronteira e 
    # podem impedir ou liberar a alteração.abs

    @id_.setter 
    def id_(self, nv_id: str):
        return self.__id_ == nv_id 

    

def main():

    """Testando se o código está correto..."""

    jogador = Jogador("marcos_joao", "12345", "Marcos")

    print(jogador.nome)
    print(jogador.senha)


if __name__ == '__main__':
    main()