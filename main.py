# Importando fuções do módulo de coletas

from services.coletas import menu_coleta

# Importando funções do módulo de fornecedores

from models.fornecedores import menu_fornecedor

# Importando funções do módulo de credores

from models.credores import menu_credor


print("===================================")
print(" SISTEMA DE PROGRAMAÇÃO LOGÍSTICA ")
print("===================================")

# Loop para execução do menu principal

while True:

    print("\n===== MENU PRINCIPAL =====")
    print("1 - Coletas")
    print("2 - Fornecedores")
    print("3 - Credores")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        menu_coleta()

    elif opcao == "2":

        menu_fornecedor()

    elif opcao == "3":

        menu_credor()

    elif opcao == "4":

        print("\nSistema encerrado.")
        break

    else:

        print("\n❌ Opção inválida.")