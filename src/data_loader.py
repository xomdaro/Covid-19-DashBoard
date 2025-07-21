import pandas as pd
import requests
import os

def baixar_dados(url, arquivo):
    if not os.path.exists(arquivo):
        print("Baixando dados do servidor...")
        response = requests.get(url)
        with open(arquivo, 'wb') as f:
            f.write(response.content)
        print("Download concluído.")
    else:
        print("Dados já existem, pulando download.")

def carregar_dados(caminho):
    print("Carregando dados...")
    df = pd.read_csv(caminho)
    return df