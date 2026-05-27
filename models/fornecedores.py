import requests

# Importação da função Optional que tras os dados do fornecedor via CNPJ pelço api

from typing import Optional

# Importação do databse

from database.conexao import conexao, cursor

# Função do menu de escolha de função do fornecedor

def menu_fornecedor():

    while True:

        print("\n===== FORNECEDORES =====")
        print("1 - Cadastrar fornecedor")
        print("2 - Listar fornecedores")
        print("3 - Editar fornecedor")
        print("4 - Buscar fornecedor")
        print("5 - Remover fornecedor")
        print("6 - Voltar")



        opcao_fornecedor = input("Escolha uma opção: ")

        if opcao_fornecedor == "1":

            cadastrar_fornecedor()

        elif opcao_fornecedor == "2":

            listar_fornecedores()

        elif opcao_fornecedor == "3":

            editar_fornecedor()

        elif opcao_fornecedor == "4":

            buscar_fornecedor()

        elif opcao_fornecedor == "5":

            remover_fornecedor()

        elif opcao_fornecedor == "6":

            break

        else:

            print("\n❌ Opção inválida.")

# Função de importação dos dados via CNPJ dos fornecedores

def consultar_cnpj(cnpj):

    cnpj = cnpj.replace(".", "")
    cnpj = cnpj.replace("/", "")
    cnpj = cnpj.replace("-", "")

    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"

    try:

        resposta = requests.get(url)

        if resposta.status_code == 200:

            return resposta.json()

        elif resposta.status_code == 429:

            print("\n⚠ Muitas consultas realizadas. Tente novamente em alguns minutos.")

            return None

        else:

            print(f"\nErro API: {resposta.status_code}")

            return None

    except Exception as erro:

        print(f"\nErro na conexão: {erro}")

        return None

# Função de cadastramento de fornecedor

def cadastrar_fornecedor():

    print("\n===== CADASTRAR FORNECEDOR =====")

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

    INSERT INTO fornecedores (
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

    print("\n✅ Fornecedor cadastrado com sucesso!")

# Função de listar fornecedores cadastrados

def listar_fornecedores():

    print("\n===== FORNECEDORES =====")

    cursor.execute("SELECT * FROM fornecedores")

    fornecedores = cursor.fetchall()

    if len(fornecedores) == 0:

        print("\n❌ Nenhum fornecedor cadastrado.")
        return

    for fornecedor in fornecedores:

        print(f"\nID: {fornecedor[0]}")
        print(f"CNPJ: {fornecedor[1]}")
        print(f"Nome: {fornecedor[2]}")
        print(f"Endereço: {fornecedor[3]}")
        print(f"Telefone: {fornecedor[4]}")

# Função de edição dos dados do fornecedor escolhido

def editar_fornecedor():

    print("\n===== EDITAR FORNECEDOR =====")

    cursor.execute("SELECT * FROM fornecedores")

    fornecedores = cursor.fetchall()

    if len(fornecedores) == 0:

        print("\n❌ Nenhum fornecedor cadastrado.")
        return

    for fornecedor in fornecedores:

        print(f"{fornecedor[0]} - {fornecedor[2]}")

    try:

        id_fornecedor = int(input("\nDigite o ID do fornecedor: "))

        cursor.execute("""

        SELECT * FROM fornecedores
        WHERE id = ?

        """, (id_fornecedor,))

        fornecedor = cursor.fetchone()

        if fornecedor is None:

            print("\n❌ Fornecedor não encontrado.")
            return

        novo_nome = input("Novo nome: ")
        novo_endereco = input("Novo endereço: ")
        novo_telefone = input("Novo telefone: ")

        cursor.execute("""

        UPDATE fornecedores

        SET
            nome = ?,
            endereco = ?,
            telefone = ?

        WHERE id = ?

        """, (

            novo_nome,
            novo_endereco,
            novo_telefone,
            id_fornecedor

        ))

        conexao.commit()

        print("\n✅ Fornecedor atualizado com sucesso!")

    except ValueError:

        print("\n❌ Digite apenas números.")

# Função de busca de um fornecedor

def buscar_fornecedor():

    print("\n===== BUSCAR FORNECEDOR =====")

    busca = input("Digite o nome do fornecedor: ")

    cursor.execute("""

    SELECT * FROM fornecedores

    WHERE nome LIKE ?

    """, (f"%{busca}%",))

    fornecedores = cursor.fetchall()

    if len(fornecedores) == 0:

        print("\n❌ Nenhum fornecedor encontrado.")
        return

    for fornecedor in fornecedores:

        print(f"\nID: {fornecedor[0]}")
        print(f"CNPJ: {fornecedor[1]}")
        print(f"Nome: {fornecedor[2]}")
        print(f"Endereço: {fornecedor[3]}")
        print(f"Telefone: {fornecedor[4]}")

# Função de remover um fornecedor

def remover_fornecedor():

    print("\n===== REMOVER FORNECEDOR =====")

    cursor.execute("SELECT * FROM fornecedores")

    fornecedores = cursor.fetchall()

    if len(fornecedores) == 0:

        print("\n❌ Nenhum fornecedor cadastrado.")
        return

    for fornecedor in fornecedores:

        print(f"{fornecedor[0]} - {fornecedor[2]}")

    try:

        id_fornecedor = int(input("\nDigite o ID do fornecedor: "))

        cursor.execute("""

        SELECT * FROM fornecedores

        WHERE id = ?

        """, (id_fornecedor,))

        fornecedor = cursor.fetchone()

        if fornecedor is None:

            print("\n❌ Fornecedor não encontrado.")
            return

        cursor.execute("""

        DELETE FROM fornecedores

        WHERE id = ?

        """, (id_fornecedor,))

        conexao.commit()

        print("\n✅ Fornecedor removido com sucesso!")

    except ValueError:

        print("\n❌ Digite apenas números.")

