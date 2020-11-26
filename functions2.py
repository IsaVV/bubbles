import datetime
import calendar
from datetime import date

def add_work_to_table(conexao, tarefa):
    cursor = conexao.cursor()
    com_sql = ("INSERT INTO Lista_de_Tarefas(Nome) VALUES (%s)")

    valor = (tarefa)
    cursor.execute(com_sql, valor)

    conexao.commit()

def addusertotable(conexao, nome, usuario, data_nascimento, senha, email):
    cursor = conexao.cursor()
    com_sql = ("INSERT INTO Lista_de_Usuarios(Nome, Usuario, Data_Nascimento, Senha, Email) VALUES (%s, %s, %s, %s, %s)")

    valor = (nome, usuario, data_nascimento, senha, email)
    cursor.execute(com_sql, valor)

    conexao.commit()

def descobrir_idade(dia, mes, ano):
    data_atual = date.today()
    data_em_texto = "{}/{}/{}".format(data_atual.day, data_atual.month,
                                      data_atual.year)

    idade = int(data_em_texto[6:]) - ano
    if (int(data_em_texto[3:5]) < mes):
        if (int(data_em_texto[0:2]) < dia):
            idade -= 1
    return idade

def day():
    from datetime import date
    def findDay(date):
        today = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[today])

    date = date.today()
    today = "{} {} {}".format(date.day, date.month, date.year)

    return(findDay(today))

def print_dia(conexao, dia):
    cursor = conexao.cursor()
    com_sql = "SELECT Pessoa, Tarefa, Hora_Inicio FROM Calendário WHERE Dia = " + str(dia)
    cursor.execute(com_sql)
    resultado = cursor.fetchall()

    for x in resultado:
        hora_inicio = str(x[2])[0:2] + ":" + str(x[2])[2:4]
        print("Pessoa: {} | Tarefa: {} | Hora: {}".format(x[0], x[1], hora_inicio))

    if not resultado:
        print("Dia livre!")

def outtxt(conexao, pessoa):
    cursor = conexao.cursor()
    cursor.execute("SELECT Tarefa, Hora_Inicio, Hora_Fim FROM Calendário WHERE Pessoa = '" + pessoa + "'")
    resultado = cursor.fetchall()

    now = datetime.datetime.now()
    time = int(str(now.hour) + str(now.minute))

    outF = open("output.txt", "w")
    with open('out.txt', 'w') as f:
        for x in resultado:
            if x[2] > time:
                outF.writelines(str(x[0]) + "," + str(x[1]) + ") ")

def listar_Tarefas(conexao):
  cursor = conexao.cursor()
  cursor.execute("SELECT Nome, Id FROM Lista_de_Tarefas")
  resultado = cursor.fetchall()
  print("")
  for x in resultado:
    print("\033[1;34mTarefa: \033[m: " + x[0] + " | \033[1;34mId: \033[m: " + str(x[1]))

def listar_usuarios(conexao):
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT Nome, Usuario, id, Data_Nascimento FROM Lista_de_Usuarios")
    resultado = cursor.fetchall()
    print("")
    for x in resultado:
        dia_nascimento = int(x[3][0:2])
        mes_nascimento = int(x[3][3:5])
        ano_nascimento = int(x[3][6:])
        idade = str(
            descobrir_idade(dia_nascimento, mes_nascimento, ano_nascimento))
        #perguntar a joice \033
        print("\033[1;34mNome:\033[m " + x[0] +
              " | \033[1;34mUsuário: \033[m" + x[1] +
              " | \033[1;34mId: \033[m" + str(x[2]) +
              " | \033[1;34mIdade: \033[m" + idade)
    print("")

def data(dia):
    from datetime import date
    date = date.today()
    if dia == "1":
        if day() == "Monday":
            return date.day

        elif day() == "Tuesday":
            return (date.day - 1)

        elif day() == "Wednesday":
            return (date.day - 2)

        elif day() == "Thursday":
            return (date.day - 3)

        elif day() == "Friday":
            return (date.day - 4)

        elif day() == "Saturday":
            return (date.day - 5)

        elif day() == "Sunday":
            return (date.day - 6)

    if dia == "2":
        if day() == "Monday":
            return (date.day + 1)

        elif day() == "Tuesday":
            return (date.day)

        elif day() == "Wednesday":
            return (date.day - 1)

        elif day() == "Thursday":
            return (date.day - 2)

        elif day() == "Friday":
            return (date.day - 3)

        elif day() == "Saturday":
            return (date.day - 4)

        elif day() == "Sunday":
            return (date.day - 5)

    if dia == "3":
        if day() == "Monday":
            return (date.day + 2)

        elif day() == "Tuesday":
            return (date.day + 1)

        elif day() == "Wednesday":
            return date.day

        elif day() == "Thursday":
            return (date.day - 1)

        elif day() == "Friday":
            return (date.day - 2)

        elif day() == "Saturday":
            return (date.day - 3)

        elif day() == "Sunday":
            return (date.day - 4)

    if dia == "4":
        if day() == "Monday":
            return (date.day - 3)

        elif day() == "Tuesday":
            return (date.day - 2)

        elif day() == "Wednesday":
            return (date.day - 1)

        elif day() == "Thursday":
            return date.day

        elif day() == "Friday":
            return (date.day + 1)

        elif day() == "Saturday":
            return (date.day + 2)

        elif day() == "Sunday":
            return (date.day + 3)

    if dia == "5":
        if day() == "Monday":
            return (date.day - 4)

        elif day() == "Tuesday":
            return (date.day - 3)

        elif day() == "Wednesday":
            return (date.day - 2)

        elif day() == "Thursday":
            return (date.day - 1)

        elif day() == "Friday":
            return date.day

        elif day() == "Saturday":
            return (date.day + 1)

        elif day() == "Sunday":
            return (date.day + 2)

    if dia == "6":
        if day() == "Monday":
            return (date.day - 5)

        elif day() == "Tuesday":
            return (date.day - 4)

        elif day() == "Wednesday":
            return (date.day - 3)

        elif day() == "Thursday":
            return (date.day - 2)

        elif day() == "Friday":
            return (date.day - 1)

        elif day() == "Saturday":
            return date.day

        elif day() == "Sunday":
            return (date.day + 1)

    if dia == "7":
        if day() == "Monday":
            return (date.day - 6)

        elif day() == "Tuesday":
            return (date.day - 5)

        elif day() == "Wednesday":
            return (date.day - 4)

        elif day() == "Thursday":
            return (date.day - 3)

        elif day() == "Friday":
            return (date.day - 2)

        elif day() == "Saturday":
            return (date.day - 1)

        elif day() == "Sunday":
            return date.day

def pessoa_por_usuario(conexao, usuario):
    cursor = conexao.cursor()
    cursor.execute("SELECT Nome FROM Lista_de_Usuarios WHERE Usuario = '" + usuario + "'")
    resultado = cursor.fetchall()

    return resultado[0][0]

