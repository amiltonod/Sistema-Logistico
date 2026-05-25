from coletas import menu_coleta

from fornecedores import menu_fornecedor


print("===================================")
print(" SISTEMA DE PROGRAMAÇÃO LOGÍSTICA ")
print("===================================")


while True:

    print("\n===== MENU PRINCIPAL =====")
    print("1 - Coletas")
    print("2 - Fornecedores")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        menu_coleta()

    elif opcao == "2":

        menu_fornecedor()

    elif opcao == "3":

        print("\nSistema encerrado.")
        break

    else:

        print("\n❌ Opção inválida.")