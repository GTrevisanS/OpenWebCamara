from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = BASE_DIR / "data" / "conexoes.json"

# Caso o arquivo não exista, cria ele por questão de tratativa de erro
if not os.path.exists(ARQUIVO_JSON):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump({}, f, indent=4)

# Carrega o JSON
with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
    conexoes = json.load(f)

def coletar_info():
    disponiveis = []
    for indice, conexao in conexoes.items():
        disponiveis.append(conexao["NOME"])
    return disponiveis

disponiveis = coletar_info() # Coleto todas as informações em formato de lista

def editar_json(id_conexao, campo, subcampo, novo_valor):
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        dados = json.load(f)
    if not subcampo:
        dados[id_conexao][campo] = novo_valor
    else:
        dados[id_conexao][campo][subcampo] = novo_valor
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
