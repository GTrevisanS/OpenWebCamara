from style.style import centraliza, alterar_cor as atc, criar_faixa, pause, loading
from classes import Files, Exe
from core import config

import os

def painel_listarexes():

    MINHAPASTA = config.MINHAPASTA
    TAMANHO_PADRAO = config.TAMANHO_PADRAO
    CLX = config.CLIENTE_X
    PASTA_X = config.PASTA_X

    while True:
        os.system(TAMANHO_PADRAO)
        os.system("cls")
        print(atc("", "cyan", "SIM"))
        if config.MOSTRA_TITULO == 1:
            print(centraliza(
                " DEFINA A PASTA EM QUE DESEJA LISTAR OS EXE ABAIXO ",
                "="
            ))
        else:
            print(centraliza("", "="))

        print()
        print(centraliza("Minha Pasta                         DIGITE...    [1]"," "))
        print(centraliza(f" Pasta {CLX}                      DIGITE...    [2]"," "))
        print(centraliza("Pasta Personalizada                 DIGITE...    [3]"," "))
        print()
        print(centraliza(atc("      Busca filtrada na minha pasta       DIGITE...    [B]","yellow","nao")," "))
        print(centraliza(atc("      Voltar ao painel                    DIGITE...    [X]","black","sim")," "))
        print(atc("", "cyan", "sim"))
        print(criar_faixa("="))

        QUAL = input("\n> ").lower().strip()

        # Voltar
        if QUAL == "x":
            break

        # Define a pasta e o filtro
        if QUAL == "1":

            P = MINHAPASTA
            inicio = ""

        elif QUAL == "2":

            P = PASTA_X
            inicio = ""

        elif QUAL == "3":

            P = input(
                "\n Digite o caminho da pasta que deseja listar: "
            ).strip()

            inicio = ""

        elif QUAL == "b":

            P = MINHAPASTA

            inicio = input(
                atc(
                    "\n Digite os primeiros números da versão filtrada: ",
                    "magenta",
                    "sim"
                )
            ).strip()

        else:
            continue

        # Lista os executáveis
        lista = Files.listar_executaveis_para_print(P, inicio)

        CONTADOR = len(lista)

        os.system(f"mode con: lines={CONTADOR + 8}")

        # Nenhum resultado
        if CONTADOR == 0:

            print()
            print(
                centraliza(
                    atc(
                        " NENHUMA VERSÃO ENCONTRADA !",
                        "RED",
                        "sim"
                    ),
                    " "
                )
            )

            pause()

            # IMPORTANTE:
            # volta para o menu deste painel
            continue

        # Exibe resultados
        TAMANHOMAX = 83

        print()

        TITULO = f" ({CONTADOR}) VERSÕES DISPONÍVEIS "
        TITULO = TITULO.center(TAMANHOMAX, "=")

        print(atc(TITULO, "green", "sim"))
        print()

        for versao in lista:
            print(
                atc(
                    f" ➤ {versao}",
                    "cyan",
                    "sim"
                )
            )

        print()

        TITULO_PASTA = f" {P} ".center(
            TAMANHOMAX,
            "="
        )

        print(
            atc(
                TITULO_PASTA,
                "green",
                "sim"
            )
        )

        input("\nPressione ENTER para voltar...")