import json

try:

    with open("coletas.json", "r", encoding="utf-8") as arquivo:
        coletas = json.load(arquivo)

except FileNotFoundError:

    coletas = []

print("===================================")
print(" SISTEMA DE PROGRAMAÇÃO LOGÍSTICA ")
print("===================================")

def mostrar_menu():

    print("\nMENU")
    print("1 - Cadastrar coleta")
    print("2 - Ver programação")
    print("3 - Remover coleta")
    print("4 - Sair")

def salvar_coletas():

    with open("coletas.json", "w", encoding="utf-8") as arquivos:
        json.dump(coletas, arquivos, ensure_ascii=False, indent=4)

while True:

    mostrar_menu()


    opcao = input("Escolha uma opção: ")

    # CADASTRAR COLETA
    if opcao == "1":

        cliente = input("Cliente: ")
        motorista = input("Motorista: ")
        placa = input("Placa: ")
        veiculo = input("Veículo: ")
        rota = input("Rota: ")
        prioridade = input("Prioridade: ")
        horario = input("Horário: ")

        coleta = {
            "cliente": cliente,
            "motorista": motorista,
            "placa": placa,
            "veiculo": veiculo,
            "rota": rota,
            "prioridade": prioridade,
            "horario": horario
        }

        coletas.append(coleta)

        print("\n✅ Coleta cadastrada com sucesso!")

    # VER PROGRAMAÇÃO
    elif opcao == "2":

        print("\n===== PROGRAMAÇÃO =====")

        if len(coletas) == 0:
            print("Nenhuma coleta cadastrada.")

        else:

            print(f"\nTotal de coletas: {len(coletas)}")

            for indice, coleta in enumerate(coletas, start=1):
                print(f"\n===== COLETA {indice} =====")
                print("----------------------")
                print(f"Cliente: {coleta['cliente']}")
                print(f"Placa: {coleta['placa']}")
                print(f"Veículo: {coleta['veiculo']}")
                print(f"Motorista: {coleta['motorista']}")
                print(f"Rota: {coleta['rota']}")
                print(f"Prioridade: {coleta ['prioridade']}")
                print(f"Horário: {coleta['horario']}")


    # REMOVER COLETAS

    elif opcao == "3":

        if len(coletas) == 0:

            print("\n❌ Nenhuma coleta cadastrada.")

        else:

            print("\n===== REMOVER COLETA =====")

            for indice, coleta in enumerate(coletas, start=1):
                print(f"{indice} - {coleta['cliente']}")

            indice_remover = int(input("\nDigite o número da coleta: ")) - 1

            coleta_removida = coletas.pop(indice_remover)

            print(f"\n✅ Coleta do cliente {coleta_removida['cliente']} removida com sucesso!")

    # SAIR
    elif opcao == "4":

        print("\nSistema encerrado.")
        break

    else:
        print("\n❌ Opção inválida.")