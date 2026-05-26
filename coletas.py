from database import conexao, cursor


# =========================
# FUNÇÕES AUXILIARES
# =========================

def obter_coletas():

    cursor.execute("SELECT * FROM coletas")

    return cursor.fetchall()


def exibir_coleta(coleta):

    print(f"\n===== COLETA ID {coleta[0]} =====")
    print("----------------------")
    print(f"Cliente: {coleta[1]}")
    print(f"Motorista: {coleta[2]}")
    print(f"Placa: {coleta[3]}")
    print(f"Veículo: {coleta[4]}")
    print(f"Prioridade: {coleta[5]}")
    print(f"Horário: {coleta[6]}")


def listar_ids_coletas(coletas):

    for coleta in coletas:

        print(f"{coleta[0]} - {coleta[1]}")

def obter_prioridade():

    while True:

        print("\nPrioridade:")
        print("1 - Alta")
        print("2 - Média")
        print("3 - Baixa")

        opcao_prioridade = input("Escolha a prioridade: ")

        if opcao_prioridade == "1":

            return "alta"

        elif opcao_prioridade == "2":

            return "media"

        elif opcao_prioridade == "3":

            return "baixa"

        else:

            print("\n❌ Opção inválida.")


# =========================
# MENU
# =========================

def menu_coleta():

    while True:

        print("\n===== COLETAS =====")
        print("1 - Cadastrar coleta")
        print("2 - Ver programação")
        print("3 - Remover coleta")
        print("4 - Editar coleta")
        print("5 - Buscar coleta")
        print("6 - Estatísticas")
        print("7 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":

            cadastrar_coleta()

        elif opcao == "2":

            listar_coletas()

        elif opcao == "3":

            remover_coleta()

        elif opcao == "4":

            editar_coleta()

        elif opcao == "5":

            buscar_coleta()

        elif opcao == "6":

            mostrar_estatisticas()

        elif opcao == "7":

            break

        else:

            print("\n❌ Opção inválida.")


# =========================
# CADASTRAR COLETA
# =========================

def cadastrar_coleta():

    print("\n===== CADASTRAR COLETA =====")

    cliente = input("Cliente: ")
    motorista = input("Motorista: ")
    placa = input("Placa: ")
    veiculo = input("Veículo: ")

    prioridade = obter_prioridade()

    horario = input("Horário: ")

    cursor.execute("""

    INSERT INTO coletas (
        cliente,
        motorista,
        placa,
        veiculo,
        prioridade,
        horario
    )

    VALUES (?, ?, ?, ?, ?, ?)

    """, (

        cliente,
        motorista,
        placa,
        veiculo,
        prioridade,
        horario

    ))

    conexao.commit()

    print("\n✅ Coleta cadastrada com sucesso!")


# =========================
# LISTAR COLETAS
# =========================

def listar_coletas():

    print("\n===== PROGRAMAÇÃO =====")

    coletas = obter_coletas()

    if len(coletas) == 0:

        print("\n❌ Nenhuma coleta cadastrada.")
        return

    print(f"\nTotal de coletas: {len(coletas)}")

    for coleta in coletas:

        exibir_coleta(coleta)


# =========================
# REMOVER COLETA
# =========================

def remover_coleta():

    print("\n===== REMOVER COLETA =====")

    coletas = obter_coletas()

    if len(coletas) == 0:

        print("\n❌ Nenhuma coleta cadastrada.")
        return

    listar_ids_coletas(coletas)

    try:

        id_coleta = int(input("\nDigite o ID da coleta: "))

        cursor.execute("""

        SELECT * FROM coletas

        WHERE id = ?

        """, (id_coleta,))

        coleta = cursor.fetchone()

        if coleta is None:

            print("\n❌ Coleta não encontrada.")
            return

        cursor.execute("""

        DELETE FROM coletas

        WHERE id = ?

        """, (id_coleta,))

        conexao.commit()

        print("\n✅ Coleta removida com sucesso!")

    except ValueError:

        print("\n❌ Digite apenas números.")


# =========================
# EDITAR COLETA
# =========================

def editar_coleta():

    print("\n===== EDITAR COLETA =====")

    coletas = obter_coletas()

    if len(coletas) == 0:

        print("\n❌ Nenhuma coleta cadastrada.")
        return

    listar_ids_coletas(coletas)

    try:

        id_coleta = int(input("\nDigite o ID da coleta: "))

        cursor.execute("""

        SELECT * FROM coletas

        WHERE id = ?

        """, (id_coleta,))

        coleta = cursor.fetchone()

        if coleta is None:

            print("\n❌ Coleta não encontrada.")
            return

        print("\nDigite os novos dados:")

        cliente = input("Cliente: ")
        motorista = input("Motorista: ")
        placa = input("Placa: ")
        veiculo = input("Veículo: ")

        prioridade = obter_prioridade()

        horario = input("Horário: ")

        cursor.execute("""

        UPDATE coletas

        SET
            cliente = ?,
            motorista = ?,
            placa = ?,
            veiculo = ?,
            prioridade = ?,
            horario = ?

        WHERE id = ?

        """, (

            cliente,
            motorista,
            placa,
            veiculo,
            prioridade,
            horario,
            id_coleta

        ))

        conexao.commit()

        print("\n✅ Coleta atualizada com sucesso!")

    except ValueError:

        print("\n❌ Digite apenas números.")


# =========================
# BUSCAR COLETA
# =========================

def buscar_coleta():

    print("\n===== BUSCAR COLETA =====")

    busca = input("Digite o nome do cliente: ")

    cursor.execute("""

    SELECT * FROM coletas

    WHERE cliente LIKE ?

    """, (f"%{busca}%",))

    coletas = cursor.fetchall()

    if len(coletas) == 0:

        print("\n❌ Nenhuma coleta encontrada.")
        return

    for coleta in coletas:

        exibir_coleta(coleta)


# =========================
# ESTATÍSTICAS
# =========================

def mostrar_estatisticas():

    coletas = obter_coletas()

    if len(coletas) == 0:

        print("\n❌ Nenhuma coleta cadastrada.")
        return

    alta = 0
    media = 0
    baixa = 0

    for coleta in coletas:

        prioridade = coleta[5].lower()

        if prioridade == "alta":

            alta += 1

        elif prioridade == "media":

            media += 1

        elif prioridade == "baixa":

            baixa += 1

    print("\n===== ESTATÍSTICAS =====")

    print(f"\nTotal de coletas: {len(coletas)}")
    print(f"Prioridade Alta: {alta}")
    print(f"Prioridade Média: {media}")
    print(f"Prioridade Baixa: {baixa}")