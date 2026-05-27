import requests
from typing import Optional


def consultar_cnpj(cnpj) -> Optional[dict]:

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