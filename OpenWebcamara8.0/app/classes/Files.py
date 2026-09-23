from pathlib import Path
from core import config

MINHAPASTA = config.MINHAPASTA
CONFIG_INI = Path(MINHAPASTA) / "configuracao.ini"
ENDERECO_INI = Path(MINHAPASTA) / "endereco_ip_servidor.ini"

def ver_conexao_atual(arquivo, linhas):
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

def alterar_arquivo(caminho, ip, db, dbf, porta):
    
    with open(caminho, encoding="cp1252") as arquivo:
        linhas = arquivo.readlines()

    linhas[0] = ip + "\n"
    linhas[1] = db + "\n"
    linhas[2] = dbf + "\n"
    linhas[3] = porta + "\n"
    
    with open(caminho, "w", encoding="cp1252") as arquivo:
        arquivo.writelines(linhas)

def alterar_conexao(ip, db, dbf, porta):
    alterar_arquivo(CONFIG_INI, ip, db, dbf, porta)
    alterar_arquivo(ENDERECO_INI, ip, db, dbf, porta)
    print("\n Arquivos atualizados com sucesso!\n")

def listar_executaveis_para_print(pasta, inicio):
    if inicio:
        padrao = f"WebCamara*{str(inicio)}*.exe"
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