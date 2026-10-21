import json

def abrirJson(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def editarJson(caminho, chave, novo_valor):
    configuracoes = abrirJson(caminho)
    configuracoes[chave] = novo_valor

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(configuracoes, arquivo, indent=4, ensure_ascii=False)