from style.style import centraliza, pause, coletarPaleta, alterarCor as atc, cls
from core.config import PALETA_UTILIZADA, CONFIG_INI, LAST_ACCESS, MINHAPASTA, MOSTRA_TITULO
from classes import Files

CorQua, CorFail, CorSuccess, CorLoading = coletarPaleta(PALETA_UTILIZADA, 'tratativas')

def painel_conexaoatual():
    ip, db, dbf, porta = Files.checarConexaoAtual(CONFIG_INI, 4)
    EXE = Files.checarConexaoAtual(LAST_ACCESS, 1)
    EXE = EXE.replace(f"{str(MINHAPASTA)}","").replace("\\","")
    cls()
    print(atc("", CorSuccess))
    if MOSTRA_TITULO == 1:
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
    if MOSTRA_TITULO == 1:
        print()
        print(centraliza(f" {MINHAPASTA} ", "="))
    else:
        print(centraliza("", "="))
    pause()
    return