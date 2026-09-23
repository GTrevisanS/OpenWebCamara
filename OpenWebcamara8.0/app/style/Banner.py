from core.config import CORPADRAO , TEMPO_CARREGA_BANNER as TCB
from style import Style
import time
import os

# Pega a data e hora atual do sistema
tempo_atual = time.localtime()
df = time.strftime("%d/%m/%Y", tempo_atual)

# CORPADRAO = Config.CORPADRAO
# TCB = Config.TEMPO_CARREGA_BANNER
atc = Style.alterar_cor
loading = Style.loading
os.system(CORPADRAO)


bannerp1 = f"""
====================================================================================
    ___                 __        __   _       ____
   / _ \ _ __   ___ _ _ \ \      / /__| |__  /  ___|___  _ __ _    __ _ _ __ __ _
   | | | | '_ \ / _ \ '_ \ \ /\ / / _ \ '_ \| |   / _` | '_ ` _ \ / _` | '__/ _` |
   | |_| | |_) |  __/ | | \ V  V /  __/ |_) | |__| (_| | | | | | | (_| | | | (_| |
   \___/ | .__/ \___|_| |_|\_/\_/ \___|_.__/ \____\__,_|_| |_| |_|\__,_|_|  \__,_|
         |_|
====================================================================================
⠀                                                                        Versão 8.0                                                                                                                               
"""
bannerp2 = f"""        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣏⡦⠤⣤⠽⠤⡄
    ⡴⠋⠙⢦⠀⠀⠀⠀⠀⣀⡤⠤⠣⢈⠇⠀⠁⣠⡿⡄
    ⠀⠀⣠⠏⠀⠀⡠⠂⠉⠀⠀⠀⠀⠀⢀⡀⠈⠀⠀⠈
    ⡴⠋⠀⠀⠀⡔⠀⠀⠀⠀⠀⡀⠀⡰⣯⡀⠀⠀⠀⠀
    ⡇⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⡹⠂⢽⠎⠁⠀⠀⠀⠀
    ⢳⠀⠀⠀ ⠃⣴⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠙⢦⣤⣤⣬⡷⣣⠌⣁⠐⠋{df:>67}                                                     
"""

for caractere in bannerp1:
    print(caractere, end="", flush=True)
    time.sleep(TCB)

for caractere in bannerp2:
    print(atc(caractere, "white", "sim"), end="", flush=True)
    time.sleep(TCB)

loading(atc(' '*80, "white", "nao"))
time.sleep(0.5)