from functions import *
import pymysql
from ctypes import *

libCalc = CDLL("./libcalci.so")

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='bubbles'
)

verificando = False
opcao = 0
noti = "on"

while opcao != 1:  # paginal inicial
    print("\033[1;34m------- BEM VINDE AO --------\n"
          "--------- CLEANOW ----------\n"
          "Preparado para ficar limpinh@?\n\033[m"
          "1 - CRIAR CONTA\n"
          "2 - JÁ TENHO UMA CONTA")

    opcao = int(input("Digite uma das opções acima: "))

    if opcao == 1:
        usuario_cadastro = cadastrar_usuario(conexao)
        print("\033[1;34m------ ÚLTIMO PASSO! ------\033[m")
        print("Selecione seus horários livres para tarefas: ")
        cadastro_horarios_livres(conexao, usuario_cadastro)
    else:
        opcao = 1

while (verificando == False):  # login
    print("\033[1;34m--------LOGIN--------\033[m")
    login_email = str(input("Email: "))
    login_senha = str(input("Senha: "))
    verificando = login(conexao, login_email, login_senha)
    if verificando == True:
        login_usuario = usuario_email(conexao, login_email)

while opcao != 0: # menu
    opcao2 = 1

    print("\033[1;34m\n---------- MENU ----------\033[m"
          "\n1 - Calendário"
          "\n2 - Check list"
          "\n3 - Moradores"
          "\n4 - Tarefas"
          "\n5 - Ajustes")

    opcao = int(input("Opção: "))

    if opcao == 1:
        print("\033[1;34m\n---------- CALENDÁRIO SEMANAL ----------\033[m")
        weekcalendar(conexao)
        while opcao2 != 0:
            print("1- Calendário Mensal"
                  "\n0- Voltar")
            opcao2 = int(input("opção: "))
            if opcao2 == 1:
                monthcalendar(conexao)

    elif opcao == 2:
        print("\033[1;34m\n---------- CHECK LIST ----------\033[m")
        pessoa = pessoa_por_usuario(conexao, login_usuario)
        checklist(conexao, pessoa)

    elif opcao == 3:
        while opcao2 != 0:
            print("\033[1;34m\n---------- MORADORES ----------\033[m")
            listar_usuarios(conexao)
            print("\n1 - Adicionar Morador"
                  "\n0 - Voltar")
            opcao2 = int(input("Digite uma opção: "))

    elif opcao == 4:
        while opcao2 != 0:
            print("\033[1;34m\n---------- TAREFAS ----------\033[m")
            print("1 - Selecionar Tarefa"
                  "\n2 - Horários Livres"
                  "\n3 - Seleção Por Sorteio"
                  "\n0 - Voltar")
            opcao2 = int(input("Opção: "))

            if opcao2 == 1:
                print("\033[1;34m\n---------- SELECIONAR TAREFA ----------\033[m")
                listar_Tarefas(conexao)
                print("1 - Selecionar tarefa para usuário"
                      "\n2 - Adicionar tarefa"
                      "\n0 - Voltar")
                opcao3 = int(input("Opção: "))

                if opcao3 == 1:
                    insert(conexao)
                elif opcao3 == 2:
                    print("\033[1;34m\n---------- ADICIONAR TAREFA ----------\033[m"
                          "\nEx: molhar as plantas")
                    tarefa = str(input("Nova Tarefa: "))

                    add_work_to_table(conexao, tarefa)
                    
              elif opcao2 == 2:
                  print("\033[1;34m\n---------- HORÁRIOS LIVRES ----------\033[m")
                  print_horarios_livres(conexao)

    elif opcao == 5:
        while opcao2 != 0:
            print("\033[1;34m\n---------- AJUSTES ----------\033[m")
            print("1 - Editar conta"
                  "\n2 - Notificações" 
                  "\n3 - Acessibilidade"
                  "\n4 - Ajuda"
                  "\n5 - Sobre"
                  "\n6 - Sair"
                  "\n0 - Voltar")
            opcao2 = int(input("Opção: "))

            if opcao2 == 1:
                print("\033[1;34m\n---------- EDITAR PESSOA ----------\033[m")
                check = False

                cursor = conexao.cursor()
                pessoa = input("Digite o Nome de Usuário: ")
                com_sql = "SELECT Usuario FROM Lista_de_Usuarios WHERE Usuario = '" + pessoa + "'"
                cursor.execute(com_sql)
                resultado = cursor.fetchall()

                for x in resultado:
                    if pessoa in x:
                        editar_pessoa(pessoa, conexao)
                        check = True

                if check == False:
                    print("Usuário não encontrado!")

            if opcao2 == 2:
                opcao3 = 0
                print("Notificações", noti)
                if noti == "on":
                    print("1 - Mudar notifações para off\n"
                          "0 - Voltar")
                else:
                    print("1 - Mudar notificações para on\n"
                          "0 - Voltar")
                    opcao3 = input("Opção: ")
                    if opcao3 == 1 and noti == "on":
                        noti = "off"
                    else:
                        noti = "on"

            elif opcao2 == 4:
                tela_relatar_problema()
            elif opcao2 == 5:
                tela_sobre()
            elif opcao2 == 6:
                quit()


print("\n\033[1;33m <・)"
"\n ( _ヲ\033[m"
"\n\033[1;34m^^^＾^^^\033[m")
