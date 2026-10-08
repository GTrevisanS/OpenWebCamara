from pathlib import Path
from core.config import CONFIG_INI, ENDERECO_INI, MINHAPASTA
from style.style import loading
import time, os

def checarConexaoAtual(arquivo, linhas):
    if linhas == 4:
        with open(arquivo, encoding="cp1252") as arquivo:
            linhas = arquivo.read().splitlines()
        return linhas[0], linhas[1], linhas[2], linhas[3]
    elif linhas == 1:
        with open(arquivo, encoding="cp1252") as arquivo:
            linhas = arquivo.read().splitlines()
        return linhas[0]
    else:
        print("\n Você esqueceu de definir as linhas!")
        pause()

def alterarArquivo(caminho, ip, db, dbf, porta):
    with open(caminho, encoding="cp1252") as arquivo:
        linhas = arquivo.readlines()
    linhas[0] = ip + "\n"
    linhas[1] = db + "\n"
    linhas[2] = dbf + "\n"
    linhas[3] = porta + "\n"
    with open(caminho, "w", encoding="cp1252") as arquivo:
        arquivo.writelines(linhas)

def alterarConexao(ip, db, dbf, porta):
    alterarArquivo(CONFIG_INI, ip, db, dbf, porta)
    alterarArquivo(ENDERECO_INI, ip, db, dbf, porta)
    print("\n Arquivos atualizados com sucesso!")

def listarExecutaveisparaPrint(pasta, filtro=None):
    if filtro:
        padrao = f"WebCamara*{str(filtro)}*.exe"
    else:
        padrao = "WebCamara*.exe"

    executaveis = sorted(
        Path(pasta).glob(padrao),
        key=lambda arquivo: arquivo.stat().st_mtime,
        reverse=True
    )
    lista_exe = [arquivo.name for arquivo in executaveis]
    versoes = []
    for item in lista_exe:
        item = str(item).lower().replace('webcamara','').replace('.exe','').strip()
        versoes.append(item)
    return versoes

def AbrirMinhaPasta():
    loading(f' Abrindo "{MINHAPASTA}" ')
    time.sleep(0.5)
    os.startfile(MINHAPASTA)