import requests
import json


class listaDeRepositorios():

    #é a função de inicio do programa, o 'self' é semelhante a um dicionário em python, armazena variáveis na própria classe
    def __init__(self,usuario):
        self._usuario = usuario

    #realiza a requisição na api do github
    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            #caso de erro, ele retorna um status http
            return resposta.status_code
    
#self.usuario = usuario
#dados_api = repositorios