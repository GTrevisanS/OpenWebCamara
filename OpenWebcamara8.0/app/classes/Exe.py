from pathlib import Path
from style.style import alert, alterarCor as atc, coletarPaleta
from core.config import PALETA_UTILIZADA

CorPri, CorSec, CorTer, CorQua = coletarPaleta(PALETA_UTILIZADA, 'principais')

def listarExecutaveis(pasta, sistema=None):
    if sistema:
        sistema = f"*{str(sistema)}*.exe"
    else:
        sistema = "WebCamara*.exe"
    executaveis = sorted(
        Path(pasta).glob(sistema),
        key=lambda arquivo: arquivo.stat().st_mtime,
        reverse=True
    )
    return executaveis

def procurarUltimoExe(pasta, sistema=None):
    if sistema:
        lista = listarExecutaveis(pasta, sistema)
    else:
        lista = listarExecutaveis(pasta)
    if  len(lista) < 1:
        print("\n Nenhum Executável encontrado.")
        return
    return lista[0]

def procurarExeManualmente(pasta, versaoescolhida=None, numeroescolhido=None):
    # Se não recebeu os valores, solicita ao usuário (So recebe o executável quando é uma fastconection)
    if not versaoescolhida and not numeroescolhido:
        while True:
            versao = input(atc("\n Versão: ", CorSec)).replace(" ", "")
            if versao == "":
                alert(" DIGITE UMA VERSÃO VÁLIDA!")
                continue
            if versao.count(".") == 0:
                versao = versao[0] + "." + versao[1:]
            numero = input(" Executável: ").replace(" ", "")
            if not numero.isdigit() or not versao.replace(".", "").isdigit():
                alert(" Os campos devem conter somente números e correlatos! (sem letras ou campos vazios)")
                continue
            break
    else:
        versao = str(versaoescolhida).replace(" ", "")
        numero = "" if numeroescolhido is None else str(numeroescolhido).replace(" ", "")
    candidatos = [
        Path(pasta) / f"WebCamara {versao}({numero}).exe",
        Path(pasta) / f"WebCamara {versao} ({numero}).exe",
    ]
    # Caso seja sem número ou número 1, também procura pelo executável sem sufixo
    if numero == "" or (numero.isdigit() and int(numero) <= 1):
        candidatos.append(Path(pasta) / f"WebCamara {versao}.exe")
    for candidato in candidatos:
        if candidato.exists():
            return candidato

    alert(" Executável não encontrado! (Tente novamente ou verifique a sua pasta)")
    # Se os dados vieram por parâmetro, encerra a função.
    if versaoescolhida or numeroescolhido:
        return None
    # Caso contrário, tenta novamente.
    return procurarExeManualmente(pasta)