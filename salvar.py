#importo o que eu preciso
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

#coloco o caminho da conexão
engine = create_engine('mssql+pymssql://username:password@servername.database.windows.net:1433/databasename', echo=False)
#crio uma ferramente de acesso (que também é a chave)
Session = sessionmaker(bind=engine)

#crio um objeto para trabalhar com essa ferramenta
session=Session()

#crio meu objeto que suportará todas as variaveis da tabela
#ela será passada como parametro, em outras palavras, ela é um objeto q suporta mais de 1 parametro
Base = declarative_base()

#Essa 'Base' que é o parâmetro, é um objeto
#Portanto, não é necessário adicionar outros parametros, uma vez que a 'Base' suporta
#todos os valores de cada variasveis da tabela
class   Repositorios(Base):

    #nomeio a tabela
    __tablename__ = 'repositorios'

    #crio as colunas da tabela
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    repositorio = Column(String(255))

#isso tem que ficar fora da classe, pois será declarado por ultimo para criar a tabela
#se ficar dentro da classe (que no caso representa a tabela / é a tabela) vai dar erro no programa
Base.metadata.create_all(engine)

#função para criar a tabela no banco e salvar os dados
def salvar(dados_tratados,nome):
   
    #um laço for onde vai adicionar todos os dados na minha ferramente que também é minha chave de acesso
    #o conceito é similar ao do github no 'add'
    for dado in range(len(dados_tratados)):
        repositorio = Repositorios(name=f'{nome}', repositorio=dados_tratados[dado])
        #similar ao processo de push para o github
        session.add(repositorio)
        #print(dados_misturados[dado]['name'])
    
    #é necessário realizar um commit quando for enviar. Pois caso esqueça, os dados não serão salvos
    session.commit()
    #fecha a conexão com o banco
    session.close()
    print('Dados Salvos no Banco de Dados com Sucesso!!!')