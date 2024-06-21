#Importando bibliptecas/arquivos usados
from typing import List

#Salva as informações da 'matriz' no banco de dados.
def salvar_dados(matriz,nome:str) -> None:
    with open(str(nome),'a') as arquivo:
        for i in matriz: 
                linha=[str(elemento) for elemento in i]
                arquivo.write('|'.join(linha) + '\n')

#Acessa o banco de dados e salva a informação na 'matriz'.
def ler_dados(matriz:List[List[str]],nome:str) -> List[List[str]]:
    with open(str(nome),'r') as arquivo:
        for linha in arquivo: 
                matriz.append(linha.strip().split('|'))
    return matriz

#Limpa o banco de dados, deixando-o vazio. É necessário para evitar repetições.
def limpar(nome:str) -> None:
    with open(str(nome),'w') as arquivo:
        pass

#'Banco de dados' se refere a um arquivo de texto que guarda as informações.
#'Matriz' é um argumento das duas primeiras funções. Fucniona como uma lista de listas.  
    