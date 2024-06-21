#Importando bibliptecas/arquivos usados
import salvadados
from time import sleep
from validate_email import validate_email
from typing import  List,Union,Tuple

#Lista principal que armazenará outras listas. Funciona como uma matriz. 
banco_usuarios=[]

#Perceorre o banco de usuários e retorna o número de registro do usuário.
def percorre_nome_matriz(usuarios:List[List[str]],nome:str):
    cont=0
    while cont<(len(usuarios)):
        if usuarios[cont][0]==nome:
            return usuarios[cont][3]
        else:
            pass
        cont+=1

#Percorre o  banco deusuários e verifica se já existe o nome de usuário passado no argumento.
def verifica_nome_novo_usuário(usuarios:List[List[str]],nome:str) ->str:
    cont=0
    while cont<(len(usuarios)):
        if usuarios[cont][0]==nome:
            nome=str(input('Esse nome de usuário já existe. Tente outro -> '))
            while usuarios[cont][0]==nome:
                nome=str(input('Esse nome de usuário já existe. Tente outro -> '))
                cont-=1
        else:
            pass
        cont+=1
    return nome

#Percorre o  banco deusuários e verifica se existe o nome de usuário e a senha passados nos argumentos.
def verifica_login(usuarios:List[List[str]],usuario:str,senha:str) -> Tuple[Union[bool,int]]:
    cont=0
    while cont<(len(usuarios)):
        if usuarios[cont][0]==usuario:
            if usuarios[cont][2]==senha:
                x=usuarios[cont][3]
                return True,x
            else:
                return False,False
        else:
            pass 
        cont+=1
    return False,False

#Chama a função do salvadados.py para ler os dados do arquivo de texto e atualizar a matriz passada no argumento da função.
def atualiza_dados() -> int:
    salvadados.ler_dados(banco_usuarios,'banco_dados')
    tamanho=len(banco_usuarios)
    registro_atual=int(banco_usuarios[tamanho-1][3])+1
    return registro_atual

#Definição da classe Usuário
class Usuario():
    def __init__(self, nome:str, email:str, senha:str,registro:str) -> None :
        self.nome=nome
        self.email=email
        self.__senha=senha
        self.registro=registro
    
    #Método decorado que permite acessar as informações do atributo privado.
    @property
    def mostrasenha(self) ->str:
        return self.__senha
    
    #Cria um usuário novo fazendo o tratamento das entradas.
    def criar_usuario(self,registro:int) -> None:
        nome=str(input('\nDefina o nome de usuário -> '))
        self.nome=verifica_nome_novo_usuário(banco_usuarios,nome)
        self.email=str(input('Informe seu endereço de e-mail -> '))
        email=validate_email(self.email)
        while email != True:
            print('Entre com um endereço de e-mail válido')
            self.email=str(input('Informe seu endereço de e-mail -> '))
            email=validate_email(self.email)
        self.__senha=str(input('Informe sua senha -> '))
        confirme_senha=str(input('Confirme a senha -> ')) 
        if self.mostrasenha==confirme_senha:
            self.registro=registro
            usuario=[self.nome,self.email,self.mostrasenha,self.registro]
            banco_usuarios.append(usuario)
            print('🅒🅐🅓🅐🅢🅣🅡🅞 🅡🅔🅐🅛🅘🅩🅐🅓🅞 🅒🅞🅜 🅢🅤🅒🅔🅢🅢🅞❗')
            sleep(3)
        else:
            while self.senha != confirme_senha:
                confirme_senha=str(input('Você deve estar cometendo um erro, confirme exatamente a mesma senha -> ')) 
            self.registro=self.registro+1
            usuario=[self.nome,self.email,self.senha,self.registro]
            banco_usuarios.append(usuario)
            print('🅒🅐🅓🅐🅢🅣🅡🅞 🅡🅔🅐🅛🅘🅩🅐🅓🅞 🅒🅞🅜 🅢🅤🅒🅔🅢🅢🅞❗')
            sleep(3)
        salvadados.limpar('banco_dados')
        salvadados.salvar_dados(banco_usuarios,'banco_dados')    
    
    #Exclui um usuário que já existe do banco de dados.
    def excluir_usuario(self) -> None:
        usuario_excluir=str(input('Qual o nome do usuário que deseja apagar? '))
        registro_excluir = int(percorre_nome_matriz(banco_usuarios,usuario_excluir))
        if (input('Tem certeza que deseja excluir esse usuário? Aperte n para cancelar ou enter para continuar.')) != 'n':
            confirme_senha=str(input('Confirme a sua senha para continuar-> '))
            if banco_usuarios[registro_excluir-1][2] ==confirme_senha:
                del banco_usuarios[registro_excluir-1]
                print(f'O usuário {usuario_excluir}, nº de registro {registro_excluir} foi excluído com sucesso')
                sleep(3)
            else:
                pass
        else:
            pass
        salvadados.limpar('banco_dados')
        salvadados.salvar_dados(banco_usuarios,'banco_dados') 
    
    #Verifica se as condições necessárias para fazer login foram atendidas.
    def fazer_login(self):
        usuario=str(input('Digite o seu nome de usuário: '))
        senha=str(input('Digite sua senha: '))
        situacao,endereco=verifica_login(banco_usuarios,usuario,senha) 
        if situacao == True:
            print('Login efetuado com sucesso!')
            sleep(3)
            return True,endereco
        else:
            return False,40400000000000000000000000

#Objeto da classe que Usuário. Permite chamar os métodos da classe.
auxiliar=Usuario(None,None,None,int(0))     
  