#Importando bibliptecas/arquivos usados
from random import randint
from users import Usuario
from time import sleep
from salvadados import limpar,ler_dados,salvar_dados

#Lista principal que armazenará outras listas. Funciona como uma matriz.  
fichas=[]

#Chama a função do salvadados.py para ler os dados do arquivo de texto e atualizar a matriz passada no argumento da função.
def atualizadados():
    ler_dados(fichas,'fichas')

#As próximas funções sorteiam um número entre os selecionados
def jogar_d4() -> int:
    return randint(1,4)

def jogar_d13() -> int:
    return randint(1,13)

def jogar_d100() -> int:
    return randint(1,100)

#Adiciona uma nova ficha a matriz fichas e depois salva as altrerações no arquivo de texto.
def adicionar_banco_dados(jogador,nome_personagem,raca,level,forca,constituicao,agilidade,inteligencia,precisao,carisma,end):
    personagem=[jogador,nome_personagem,raca,level,forca,constituicao,agilidade,inteligencia,precisao,carisma]
    fichas.insert(end, personagem)
    salvar_banco_fichas(fichas)

#Definição da classe Jogador, que herda da classe Usuario
class Jogador(Usuario):
    def __init__(self,nome:str, email:str, senha:str,registro:int,jogador:bool,nome_personagem:str,raca:str,level:int,forca:int,constituicao:int,agilidade:int,inteligencia:int,precisao:int,carisma:int) -> None:
        super().__init__(nome, email, senha,registro)
        self.jogador=jogador
        self.nome_personagem=nome_personagem
        self.raca=raca
        self.level=level
        self.forca=forca
        self.constituicao=constituicao
        self.agilidade=agilidade
        self.inteligencia=inteligencia
        self.precisao=precisao
        self.carisma=carisma
    
    # Cria a ficha de um novo jogador. Pode ser aleatório ou escolhido pelo usuário.  
    def criar_jogador(self,endereco:int) -> None:
        aleatorio=int(input('Você deseja: \n1. Criar um personagem completamente aleatório \n2. Criar um personagem à sua escolha \n ->'))
        endereco=int(endereco)
        if aleatorio==1:  
            self.jogador=True
            self.nome_personagem=str(input('Defina o nome do personagem: '))  
            def_raca=jogar_d13()
            
            if def_raca==1:
                self.raca='Humano'
                self.level= 1
                self.forca = jogar_d4() + jogar_d4()
                self.constituicao= jogar_d4() + jogar_d4()
                self.agilidade= jogar_d4() + jogar_d4()
                self.inteligencia= jogar_d4() + jogar_d4()
                self.precisao= jogar_d4() + jogar_d4()
                self.carisma= jogar_d4() + jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==2:
                self.raca='Orc'
                self.level= 1
                self.forca = jogar_d4() + jogar_d4() + jogar_d4()
                self.constituicao= jogar_d4()+ jogar_d4() + jogar_d4()
                self.agilidade= jogar_d4() + jogar_d4()
                self.inteligencia= jogar_d4()
                self.precisao= jogar_d4() + jogar_d4()
                self.carisma=jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==3:
                self.raca='Elfo'
                self.level= 1
                self.forca = jogar_d4()
                self.constituicao= jogar_d4() + jogar_d4()
                self.agilidade= jogar_d4() + jogar_d4()+ jogar_d4()
                self.inteligencia= jogar_d4() + jogar_d4()
                self.precisao= jogar_d4() + jogar_d4()+ jogar_d4()
                self.carisma= jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==4:
                self.raca='Anão'
                self.level= 1
                self.forca = jogar_d4() + jogar_d4()+ jogar_d4()
                self.constituicao=jogar_d4() + jogar_d4()
                self.agilidade= jogar_d4()
                self.inteligencia=jogar_d4() + jogar_d4()
                self.precisao=jogar_d4() + jogar_d4()
                self.carisma= jogar_d4() + jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==5:
                self.raca='Feralin - Raposa'
                self.level= 1
                self.forca = jogar_d4() + jogar_d4()
                self.constituicao=jogar_d4()
                self.agilidade= jogar_d4()+jogar_d4() + jogar_d4()
                self.inteligencia= jogar_d4()+jogar_d4() + jogar_d4()
                self.precisao= jogar_d4() + jogar_d4()
                self.carisma= jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==6:
                self.raca='Feralin - Elefante'
                self.level= 1
                self.forca = jogar_d4() + jogar_d4() + jogar_d4() + jogar_d4()
                self.constituicao=jogar_d4() + jogar_d4() + jogar_d4()
                self.agilidade=jogar_d4()
                self.inteligencia=jogar_d4()
                self.precisao=jogar_d4()
                self.carisma=jogar_d4() + jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==7:
                self.raca='Feralin - Águia'
                self.level= 1
                self.forca =jogar_d4() 
                self.constituicao=jogar_d4() + jogar_d4()
                self.agilidade=jogar_d4() + jogar_d4()+ jogar_d4()
                self.inteligencia=jogar_d4() 
                self.precisao=jogar_d4() + jogar_d4()+ jogar_d4()
                self.carisma=jogar_d4()+ jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==8:
                self.raca='Feralin - Tigre'
                self.level= 1
                self.forca = jogar_d4() + jogar_d4()+ jogar_d4()
                self.constituicao=jogar_d4()+ jogar_d4()
                self.agilidade= jogar_d4() + jogar_d4()+ jogar_d4()
                self.inteligencia=jogar_d4()
                self.precisao=jogar_d4()+ jogar_d4()
                self.carisma=jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==9:
                self.raca='Dramon'
                self.level= 1
                self.forca = jogar_d4() + jogar_d4()+ jogar_d4()
                self.constituicao= jogar_d4() + jogar_d4()+ jogar_d4()
                self.agilidade=jogar_d4()+ jogar_d4()
                self.inteligencia=jogar_d4()+ jogar_d4()
                self.precisao=jogar_d4()+ jogar_d4()
                self.carisma=jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==10:
                self.raca='Imp'
                self.level= 1
                self.forca =jogar_d4()+ jogar_d4()
                self.constituicao=jogar_d4()+ jogar_d4()
                self.agilidade=jogar_d4() + jogar_d4()+ jogar_d4()
                self.inteligencia=jogar_d4()
                self.precisao=jogar_d4() + jogar_d4()+ jogar_d4()
                self.carisma=jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==11:
                self.raca='Migurd'
                self.level= 1
                self.forca = jogar_d4()+ jogar_d4()
                self.constituicao=jogar_d4()+ jogar_d4()+ jogar_d4()
                self.agilidade=jogar_d4()+ jogar_d4()
                self.inteligencia=jogar_d4()+ jogar_d4()
                self.precisao=jogar_d4()+ jogar_d4()
                self.carisma=jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==12:
                self.raca='Miigle'
                self.level= 1
                self.forca = jogar_d4()
                self.constituicao= jogar_d4() 
                self.agilidade= jogar_d4()+ jogar_d4()+ jogar_d4()
                self.inteligencia= jogar_d4()
                self.precisao= jogar_d4()+ jogar_d4()+ jogar_d4()
                self.carisma= jogar_d4()+ jogar_d4()+ jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
            if def_raca==13: 
                self.raca='Heavenlords'
                self.level= 1
                self.forca = jogar_d4()+ jogar_d4()+ jogar_d4()
                self.constituicao= jogar_d4()+ jogar_d4()+ jogar_d4()
                self.agilidade=jogar_d4()+ jogar_d4()+ jogar_d4()
                self.inteligencia=jogar_d4()+ jogar_d4()+ jogar_d4()
                self.precisao=jogar_d4()+ jogar_d4()+ jogar_d4()
                self.carisma=jogar_d4()+ jogar_d4()
                adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
        elif aleatorio==2:
            print('ATENÇÃO\n Nessa opção damos a você a escolha de escolher, mas converse com seu mestre para não quebrar as regras da sua mesa.  ')
            print('Escolha uma raça: \n1.Humano \n2.Orc \n3.Elfo \n4.Anãos \n5.Feralin - Raposa \n6.Feralin - Elefante \n7.Feralin - Águia \n8. Feralin - Tigre \n9.Dramon \n10. Imp \n11. Migurd \n12. Miigle \n13. Heavenlords')
            self.jogador=True
            self.raca=int(input('Escreva o nome da raça escolhida -> ' ))
            self.nome_personagem=str(input('Defina o nome do personagem: '))  
            self.level=int(input('Escreva o seu nível -> ' ))
            self.forca =int(input('Escreva o seu atributo Força -> ' ))
            self.constituicao= int(input('Escreva o seu atributo Constituição -> ' ))
            self.agilidade= int(input('Escreva o seu atributo Agilidade -> ' ))
            self.inteligencia= int(input('Escreva o seu atributo Inteligência -> ' ))
            self.precisao= int(input('Escreva o seu atributo Precisão -> ' ))
            self.carisma=int(input('Escreva o seu atributo Carisma -> ' ))
            adicionar_banco_dados(self.jogador,self.nome_personagem,self.raca,self.level,self.forca,self.constituicao,self.agilidade,self.inteligencia,self.precisao,self.carisma,endereco)
        else:
            print('ERRO! OPÇÃO INVÁLIDA')
            
#Limpa o arquivo de texto e salva as informações armazenadas na matriz passada como argumento.
def salvar_banco_fichas(matriz)->None:
    limpar('fichas')
    salvar_dados(matriz,'fichas')

#Le e imprime os dados armazenados no arquivo de texto
def exibir_banco_fichas()->None:
    ficha=[]
    ler_dados(ficha,'fichas')
    comprimento_colunas = [8, 10, 25, 5, 5, 12, 9, 12, 8, 7]
    
    cabecalho = ['Jogador', 'Nome', 'Raça', 'Level', 'Forca', 'Constituicao', 'Agilidade', 'Inteligencia', 'Precisao', 'Carisma']
    cabecalho_formatado = [f'{cabecalho[i]:^{comprimento_colunas[i]}}' for i in range(len(cabecalho))]
    print('|'.join(cabecalho_formatado))
    for i in range(len(ficha)):  
        for j in range(len(ficha[i])):
            print(f'{ficha[i][j]:<{comprimento_colunas[j]}}|',end='' )
        print('\n')
        sleep(5)

#Objeto da classe Jogador. Permite chamar os métodos da classe.        
jogador_auxiliar=Jogador(None,None,None,int(0),None,None,None,int(1),int(0),int(0),int(0),int(0),int(0),int(0))

