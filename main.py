import json

import sqlite3

conexao = sqlite3.connect("logistica.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS coletas (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    motorista TEXT,
    placa TEXT,
    veiculo TEXT,
    prioridade TEXT,
    horario TEXT

)
""")

conexao.commit()

try:

    with open("coletas.json", "r", encoding="utf-8") as arquivo:
        coletas = json.load(arquivo)

except FileNotFoundError:

    coletas = []

print("===================================")
print(" SISTEMA DE PROGRAMAÇÃO LOGÍSTICA ")
print("===================================")

# MENU

def mostrar_menu():

    print("\nMENU")
    print("1 - Cadastrar coleta")
    print("2 - Ver programação")
    print("3 - Remover coleta")
    print("4 - Editar coleta")
    print("5 - Buscar coleta")
    print("6 - Estatísticas")
    print("7 - Sair")

# SALVAR AS COLETAS

def salvar_coletas():

    with open("coletas.json", "w", encoding="utf-8") as arquivo_salvo:
        json.dump(coletas, arquivo_salvo, ensure_ascii=False, indent=4)

# EDITAR AS COLETAS

def editar_coleta():

    if len(coletas) == 0:

        print("\n❌ Nenhuma coleta cadastrada.")
        return

    print("\n===== EDITAR COLETA =====")

    for indice_coleta, coleta_atual in enumerate(coletas, start=1):

        print(f"{indice_coleta} - {coleta_atual['cliente']}")

    try:

        indice_editar = int(input("\nDigite o número da coleta: ")) - 1

        coleta_atual = coletas[indice_editar]

        print("\nDigite os novos dados:")

        coleta_atual["cliente"] = input("Cliente: ")
        coleta_atual["motorista"] = input("Motorista: ")
        coleta_atual["placa"] = input("Placa: ")
        coleta_atual["veiculo"] = input("Veículo: ")
        coleta_atual["prioridade"] = input("Prioridade: ")
        coleta_atual["horario"] = input("Horário: ")

        salvar_coletas()

        print("\n✅ Coleta atualizada com sucesso!")

    except ValueError:

        print("\n❌ Digite apenas números.")

    except IndexError:

        print("\n❌ Coleta inexistente.")

# BUSCAR AS COLETAS

def buscar_coleta():

    if len(coletas) == 0:

        print("\n❌ Nenhuma coleta cadastrada.")
        return

    busca = input("\nDigite o nome do cliente: ").lower()

    encontrada = False

    print("\n===== RESULTADO DA BUSCA =====")

    for indice_coleta, coleta_atual in enumerate(coletas, start=1):

        nome_cliente = coleta_atual["cliente"].lower()

        if busca in nome_cliente:

            encontrada = True

            print(f"\n===== COLETA {indice_coleta} =====")
            print("----------------------")
            print(f"Cliente: {coleta_atual['cliente']}")
            print(f"Motorista: {coleta_atual['motorista']}")
            print(f"Placa: {coleta_atual['placa']}")
            print(f"Veículo: {coleta_atual['veiculo']}")
            print(f"Prioridade: {coleta_atual['prioridade']}")
            print(f"Horário: {coleta_atual['horario']}")

    if not encontrada:

        print("\n❌ Nenhuma coleta encontrada.")

# ESTATISTICA

def mostrar_estatisticas():
    if len(coletas) == 0:
        print("\n❌ Nenhuma coleta cadastrada.")
        return

    alta = 0
    media = 0
    baixa = 0

    for coleta_nova in coletas:

        prioridade_contagem = coleta_nova["prioridade"].lower()

        if prioridade_contagem == "alta":

            alta += 1

        elif prioridade_contagem == "media":

            media += 1

        elif prioridade_contagem == "baixa":

            baixa += 1

    print("\n===== ESTATÍSTICAS =====")

    print(f"\nTotal de coletas: {len(coletas)}")
    print(f"Prioridade Alta: {alta}")
    print(f"Prioridade Média: {media}")
    print(f"Prioridade Baixa: {baixa}")


while True:

    mostrar_menu()


    opcao = input("Escolha uma opção: ")

    # CADASTRAR COLETA
    if opcao == "1":

        cliente = input("Cliente: ")
        motorista = input("Motorista: ")
        placa = input("Placa: ")
        veiculo = input("Veículo: ")
        while True:

            print("\nPrioridade:")
            print("1 - Alta")
            print("2 - Média")
            print("3 - Baixa")

            opcao_prioridade = input("Escolha a prioridade: ")

            if opcao_prioridade == "1":

                prioridade = "alta"
                break

            elif opcao_prioridade == "2":

                prioridade = "media"
                break

            elif opcao_prioridade == "3":

                prioridade = "baixa"
                break

            else:

                print("\n❌ Opção inválida.")
        horario = input("Horário: ")

        coleta = {
            "cliente": cliente,
            "motorista": motorista,
            "placa": placa,
            "veiculo": veiculo,
            "prioridade": prioridade,
            "horario": horario
        }

        coletas.append(coleta)

        salvar_coletas()

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

            try:

                indice_remover = int(input("\nDigite o número da coleta: ")) - 1

                coleta_removida = coletas.pop(indice_remover)

                salvar_coletas()

                print(f"\n✅ Coleta do cliente {coleta_removida['cliente']} removida com sucesso!")

            except ValueError:

                print("\n❌ Digite apenas números.")

            except IndexError:

                print("\n❌ Coleta inexistente.")

    # EDITAR COLETA

    elif opcao == "4":

        editar_coleta()

    # BUSCAR COLETA

    elif opcao == "5":

        buscar_coleta()

    # ESTATISTICAS

    elif opcao == "6":

        mostrar_estatisticas()

    # SAIR

    elif opcao == "7":

        print("\nSistema encerrado.")
        break

    else:
        print("\n❌ Opção inválida.")