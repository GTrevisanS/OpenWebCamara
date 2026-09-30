from style.style import centraliza, pause
from classes import Files
from core import config
import os

def painel_conexaoatual():
    CONFIG_INI = config.CONFIG_INI
    LAST_ACCESS = config.LAST_ACCESS
    MINHAPASTA = config.MINHAPASTA
    
    ip, db, dbf, porta = Files.ver_conexao_atual(CONFIG_INI, 4)
    EXE = Files.ver_conexao_atual(LAST_ACCESS, 1)
    EXE = EXE.replace(f"{str(MINHAPASTA)}","").replace("\\","")

    os.system("cls")
    os.system("color 0A")

    print()
    if config.MOSTRA_TITULO == 1:
        print(centraliza(" CONEXÃO ATUAL DA SUA PASTA ABAIXO ", "="))
        print()
    else:
        print(centraliza("", "="))
    print("")
    print(f"            IP:                             {ip}")
    print(f"            DB1:                            {db}")
    print(f"            DB2:                            {dbf}")
    print(f"            PORTA:                          {porta}")
    print()
    print(f"            Último EXE acessado:            {EXE}")
    print("")
    if config.MOSTRA_TITULO == 1:
        print()
        print(centraliza(f" {MINHAPASTA} ", "="))
    else:
        print(centraliza("", "="))
    pause()
    return