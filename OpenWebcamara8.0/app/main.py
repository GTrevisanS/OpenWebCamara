from core.config import PALETA_UTILIZADA, LAST_ACCESS, MINHAPASTA, PASTA_X, CLIENTE_X, USUARIOWEBCAM, SENHAWEBCAM, USA_BANNER, MOSTRA_TITULO
from style.style import loading, centraliza, alterarCor as atc, criar_faixa, pause, alert, redimensionar, cls, coletarPaleta
from core.login import executarLogin
from classes import Exe, Files
import random, time, sys, os, subprocess
from pathlib import Path

CorPri, CorSec, CorTer, CorQua = coletarPaleta(PALETA_UTILIZADA, 'principais')

if USA_BANNER == 1: # Se a configuração definir que o banner deve ser chamado, ele executa
    from style import banner

def painel():
    from core.config import IP, DB, DBF, PORTA
    while True:
        redimensionar()
        cls()
        print(atc("", CorPri))
        print(criar_faixa("="))
        print()
        if MOSTRA_TITULO == 1:
            print(centraliza("DEFINA QUE TIPO DE AÇÃO VOCÊ DESEJA REALIZAR PELO PAINEL"," "))
            print()
        print(centraliza("WebCamara Homologacão              DIGITE...        [1]"," "))
        print(centraliza("Conexão rápida                     DIGITE...        [2]"," "))
        print(centraliza("Conexão Personalizada              DIGITE...        [3]"," "))
        print(centraliza("WebCamara cliente X                DIGITE...        [4]"," "))
        print(centraliza("Verificar Conexão atual            DIGITE...        [0]"," "))
        print()
        print(centraliza(atc('"Fast-Conections"                  DIGITE...        [F]', CorSec)," "))
        print(centraliza(atc('Abrir minha pasta                  DIGITE...        [P]', CorTer)," "))
        print(centraliza(atc('Listar todos os EXE´s              DIGITE...        [E]', CorQua)," "))
        print(centraliza(atc('Rodar WebUpload                    DIGITE...        [W]', CorQua)," "))
        print(atc('', CorPri))
        print(criar_faixa("="))
        RESPOSTA = input("\n> ")
        RESPOSTA = str(RESPOSTA).lower().strip()
        match RESPOSTA:
            case "1":
                Files.alterarConexao(IP,DB,DBF,PORTA)
                print()
                loading(" Abrindo versão mais recente de Homologação")
                time.sleep(2)
                EXE = Exe.procurarUltimoExe(MINHAPASTA)
                executarLogin(USUARIOWEBCAM, SENHAWEBCAM, EXE)
            case "2":
                PERGUNTA = input(atc("\n Deseja escolher o Executável? [S/N]: ", CorSec)).strip().lower()
                match PERGUNTA:
                    case "s":
                        EXE = Exe.procurarExeManualmente(MINHAPASTA, "", "")
                        if EXE:
                            Files.alterarArquivo(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
                            executarLogin(USUARIOWEBCAM, SENHAWEBCAM, EXE)
                        else:
                            painel()
                    case "n":
                        EXE = Exe.procurarUltimoExe(MINHAPASTA)
                        Files.alterarArquivo(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
                        executarLogin(USUARIOWEBCAM, SENHAWEBCAM, EXE)
                    case _:
                        alert('\n RESPONDA SOMENTE "S" OU "N" ')
                        painel()
            case "3":
                cls()
                print(atc("", CorSec))
                print(centraliza(' CONEXÃO PERSONALIZADA SELECIONADA ','='))
                print()
                IP = input("\n> IP: ").replace(" ","")
                PORTA = input("> PORTA: ").replace(" ","")
                DB = input("\n> BANCO REGISTROS: ").replace(" ","").lower()
                if "webcamara" not in DB:
                    print(atc('\n Opa, parece que seu banco não começa com "webcamara", tem certeza?! \n', CorTer))
                DBF = input(atc("> BANCO ARQUIVOS: ", CorSec)).replace(" ","").lower()
                print()
                if IP == "" or PORTA == "" or DB == "" or DBF == "":
                    alert(" Ops, algum campo ficou vazio!")
                Files.alterarConexao(IP,DB,DBF,PORTA) # Caso nao haja erro, altera a conexão na pasta pessoal
                EXE = Exe.procurarExeManualmente(MINHAPASTA, "", "")
                Files.alterarArquivo(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
                executarLogin(USUARIOWEBCAM, SENHAWEBCAM, EXE)
            case "4":
                pergunta = input("\n Deseja escolher a versão? [S/N]: ")
                pergunta = pergunta.strip().lower()
                if pergunta == "s":
                    EXE = Exe.procurarExeManualmente(PASTA_X, "", "")
                    print()
                    loading(f" Abrindo versão digitada na pasta de {CLIENTE_X}")
                    executarLogin(USUARIOWEBCAM, SENHAWEBCAM, EXE)
                else: 
                    EXE = Exe.procurarUltimoExe(PASTA_X)
                    print()
                    loading(f" Abrindo versão mais recente de {CLIENTE_X}")
                    executarLogin(USUARIOWEBCAM, SENHAWEBCAM, EXE)
            case "0":
                from painels.conexaoatual import painel_conexaoatual
                painel_conexaoatual()
            case "e":
                from painels.listarexes import painel_listarexes
                painel_listarexes()
            case "w":
                EXE = str(Exe.procurarUltimoExe(MINHAPASTA, "Webupload"))
                PEXE = str(EXE).replace(MINHAPASTA, "").replace(PASTA_X, "").replace("\\", "")
                print(atc(f"\n Caminho encontrado: {PEXE}", CorTer))
                time.sleep(2)
                os.system(f'start "" {EXE}')
            case "f":
                from painels.fastconections import painel_fastconections
                painel_fastconections()
            case "p":
                print()
                Files.AbrirMinhaPasta()
            case _:
                continue
painel()