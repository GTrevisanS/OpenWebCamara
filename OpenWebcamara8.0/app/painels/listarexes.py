from core.config import PALETA_UTILIZADA, MINHAPASTA, TAMANHO_PADRAO, CLIENTE_X, PASTA_X, MOSTRA_TITULO
from style.style import centraliza, alterarCor as atc, criar_faixa, pause, loading, cls, redimensionar, coletarPaleta
from classes.Files import listarExecutaveisparaPrint
from classes import Exe
CorPri, CorSec, CorTer, CorQua, CorFail, CorSuccess, CorLoading= coletarPaleta(PALETA_UTILIZADA)

def painel_listarexes():
    while True:
        redimensionar()
        cls()
        print(atc("", CorPri))
        if MOSTRA_TITULO == 1:
            print(centraliza(" DEFINA A PASTA EM QUE DESEJA LISTAR OS EXE ABAIXO ","="))
        else:
            print(centraliza("", "="))
        print()
        print(centraliza("Minha Pasta                         DIGITE...    [1]"," "))
        print(centraliza(f"Pasta {CLIENTE_X}                      DIGITE...    [2]"," "))
        print(centraliza("Pasta Personalizada                 DIGITE...    [3]"," "))
        print()
        print(centraliza(atc("Busca filtrada na minha pasta       DIGITE...    [B]", CorSec)," "))
        print(centraliza(atc("Voltar ao painel                    DIGITE...    [X]", CorQua)," "))
        print(atc("", CorPri))
        print(criar_faixa("="))

        QUAL = input("\n> ").lower().strip()

        if QUAL == "x":
            break
        if QUAL == "1":
            P = MINHAPASTA
            inicio = ""
        elif QUAL == "2":
            P = PASTA_X
            inicio = ""
        elif QUAL == "3":
            P = input("\n Digite o caminho da pasta que deseja listar: ").strip()
            inicio = ""
        elif QUAL == "b":
            P = MINHAPASTA
            inicio = input(atc("\n Digite os primeiros números da versão filtrada: ", CorSec)).strip()
        else:
            continue
        lista = listarExecutaveisparaPrint(P, inicio)
        CONTADOR = len(lista)
        redimensionar(CONTADOR + 8)
        if CONTADOR == 0:
            print()
            print(centraliza(atc(" NENHUMA VERSÃO ENCONTRADA !", CorFail)," "))
            pause()
            # IMPORTANTE:
            # volta para o menu deste painel
            continue

        # Exibe resultados
        TAMANHOMAX = 83
        print()
        TITULO = f" ({CONTADOR}) VERSÕES DISPONÍVEIS "
        TITULO = TITULO.center(TAMANHOMAX, "=")
        print(atc(TITULO, CorSuccess))
        print()
        for versao in lista:
            print(atc(f" ➤ {versao}",CorPri))
        print()
        TITULO_PASTA = f" {P} ".center(
            TAMANHOMAX,
            "="
        )
        print(atc(TITULO_PASTA, CorSuccess))
        input("\nPressione ENTER para voltar...")