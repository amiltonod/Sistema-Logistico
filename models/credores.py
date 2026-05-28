from database.conexao import conexao, cursor

from utils.cnpj_api import consultar_cnpj

# Importação da função Optional que tras os dados do credor via CNPJ pelço api

def menu_credor():

    while True:

        print("\n===== CREDORES =====")
        print("1 - Cadastrar credor")
        print("2 - Listar credores")
        print("3 - Editar credor")
        print("4 - Buscar credor")
        print("5 - Remover credor")
        print("6 - Voltar")



        opcao_credores = input("Escolha uma opção: ")

        if opcao_credores == "1":

            cadastrar_credor()

        elif opcao_credores == "2":

            listar_credores()

        elif opcao_credores == "3":

            editar_credor()

        elif opcao_credores == "4":

            buscar_credor()

        elif opcao_credores == "5":

            remover_credor()

        elif opcao_credores == "6":

            break

        else:

            print("\n❌ Opção inválida.")

# Função de cadastro de credores, onde o usuário pode inserir o CNPJ e caso seja encontrado na API, os dados serão preenchidos automaticamente, caso contrário, o usuário poderá preencher manualmente os dados do credor.

def cadastrar_credor():

    print("\n===== CADASTRAR CREDORES =====")

    cnpj = input("CNPJ: ")
    
    dados = consultar_cnpj(cnpj)

    if dados is not None:

        nome = dados["razao_social"]

        endereco = (
            f"{dados['logradouro']}, "
            f"{dados['numero']} - "
            f"{dados['municipio']}/{dados['uf']}"
        )

        print(f"\nEmpresa encontrada: {nome}")
        print(f"Endereço: {endereco}")

    else:

        print("\n❌ CNPJ não encontrado.")

        nome = input("Nome: ")
        endereco = input("Endereço: ")

    telefone = input("Telefone: ")

    cursor.execute("""

    INSERT INTO credores (
        cnpj,
        nome,
        endereco,
        telefone
    )

    VALUES (?, ?, ?, ?)

    """, (

        cnpj,
        nome,
        endereco,
        telefone

    ))

    conexao.commit()

    print("\n✅ Credor cadastrado com sucesso!")

# Função para listar os credores cadastrados, exibindo seus dados de forma organizada. Caso não haja nenhum credor cadastrado, uma mensagem de aviso será exibida.

def listar_credores():

    print("\n===== CREDORES =====")

    cursor.execute("SELECT * FROM credores")

    credores = cursor.fetchall()

    if len(credores) == 0:

        print("\n❌ Nenhum credor cadastrado.")
        return

    for credor in credores:

        print(f"\nID: {credor[0]}")
        print(f"CNPJ: {credor[1]}")
        print(f"Nome: {credor[2]}")
        print(f"Endereço: {credor[3]}")
        print(f"Telefone: {credor[4]}")


# Função de edição dos dados do credor escolhido, onde o usuário pode selecionar o ID do credor que deseja editar e atualizar seus dados. Caso o ID não seja encontrado, uma mensagem de aviso será exibida. O usuário também deve inserir apenas números para o ID.

def editar_credor():

    print("\n===== EDITAR CREDORES =====")

    cursor.execute("SELECT * FROM credores")

    credores = cursor.fetchall()

    if len(credores) == 0:

        print("\n❌ Nenhum credor cadastrado.")
        return

    for credor in credores:

        print(f"{credor[0]} - {credor[2]}")

    try:

        id_credor = int(input("\nDigite o ID do credor: "))

        cursor.execute("""

        SELECT * FROM credores
        WHERE id = ?

        """, (id_credor,))

        credor = cursor.fetchone()

        if credor is None:

            print("\n❌ Credor não encontrado.")
            return

        novo_nome = input("Novo nome: ")
        novo_endereco = input("Novo endereço: ")
        novo_telefone = input("Novo telefone: ")

        cursor.execute("""

        UPDATE credores 

        SET
            nome = ?,
            endereco = ?,
            telefone = ?

        WHERE id = ?

        """, (

            novo_nome,
            novo_endereco,
            novo_telefone,
            id_credor

        ))

        conexao.commit()

        print("\n✅ Credor atualizado com sucesso!")

    except ValueError:

        print("\n❌ Digite apenas números.")

# Função de busca dos credores cadastrados, onde o usuário pode digitar o nome do credor que deseja buscar e os resultados serão exibidos. Caso nenhum credor seja encontrado, uma mensagem de aviso será exibida.

def buscar_credor():

    print("\n===== BUSCAR CREDORES =====")

    busca = input("Digite o nome do credor: ")

    cursor.execute("""

    SELECT * FROM credores

    WHERE nome LIKE ?

    """, (f"%{busca}%",))

    credores = cursor.fetchall()

    if len(credores) == 0:

        print("\n❌ Nenhum credor encontrado.")
        return

    for credor in credores:

        print(f"\nID: {credor[0]}")
        print(f"CNPJ: {credor[1]}")
        print(f"Nome: {credor[2]}")
        print(f"Endereço: {credor[3]}")
        print(f"Telefone: {credor[4]}")


# Função de remoção de um credor, onde o usuário pode selecionar o ID do credor que deseja remover. Caso o ID não seja encontrado, uma mensagem de aviso será exibida. O usuário também deve inserir apenas números para o ID.

def remover_credor():

    print("\n===== REMOVER CREDORES =====")

    cursor.execute("SELECT * FROM credores")

    credores = cursor.fetchall()

    if len(credores) == 0:

        print("\n❌ Nenhum credor cadastrado.")
        return

    for credor in credores:

        print(f"{credor[0]} - {credor[2]}")

    try:

        id_credor = int(input("\nDigite o ID do credor: "))

        cursor.execute("""

        SELECT * FROM credores

        WHERE id = ?

        """, (id_credor,))

        credor = cursor.fetchone()

        if credor is None:

            print("\n❌ Credor não encontrado.")
            return

        cursor.execute("""

        DELETE FROM credores

        WHERE id = ?

        """, (id_credor,))

        conexao.commit()

        print("\n✅ Credor removido com sucesso!")

    except ValueError:

        print("\n❌ Digite apenas números.")
