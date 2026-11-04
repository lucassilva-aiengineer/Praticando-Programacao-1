from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker


# Em sqlalchemy temos a possíbilidade de trabalhar com dados como objetos python. 

Base = declarative_base()


class Livro(Base):

    # Nome da base de dados 
    __tablename__ = "estante"

    ssn = Column("ssn", Integer, primary_key= True) 
    titulo = Column("titulo", String)
    autor = Column("autor", String)


    # Definindo um método construtor 
    def __init__(self, ssn, titulo, autor):
        self.ssn = ssn 
        self.titulo = titulo 
        self.autor = autor 


    def __repr__(self):
        return f"({self.ssn}) - ({self.titulo}) - ({self.autor})"


engine = create_engine("sqlite:///livros.db", echo= True) # echo = True, conecta ao banco de dados

Base.metadata.create_all(bind= engine)

# Criando seção 
Session = sessionmaker(bind= engine)
session = Session()




def teste_1():
    # Adicionando um objeto 

    livro_1 = Livro(15189045, "Reflexões", "C.S Lewis")
    session.add(livro_1)

    session.commit()


def salvar_livro(livro):

    l1 = Livro(10000, livro.titulo, livro.autor)
    session.add(l1)
    session.commit()

