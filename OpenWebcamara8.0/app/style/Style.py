from core.config import PALETA_UTILIZADA, TEMPO_LOADING_PADRAO, TAMANHO_PADRAO
from pathlib import Path
import itertools, json, time, sys, re, os

# ====================================== PALETAS DE CORES =======================================

pastaPrincipal = Path(__file__).resolve().parent.parent
paletas = pastaPrincipal / "style" / "palettes.json"
with open(paletas, "r", encoding="utf-8") as p:
    arquivoPaletas = json.load(p)

def coletarPaleta(selecionado, quantidade=None):
    paleta = arquivoPaletas.get(str(selecionado))
    if paleta is None or paleta == "":
        print("Erro ao coletar a paleta, trocando para principal...")
        paleta = arquivoPaletas.get("principal")
    if quantidade:
        match quantidade.strip().lower():
            case 'principais':
                CorPri = paleta["primary"]
                CorSec = paleta["secundary"]
                CorTer = paleta["tertiary"]
                CorQua = paleta["quaternary"]
                return CorPri, CorSec, CorTer, CorQua
            case 'tratativas':
                CorQua = paleta["quaternary"]
                CorFail = paleta["alerts"]["fail"]
                CorSuccess = paleta["alerts"]["success"]
                CorLoading = paleta["alerts"]["loading"]
                return CorQua, CorFail, CorSuccess, CorLoading
            case _:
                pass
    else:
        CorPri = paleta["primary"]
        CorSec = paleta["secundary"]
        CorTer = paleta["tertiary"]
        CorQua = paleta["quaternary"]
        CorQua = paleta["quaternary"]
        CorFail = paleta["alerts"]["fail"]
        CorSuccess = paleta["alerts"]["success"]
        CorLoading = paleta["alerts"]["loading"]
    return CorPri, CorSec, CorTer, CorQua, CorFail, CorSuccess, CorLoading

# ==============================================================================================


CorQua, CorFail, CorSuccess, CorLoading = coletarPaleta(PALETA_UTILIZADA, 'tratativas')


def alterarCor(texto, cor):
    cor = cor.lstrip("#")
    r = int(cor[0:2], 16)
    g = int(cor[2:4], 16)
    b = int(cor[4:6], 16)
    # \033[0m = reset das configurações do terminal
    return f"\033[38;2;{r};{g};{b}m{texto}"


def centraliza(texto, caractere):
    if not texto:
        texto = str(caractere)
    # Remove ANSI somente para calcular o tamanho
    texto_limpo = re.sub(r'\033\[[0-9;]*m', '', texto)
    espacos = 87 - len(texto_limpo)
    if espacos <= 0:
        return texto
    esquerda = espacos // 2
    direita = espacos - esquerda
    return (caractere * esquerda) + texto + (caractere * direita)


def loading(texto="Carregando", duracao=TEMPO_LOADING_PADRAO): # Função usada para criar efeito de carregamento visual no terminal
    inicio = time.time()
    for simbolo in itertools.cycle("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"):
        if time.time() - inicio >= duracao:
            break
        sys.stdout.write(alterarCor(f"\r{texto} {simbolo}", CorQua))
        sys.stdout.flush()
        time.sleep(0.07)
    texto = (f"\r{texto} ✔")
    print(alterarCor(texto, CorSuccess))


def criar_faixa(caractere):
    caractere = str(caractere)
    faixa = caractere.center(87, caractere) 
    return faixa


def redimensionar(linhas=None, colunas=None):
    if linhas and colunas:
         os.system(f"mode con: cols={colunas} lines={linhas}")
    elif linhas:
         os.system(f"mode con: lines={linhas}")
    elif colunas:
         os.system(f"mode con: cols={colunas}")
    else:
        os.system(TAMANHO_PADRAO)

def pause():  # Função para pausar processos
    input(alterarCor("\nPressione ENTER para continuar...", CorQua))

def alert(texto): # Função para dar alerta / usada na tratativa de erro
    input(alterarCor(f"{texto}\n",CorSuccess))

def cls(): # Função para limpar o terminal
    os.system('cls')