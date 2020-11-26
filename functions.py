from functions2 import *

def tela_sobre():
    print(
        "\033[1;34mOLÁ, LIMPINH@!\033[m\n Somos a equipe Bubbles, composta por alunos da CESAR School. Sabemos como é difícil manter"
        "nossas casas organizadas e limpas nessa época tão complicada, pensando nisso, criamos o CLEANOW! Um "
        "aplicativo mobile super prático que te ajudará a cuidar da sua moradia nos melhores momentos e assim "
        "criar novas memórias incríveis.")

def tela_relatar_problema(conexao):
    cursor = conexao.cursor()
    problema = input("-------AJUDA-------\n" "RELATAR UM PROBLEMA\n" "-> ")

    comsql = ("INSERT INTO Reclamacoes(Reclamacao) VALUES (%s)")
    cursor.execute(comsql, problema)
    conexao.commit()

    print("Obrigade por informar o seu problema.\n"
          "Resolveremos o mais rápido possível!")

def apagar_Tarefa(conexao):
    cursor = conexao.cursor()
    listar_Tarefas(conexao)
    id_tarefa = str(input("Digite o ID da tarefa que deseja remover: "))
    cursor.execute("DELETE FROM Lista_de_Tarefas WHERE id = '" + id_tarefa + "'")
    conexao.commit()

def insert(conexao):
    cursor = conexao.cursor()

    id_tarefa = input("\033[1;34mDigite o ID da tarefa: \033[m")

    cursor.execute(
        "SELECT Nome FROM Lista_de_Tarefas WHERE Id = {}".format(id_tarefa))
    tarefa = str(cursor.fetchall())
    tarefa = tarefa[3:-5]

    listar_usuarios(conexao)
    id_usuario = input("\033[1;34mDigite o ID do usuário: \033[m")

    cursor.execute("SELECT Nome FROM Lista_de_Usuarios WHERE Id = " +
                   id_usuario)
    usuario = str(cursor.fetchall())
    usuario = usuario[3:-5]

    horario = input("Horário: ")
    dia = input("Dia: ")

    com_sql = "INSERT INTO Calendário(Pessoa, Tarefa, Hora_Inicio, Dia) VALUES (%s, %s, %s, %s)"
    valor = (usuario, tarefa, horario, dia)
    cursor.execute(com_sql, valor)
    conexao.commit()

def login(conexao, email, senha):
    cursor = conexao.cursor()
    cursor.execute("SELECT Email FROM Lista_de_Usuarios")
    resultado = cursor.fetchall()
    check = False

    for x in resultado:
        if email in x:
            check = True

    if check == False:
        print("Usuário não encontrado!")
        return False

    com_sql = "SELECT Senha FROM Lista_de_Usuarios WHERE Email = '" + email + "'"
    cursor.execute(com_sql)
    senha_real = cursor.fetchall()

    if senha_real[0][0] == senha:
        return True

    else:
        print("Senha incorreta!")
        return False

def usuario_email(conexao, email):
    cursor = conexao.cursor()
    com_sql = "SELECT Usuario FROM Lista_de_Usuarios WHERE Email = '" + email + "'"
    cursor.execute(com_sql)
    usuario = cursor.fetchall()

    return usuario[0][0]

def weekcalendar(conexao):
    from datetime import date

    date = date.today()
    if day() == "Monday":
        for dia in range(date.day, date.day + 7):
            if dia == date.day:
                print("\033[1;34mSEG\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 1):
                print("\033[1;34mTER\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 2):
                print("\033[1;34mQUA\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 3):
                print("\033[1;34mQUI\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 4):
                print("\033[1;34mSEX\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 5):
                print("\033[1;34mSAB\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 6):
                print("\033[1;34mDOM\033[m")
                print_dia(conexao, dia)
            print("")

    if day() == "Tuesday":
        for dia in range(date.day - 1, date.day + 6):
            if dia == (date.day - 1):
                print("\033[1;34mSEG\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day):
                print("\033[1;34mTER\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 1):
                print("\033[1;34mQUA\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 2):
                print("\033[1;34mQUI\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 3):
                print("\033[1;34mSEX\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 4):
                print("\033[1;34mSAB\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 5):
                print("\033[1;34mDOG\033[m")
                print_dia(conexao, dia)
            print("")
    if day() == "Wednesday":
        for dia in range(date.day - 2, date.day + 5):
            if dia == (date.day - 2):
                print("\033[1;34mSEG\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 1):
                print("\033[1;34mTER\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day):
                print("\033[1;34mQUA\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 1):
                print("\033[1;34mQUI\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 2):
                print("\033[1;34mSEX\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 3):
                print("\033[1;34mSAB\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 4):
                print("\033[1;34mDOM\033[m")
                print_dia(conexao, dia)
            print("")
    if day() == "Thursday":
        for dia in range(date.day - 3, date.day + 4):
            if dia == (date.day - 3):
                print("\033[1;34mSEG\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 2):
                print("\033[1;34mTER\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 1):
                print("\033[1;34mQUA\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day):
                print("\033[1;34mQUI\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 1):
                print("\033[1;34mSEX\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 2):
                print("\033[1;34mSAB\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 3):
                print("\033[1;34mDOM\033[m")
                print_dia(conexao, dia)
            print("")
    if day() == "Friday":
        for dia in range(date.day - 4, date.day + 3):
            if dia == (date.day - 4):
                print("\033[1;34mSEG\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 3):
                print("\033[1;34mTER\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 2):
                print("\033[1;34mQUA\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 1):
                print("\033[1;34mQUI\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day):
                print("\033[1;34mSEX\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 1):
                print("\033[1;34mSAB\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 2):
                print("\033[1;34mDOM\033[m")
                print_dia(conexao, dia)
            print("")
    if day() == "Saturday":
        for dia in range(date.day - 5, date.day + 2):
            if dia == (date.day - 5):
                print("\033[1;34mSEG\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 4):
                print("\033[1;34mTER\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 3):
                print("\033[1;34mQUA\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 2):
                print("\033[1;34mQUI\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 1):
                print("\033[1;34mSEX\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day):
                print("\033[1;34mSAB\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day + 1):
                print("\033[1;34mDOM\033[m")
                print_dia(conexao, dia)
            print("")
    if day() == "Sunday":
        for dia in range(date.day - 6, date.day + 1):
            if dia == (date.day - 6):
                print("\033[1;34mSEG\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 5):
                print("\033[1;34mTER\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 4):
                print("\033[1;34mQUA\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 3):
                print("\033[1;34mQUI\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 2):
                print("\033[1;34mSEX\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day - 1):
                print("\033[1;34mSAB\033[m")
                print_dia(conexao, dia)

            elif dia == (date.day):
                print("\033[1;34mDOM\033[m")
                print_dia(conexao, dia)
            print("")

def editar_pessoa(pessoa, conexao):
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT Nome, Data_Nascimento FROM Lista_de_Usuarios WHERE Usuario = '"
        + pessoa + "'")
    resultado = cursor.fetchall()
    data_nascimento = resultado[0][1]
    dia_nascimento = int(data_nascimento[0:2])
    mes_nascimento = int(data_nascimento[3:5])
    ano_nascimento = int(data_nascimento[6:])
    idade = str(
        descobrir_idade(dia_nascimento, mes_nascimento, ano_nascimento))
    print("\nNome de usuário: " + pessoa + "\nNome: " + resultado[0][0] +
          "\nIdade: " + idade)

    opcao = 1
    while (opcao != 0):
        opcao = editarinformacoes(conexao, pessoa)

def cadastrar_usuario(conexao):
    print("\033[1;34m------ CADASTRO ------\033[m")
    global usuarios
    print("\n+ FOTO\n")
    nome_pessoa = input("Nome: ")
    nome_usuario = input("Nome de usuário: ")
    data_nascimento = input("Data de nascimento (formato DD/MM/AAAA): ")
    senha_pessoa = input("Senha: ")
    email = input("Email: ")

    addusertotable(conexao, nome_pessoa, nome_usuario, data_nascimento, senha_pessoa, email)
    print("\nCadastro realizado com sucesso!")

def remover_pessoa(conexao):
    cursor = conexao.cursor()
    listar_usuarios(conexao)
    nome = ""
    opcao = input("Digite o ID do usuário: ")
    cursor.execute("SELECT Nome FROM Lista_de_Usuarios WHERE id = '" + opcao +
                   "'")
    cursor.execute("DELETE FROM Lista_de_Usuarios WHERE id = '" + opcao + "'")
    resultado = cursor.fetchall()
    for x in resultado:
        nome = x[0]
    cursor.execute("DELETE FROM Calendário WHERE Pessoa = '" + nome + "'")
    conexao.commit()

def editarinformacoes(conexao, pessoa):
    cursor = conexao.cursor()
    print("\n1 - Editar nome")
    print("2 - Editar data de nascimento")
    print("3 - Editar senha")
    print("0 - Voltar para menu")

    opcao_editar = int(input("Digite uma opção: "))

    if opcao_editar == 1:
        novo_nome = input("Novo Nome: ")
        cursor.execute("UPDATE Lista_de_Usuarios SET Nome = '" + novo_nome +
                       "' WHERE Usuario = '" + pessoa + "'")
        pessoa = novo_nome
        conexao.commit()
        print("Edição concluída com sucesso!")
    elif opcao_editar == 2:
        dia = str(input("\nDia de nascimento: "))
        mes = str(input("\nMes de nascimento: "))
        ano = str(input("\nAno de nascimento: "))
        nova_data_de_nascimento = (dia + "/" + mes + "/" + ano)
        cursor.execute("UPDATE Lista_de_Usuarios SET Data_Nascimento = '" +
                       nova_data_de_nascimento + "' WHERE Usuario = '" +
                       pessoa + "'")
        conexao.commit()
        print("Edição concluída com sucesso!")
    elif opcao_editar == 3:
        senha = input("Senha atual: ")
        cursor.execute("SELECT Senha FROM Lista_de_Usuarios WHERE Usuario = '"
                       + pessoa + "'")
        resultado = cursor.fetchall()
        if senha == resultado[0][0]:
            nova_senha = input("\nNova Senha: ")
            cursor.execute("UPDATE Lista_de_Usuarios SET Senha = '" +
                           nova_senha + "' WHERE Usuario = '" + pessoa + "'")
            conexao.commit()
            print("Edição concluída com sucesso!")
        else:
            print("Senha incorreta")

    return (opcao_editar)

def checklist(conexao, pessoa):
    dia = input("1 - SEGUNDA\n"
                "2 - TERÇA\n"
                "3 - QUARTA\n"
                "4 - QUINTA\n"
                "5 - SEXTA\n"
                "6 - SÁBADO\n"
                "7 - DOMINGO\n")

    dia = str(data(dia))
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT Tarefa, Hora_Inicio, Hora_Fim FROM Calendário WHERE Pessoa = '" + pessoa + "' AND Dia = '" + dia + "'")
    resultado = cursor.fetchall()

    if len(resultado) == 1:
        for x in resultado:
            print(x[0] + " às " + (str(x[1])[0:2] + ":" + str(x[1])[2:4]))

    now = datetime.datetime.now()
    time = int(str(now.hour) + str(now.minute))

    outF = open("output.txt", "w")
    with open('out.txt', 'w') as f:
        for x in resultado:
            if x[2] > time:
                outF.writelines(str(x[0]) + "," + str(x[1]) + ") ")

def monthcalendar(conexao):
    cursor = conexao.cursor()
    for day in range(1, 32):
        cursor.execute("SELECT Tarefa, Pessoa FROM Calendário WHERE Dia = '" + str(day) + "'")
        resultado = cursor.fetchall()
        print("\033[1;34mDia " + str(day) + "\033[m")

        for x in resultado:
            print("Tarefa:", x[0], "Pessoa:", x[1])

        if not resultado:
            print("Dia livre!")
        print("")

def cadastro_horarios_livres(conexao, usuario):
    hora1 = input("Digite o 1º horário livre no formato HHMM: ")
    hora2 = input("Digite o 2º horário livre no formato HHMM: ")
    hora3 = input("Digite o 3º horário livre no formato HHMM: ")
    cursor = conexao.cursor()

    com_sql = ("INSERT INTO Horarios_Livres (Nome, Hora1, Hora2, Hora3) VALUES (%s, %s, %s, %s)")

    valor = (usuario, hora1, hora2, hora3)
    cursor.execute(com_sql, valor)

    conexao.commit()

def print_horarios_livres(conexao):
    cursor = conexao.cursor()

    cursor.execute("SELECT Nome, Hora1, Hora2, Hora3 FROM Horarios_Livres")
    resultado = cursor.fetchall()
    for x in resultado:
        hora1 = str(x[1])[0:2] + ":" + str(x[1])[2:4]
        hora2 = str(x[2])[0:2] + ":" + str(x[2])[2:4]
        hora3 = str(x[3])[0:2] + ":" + str(x[3])[2:4]
        print ("\033[1;34mPessoa: \033[m" + x[0] + "\033[1;34m Horários: \033[m" + hora1 + "\033[1;34m | \033[m" + hora2 + "\033[1;34m | \033[m" + hora3)

