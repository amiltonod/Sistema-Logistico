from utils.cnpj_api import consultar_cnpj

def menu_credor():

    while True:

        print("\n===== CREDORES =====")
        print("1 - Cadastrar credor")
        print("2 - Listar credores")
        print("3 - Editar credor")
        print("4 - Buscar credor")
        print("5 - Remover credor")
        print("6 - Voltar")



        opcao_credor = input("Escolha uma opção: ")

        if opcao_fornecedor == "1":

            cadastrar_credor()

        elif opcao_fornecedor == "2":

            listar_credores()

        elif opcao_fornecedor == "3":

            editar_credor()

        elif opcao_fornecedor == "4":

            buscar_credor()

        elif opcao_fornecedor == "5":

            remover_credor()

        elif opcao_credor == "6":

            break

        else:

            print("\n❌ Opção inválida.")