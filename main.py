from functions import *
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='bubbles'
)

usuarios = {}

def cadastrar_usuario():
    global usuarios
    print("\n\n+ FOTO\n\n")
    nome_pessoa = input("Nome\n")
    nome_usuario = input("\nNome de usuário\n")
    dia = int(input("\nDia de nascimento: "))
    mes = int(input("mes de nascimento: "))
    ano = int(input("ano de nascimento: "))
    senha_pessoa = input("\nSenha\n")
    idade = descobrir_idade(dia, mes, ano)

    addusertotable(conexao, nome_pessoa, nome_usuario, idade, senha_pessoa)
    print("\nCadastro realizado com sucesso!")

def editar_pessoa(pessoa):
    global usuarios
    print("\n\n+ FOTO\n\n")
    print('Nome:', pessoa,
         '\nNome de usuário:', usuarios[pessoa]['nome de usuario'],'\nData de nascimento:', usuarios[pessoa]['data de nascimento'][0],'/',usuarios[pessoa]['data de nascimento'][1], '/', usuarios[pessoa]['data de nascimento'][2],'\nIdade:', usuarios[pessoa]['idade'], '\nSenha:', usuarios[pessoa]['senha'])
    print("\n\n1 - Editar nome")
    print("2 - Editar nome de usuário")
    print("3 - Editar data de nascimento")
    print("4 - Editar senha")
    print("0 - Voltar para menu")
    opcao_editar = int(input("Digite uma opção: "))

    if opcao_editar == 1:
        novo_nome = input("Novo nome\n ")
        usuarios[novo_nome] = usuarios.pop(pessoa)
    elif opcao_editar == 2:
        usuarios[pessoa]['nome de usuario'] = input("Novo nome de usuário\n")
    elif opcao_editar == 3:
        dia = int(input("Dia de nascimento\n"))
        mes = int(input("mes de nascimento\n"))
        ano = int(input("ano de nascimento\n"))
        usuarios[pessoa]['data de nascimento'] = [dia, mes, ano]
        usuarios[pessoa]['idade'] = descobrir_idade(dia, mes, ano)
    elif opcao_editar == 4:
        usuarios[pessoa]['senha'] = input("Nova senha\n")

def func_usuarios():
    opcao = 1
    while opcao != 0:
        print("1 - Configurações Usuário")
        print("2 - Adicionar tarefa")
        print("3 - Listar Usuários")
        print("0 - Voltar para menu")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            pessoa = input("Digite o nome: ")
            if pessoa in usuarios:
                editar_pessoa(pessoa)
            else:
                print("Usuário não encontrado!")

        elif opcao == 2:
            insert(conexao)
            print("\nTarefa atribuída ao usuário com sucesso!\n")

        elif opcao == 3:
            listar_usuarios(conexao)

def remover_pessoa(pessoa):
    global usuarios
    if pessoa in usuarios:
        del usuarios[pessoa]
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado!")

def descobrir_idade(dia, mes, ano):
    ANO_ATUAL = 2020
    MES_ATUAL = 10
    DIA_ATUAL = 20
    idade = 0
    if mes < MES_ATUAL or (MES_ATUAL == mes and dia < DIA_ATUAL):
        idade = ANO_ATUAL - ano
    else:
        idade = (ANO_ATUAL - ano) - 1

    return idade

opcao = -1
while opcao != 0:

    print("\n******** MENU **********")
    print("1 - Usuários")  #listar pessoas
    print("2 - Criar conta")  #cadastrar pessoa
    print("3 - Configurações pessoa")  #editar pessoa
    #print("4 - Deletar Pessoa") não vai precisar provavelmente
    print("0 - Encerrar programa")

    opcao = int(input("Digite uma das opções acima: "))

    if opcao == 1:
        func_usuarios()

    elif opcao == 2:
        cadastrar_usuario()

    elif opcao == 3:
        pessoa = input("Digite o nome: ")
        if pessoa in usuarios:
            editar_pessoa(pessoa)
        else:
            print("Usuário não encontrado!")

    elif opcao == 4:
        pessoa = input("Digite o nome: ")
        if pessoa in usuarios:
            remover_pessoa(pessoa)
        else:
            print("Usuário não encontrado!")
