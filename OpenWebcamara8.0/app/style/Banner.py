from core.config import CORPADRAO , TEMPO_CARREGA_BANNER ,HOJE , PALETA_UTILIZADA
from style.style import alterarCor as atc, loading, cls, coletarPaleta
import time, os

CorPri, CorSec, CorTer, CorQua = coletarPaleta(PALETA_UTILIZADA, 'principais')
parte1 = f"""
=======================================================================================
     ___                 __        __   _       ____
    / _ \ _ __   ___ _ _ \ \      / /__| |__  /  ___|___  _ __ _    __ _ _ __ __ _
    | | | | '_ \ / _ \ '_ \ \ /\ / / _ \ '_ \| |   / _` | '_ ` _ \ / _` | '__/ _` |
    | |_| | |_) |  __/ | | \ V  V /  __/ |_) | |__| (_| | | | | | | (_| | | | (_| |
    \___/ | .__/ \___|_| |_|\_/\_/ \___|_.__/ \____\__,_|_| |_| |_|\__,_|_|  \__,_|
          |_|
=======================================================================================
⠀                                                                          Versão 8.2                                                                                                                               
"""
part2 = f"""        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣏⡦⠤⣤⠽⠤⡄
    ⡴⠋⠙⢦⠀⠀⠀⠀⠀⣀⡤⠤⠣⢈⠇⠀⠁⣠⡿⡄
    ⠀⠀⣠⠏⠀⠀⡠⠂⠉⠀⠀⠀⠀⠀⢀⡀⠈⠀⠀⠈
    ⡴⠋⠀⠀⠀⡔⠀⠀⠀⠀⠀⡀⠀⡰⣯⡀⠀⠀⠀⠀
    ⡇⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⡹⠂⢽⠎⠁⠀⠀⠀⠀
    ⢳⠀⠀⠀ ⠃⣴⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠙⢦⣤⣤⣬⡷⣣⠌⣁⠐⠋{HOJE:>67}                                                     
"""

print(atc(" ", CorPri))
cls()
for caractere in parte1:
    print(caractere, end="", flush=True)
    time.sleep(TEMPO_CARREGA_BANNER)

print(atc(" ", CorSec))
for caractere in part2:
    print(caractere, end="", flush=True)
    time.sleep(TEMPO_CARREGA_BANNER)

# loading(' '*80)
time.sleep(0.7)