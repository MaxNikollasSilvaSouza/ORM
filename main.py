import salvar
import ListarRepositorio as lista

#input do nome do usuário no github
print("Insira o nome do usuário do github: ")
_nome = input()

#cria um objeto da classe de ListaDeRepositorios
repositorios = lista.listaDeRepositorios(_nome)

#puxa a lista de repositorios caso encontre, se nao encontrar puxa um status de erro http
dados_misturados = repositorios.requisicao_api()

dados_tratados =[]

#verifica se o valor retornado não é um numero inteiro (status de erro http)
if type(dados_misturados) is not int:

    print(f'Repositorios do usuário: {_nome}')

    #trata os dados que foram retornados, neste caso, pegando somente o nome dos repositorios
    for dado in range(len(dados_misturados)):
        dados_tratados.append(dados_misturados[dado]['name'])
        print(dados_misturados[dado]['name'])
    
    #salva no banco de dados (caso não tenha tabela, ele cria uma)
    print('\n\nSalvando no banco...\n\n')
    salvar.salvar(dados_tratados,_nome)
       
else:
    print(dados_misturados)
