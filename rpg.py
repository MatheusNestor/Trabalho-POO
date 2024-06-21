#Salva as informações da 'matriz' no banco de dados.
import os
import users
import personagens
from personagens import jogador_auxiliar
from time import sleep
from typing import List,Union,Tuple

#Mostra o nome do software.
def mostrar_nome() -> None:

    print('''
█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█
██─▄─▄██─▄▄▄█─██▄─█
▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀

█─▄─▄─█▄─▄▄─█─▄▄▄▄█─▄─▄─█▄─▄▄─███▀░██
███─████─▄█▀█▄▄▄▄─███─████─▄█▀████░██
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▀
''')
    
#Limpa a tela do terminal.
def limpar_tela() -> None:
    os.system('cls')

#Mostra as opções do menu principal.
def mostrar_opções_menu_cadastro() -> None:
    print('\nSeja bem vindo ao nosso novo sistema de rpg! \n')
    print('1. Cadastrar um novo usuário -> ')
    print('2. Excluir um usuário -> ')
    print('3. Fazer login -> ')
    print('4. Mostrar personagens criados -> ')
    print('5. Sair -> \n')

#Chama as funções anteriores e recebe a entrada do que o usuário quer fazer.
def acessar_menu_cadastro() -> int:
    limpar_tela()
    mostrar_nome()
    mostrar_opções_menu_cadastro()
    opcao=int(input('O que você gostaria de fazer?  '))
    return opcao

#Mostra opções do menu de criação de personagens.
def mostrar_opções_menu_personagens():
    print('\nAqui você cria seus próprios personagens!')
    print('\n\nSua imaginação é o limite! \nSeja um criador de mundos, ou desbrave-os a bel-prazer!')
    print('1. Criar um personagem jogável -> ')
    print('2. Voltar ao menu anterior -> ')

#Mostra um menu depois do login
def acessar_menu_personagens():
    limpar_tela()
    mostrar_nome()
    mostrar_opções_menu_personagens()
    opcao = int(input('O que você gostaria de fazer?  '))
    return opcao

#Chama a função do user.py para verificar o login.
def login():
    limpar_tela()
    situacao,endereco=users.auxiliar.fazer_login()
    return situacao,endereco


 
    
# Organiza e chama as funções dos outros arquivos conforme as opções escolhidas.
def main():
    registro=users.atualiza_dados()
    personagens.atualizadados()
    opcao=None
    while opcao!=0:
        opcao=acessar_menu_cadastro()

        if opcao==1:
            users.auxiliar.criar_usuario(registro)
        elif opcao==2:
            users.auxiliar.excluir_usuario()
        elif opcao==3:
            situacao,endereco=login()
            if situacao== True:
                mostrar_nome()
                aux = acessar_menu_personagens()
                if aux == 1:
                    jogador_auxiliar.criar_jogador(endereco)
                elif aux == 2:
                    opcao=acessar_menu_cadastro()
                    
                else:
                    print('Essa opção ainda não está disponível!')
            else:
                print('Nome de usuário ou senha estão incorretos. \nTente Novamente!!.')
                sleep(3)
        elif opcao==4:
            personagens.exibir_banco_fichas()

        elif opcao==5:
            break
        
        else:
            print('Você deve estar cometendo um engano, tente novamente.')
            opcao=acessar_menu_cadastro()

#Chama a função 'main'   
main()