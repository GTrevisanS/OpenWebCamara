
from core.config import CORPADRAO, TEMPO_CARREGA_BANNER, TEMPO_LOADING_PADRAO, HOJE, PALETA_UTILIZADA, COLUNAS
from style.style import alterarCor as atc, loading, cls, coletarPaleta, criar_faixa, centralizarBanner, redimensionar
import time, os

CorPri, CorSec, CorTer, CorQua = coletarPaleta(PALETA_UTILIZADA, 'principais')

def animar(texto):
    for caractere in texto:
        print(caractere, end="", flush=True)
        time.sleep(TEMPO_CARREGA_BANNER)

faixa = "=" * COLUNAS

parte1 = f"""
     ___                 __        __   _       ____
    / _ \ _ __   ___ _ _ \ \      / /__| |__  /  ___|___  _ __ _    __ _ _ __ __ _
    | | | | '_ \ / _ \ '_ \ \ /\ / / _ \ '_ \| |   / _` | '_ ` _ \ / _` | '__/ _` |
    | |_| | |_) |  __/ | | \ V  V /  __/ |_) | |__| (_| | | | | | | (_| | | | (_| |
    \___/ | .__/ \___|_| |_|\_/\_/ \___|_.__/ \____\__,_|_| |_| |_|\__,_|_|  \__,_|
          |_|
⠀                                                                        Versão 8.3
"""


parte2 = f"""        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣏⡦⠤⣤⠽⠤⡄
    ⡴⠋⠙⢦⠀⠀⠀⠀⠀⣀⡤⠤⠣⢈⠇⠀⠁⣠⡿⡄
    ⠀⠀⣠⡏⠀⠀⡠⠂⠉⠀⠀⠀⠀⠀⢀⡀⠈⠀⠀⠈
    ⡴⠋⠀⠀⠀⡔⠀⠀⠀⠀⠀⡀⠀⡰⣯⡀⠀⠀⠀⠀
    ⡇⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⡹⠂⢽⠎⠁⠀⠀⠀⠀
    ⢳⠀⠀⠀ ⠃⣴⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠙⢦⣤⣤⣬⡷⣣⠌⣁⠐⠋{HOJE:>{COLUNAS - 20}}
"""

parte1 = centralizarBanner(parte1)
# parte2 = centralizarBanner(parte2)

redimensionar()
cls()

print(atc("\n", CorPri), end="", flush=True)

animar(faixa)

for caractere in parte1:
    print(caractere, end="", flush=True)
    time.sleep(TEMPO_CARREGA_BANNER)

animar(faixa)

print(atc(" ", CorSec))

for caractere in parte2:
    print(caractere, end="", flush=True)
    time.sleep(TEMPO_CARREGA_BANNER)

time.sleep(TEMPO_LOADING_PADRAO)
