import sqlite3

conexao = sqlite3.connect("database/logistica.db")

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

cursor.execute("""

CREATE TABLE IF NOT EXISTS fornecedores (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cnpj TEXT,
    nome TEXT,
    endereco TEXT,
    telefone TEXT

)

""")

conexao.commit()