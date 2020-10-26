def addusertotable(conexao, nome, usuario, idade, senha):
    cursor = conexao.cursor()
    com_sql = ("INSERT INTO Lista_de_Usuarios(Nome, Usuario, Idade, Senha) VALUES (%s, %s, %s, %s)")

    valor = (nome, usuario, idade, senha)
    cursor.execute(com_sql, valor)

    conexao.commit()

def insert(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT Nome, Id FROM Lista_de_Tarefas")
    resultado = cursor.fetchall()

    print("TAREFAS")
    for x in resultado:
        print(x)
    id_tarefa = input("Digite o ID da tarefa: ")

    cursor.execute("SELECT Nome FROM Lista_de_Tarefas WHERE Id = {}".format(id_tarefa))
    tarefa = str(cursor.fetchall())
    tarefa = tarefa[3:-5]

    cursor.execute("SELECT Nome, Id FROM Lista_de_Usuarios")
    resultado = cursor.fetchall()

    print("\nUSUÁRIOS")
    for x in resultado:
        print(x)
    id_usuario = input("Digite o ID do Usuário: ")

    cursor.execute("SELECT Nome FROM Lista_de_Usuarios WHERE Id = " + id_usuario)
    usuario = str(cursor.fetchall())
    usuario = usuario[3:-5]

    horario = input("Horário: ")
    dia = input("Dia: ")

    com_sql = "INSERT INTO Calendário(Pessoa, Tarefa, Hora_Inicio, Dia) VALUES (%s, %s, %s, %s)"
    valor = (usuario, tarefa, horario, dia)
    cursor.execute(com_sql, valor)
    conexao.commit()

def listar_usuarios(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT Nome, Usuario, Idade, id FROM Lista_de_Usuarios")
    resultado = cursor.fetchall()
    print("")
    for x in resultado:
        print(x)
    print("")