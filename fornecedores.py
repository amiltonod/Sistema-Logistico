from database import conexao, cursor


def menu_fornecedor():

    while True:

        print("\n===== FORNECEDORES =====")
        print("1 - Cadastrar fornecedor")
        print("2 - Listar fornecedores")
        print("3 - Voltar")

        opcao_fornecedor = input("Escolha uma opção: ")

        if opcao_fornecedor == "1":

            cadastrar_fornecedor()

        elif opcao_fornecedor == "2":

            listar_fornecedores()

        elif opcao_fornecedor == "3":

            break

        else:

            print("\n❌ Opção inválida.")


def cadastrar_fornecedor():

    print("\n===== CADASTRAR FORNECEDOR =====")

    cnpj = input("CNPJ: ")
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