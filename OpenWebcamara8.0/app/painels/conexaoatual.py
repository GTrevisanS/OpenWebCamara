from style.style import centraliza, pause, coletarPaleta, alterarCor as atc, cls, calcularEspaco
from core.config import PALETA_UTILIZADA, CONFIG_INI, LAST_ACCESS, MINHAPASTA, MOSTRA_TITULO
from classes import Files

CorQua, CorFail, CorSuccess, CorLoading = coletarPaleta(PALETA_UTILIZADA, 'tratativas')

def painel_conexaoatual():
    ip, db, dbf, porta = Files.checarConexaoAtual(CONFIG_INI, 4)
    EXE = Files.checarConexaoAtual(LAST_ACCESS, 1)
    EXE = EXE.replace(f"{str(MINHAPASTA)}","").replace("\\","")
    cls()
    print(atc("", CorSuccess))
    if MOSTRA_TITULO:
        print(centraliza(" CONEXÃO ATUAL DA SUA PASTA ABAIXO ", "="))
        print()
    else:
        print(centraliza("", "="))

    limite = 35

    espaco1 = calcularEspaco(ip, limite)
    espaco2 = calcularEspaco(db, limite)
    espaco3 = calcularEspaco(dbf, limite)
    espaco4 = calcularEspaco(porta, limite)
    espaco5 = calcularEspaco(EXE, limite)

    print("")
    print(centraliza(f"IP:                 {espaco1}{ip}", " "))
    print(centraliza(f"DB1:                {espaco2}{db}", " "))
    print(centraliza(f"DB2:                {espaco3}{dbf}", " "))
    print(centraliza(f"PORTA:              {espaco4}{porta}", " "))
    print(atc("", CorQua))
    print(centraliza(f"Último EXE acessado:{espaco5}{EXE}", " "))
    print(atc("", CorSuccess))
    if MOSTRA_TITULO:
        print()
        print(centraliza(f" {MINHAPASTA} ", "="))
    else:
        print(centraliza("", "="))
    pause()
    return