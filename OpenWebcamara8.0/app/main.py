from core import config
from style.style import loading, centraliza, alterar_cor as atc, criar_faixa, pause, alert
from core.login import executar_login
from classes import Exe, Files
import random, time, sys, os, subprocess
from pathlib import Path

if config.USA_BANNER == 1: # Se a configuração definir que o banner deve ser chamado, ele executa
    from style import banner

def painel():
    LAST_ACCESS = config.LAST_ACCESS
    CORPADRAO = config.CORPADRAO
    TAMANHO_PADRAO = config.TAMANHO_PADRAO
    MINHAPASTA = config.MINHAPASTA
    PASTA_X = config.PASTA_X
    USUARIOWEBCAM = config.USUARIOWEBCAM
    SENHAWEBCAM = config.SENHAWEBCAM
    IP = config.IP
    DB = config.DB
    DBF = config.DBF
    PORTA = config.PORTA
    CLX = config.CLIENTE_X
    
    while True:
        os.system(CORPADRAO)
        os.system(TAMANHO_PADRAO)
        os.system("cls")
        print()
        print(criar_faixa("="))
        print()
        if config.MOSTRA_TITULO == 1:
            print(centraliza("DEFINA QUE TIPO DE AÇÃO VOCÊ DESEJA REALIZAR PELO PAINEL"," "))
            print()
        print(centraliza("WebCamara Homologacão              DIGITE...        [1]"," "))
        print(centraliza("Conexão rápida                     DIGITE...        [2]"," "))
        print(centraliza("Conexão Personalizada              DIGITE...        [3]"," "))
        print(centraliza("WebCamara cliente X                DIGITE...        [4]"," "))
        print(centraliza("Verificar Conexão atual            DIGITE...        [0]"," "))
        print()
        print(centraliza(atc('    "Fast-Conections"                  DIGITE...        [F]',"yellow", "nao")," "))
        print(centraliza(atc('    Abrir minha pasta                  DIGITE...        [P]',"blue", "sim")," "))
        print(centraliza(atc('     Listar todos os EXE´s              DIGITE...        [E]',"black", "sim")," "))
        print(centraliza(atc('     Rodar WebUpload                    DIGITE...        [W]',"black", "sim")," "))
        print(atc('',"cyan", "sim"))
        print(criar_faixa("="))
        RESPOSTA = input("\n> ")
        RESPOSTA = str(RESPOSTA).lower().strip()
        match RESPOSTA:
            case "1":
                Files.alterar_conexao(IP,DB,DBF,PORTA)
                print()
                loading(" Abrindo versão mais recente de Homologação")
                time.sleep(2)
                EXE = Exe.procurar_ultimo_EXE(MINHAPASTA)
                executar_login(USUARIOWEBCAM, SENHAWEBCAM, EXE)
            case "2":
                PERGUNTA = input(atc("\n Deseja escolher o Executável? [S/N]: ", "yellow", "nao")).strip().lower()
                match PERGUNTA:
                    case "s":
                        EXE = Exe.procurar_exe_manual(MINHAPASTA, "", "")
                        if EXE:
                            Files.alterar_arquivo(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
                            executar_login(USUARIOWEBCAM, SENHAWEBCAM, EXE)
                        else:
                            painel()
                    case "n":
                        EXE = Exe.procurar_ultimo_EXE(MINHAPASTA)
                        Files.alterar_arquivo(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
                        executar_login(USUARIOWEBCAM, SENHAWEBCAM, EXE)
                    case _:
                        alert('\n RESPONDA SOMENTE "S" OU "N" ')
                        painel()
            case "3":
                os.system("cls")
                print(atc("", "yellow", "nao"))
                print(centraliza(' CONEXÃO PERSONALIZADA SELECIONADA ','='))
                print()
                IP = input("\n> IP: ").replace(" ","")
                PORTA = input("> PORTA: ").replace(" ","")
                DB = input("\n> BANCO REGISTROS: ").replace(" ","").lower()
                if "webcamara" not in DB:
                    print(atc('\n Opa, parece que seu banco não começa com "webcamara", tem certeza?! \n', 'blue', 'sim'))
                DBF = input(atc("> BANCO ARQUIVOS: ", "yellow", "nao")).replace(" ","").lower()
                print()
                if IP == "" or PORTA == "" or DB == "" or DBF == "":
                    alert(" Ops, algum campo ficou vazio!")
                Files.alterar_conexao(IP,DB,DBF,PORTA) # Caso nao haja erro, altera a conexão na pasta pessoal
                EXE = Exe.procurar_exe_manual(MINHAPASTA, "", "")
                Files.alterar_arquivo(LAST_ACCESS, str(EXE), "", "Na linha acima esta o ultimo EXE aberto!", "")
                executar_login(USUARIOWEBCAM, SENHAWEBCAM, EXE)
            case "4":
                pergunta = input("\n Deseja escolher a versão? [S/N]: ")
                pergunta = pergunta.strip().lower()
                if pergunta == "s":
                    EXE = Exe.procurar_exe_manual(PASTA_X, "", "")
                    print()
                    loading(f" Abrindo versão digitada na pasta de {CLX}")
                    executar_login(USUARIOWEBCAM, SENHAWEBCAM, EXE)
                else: 
                    EXE = Exe.procurar_ultimo_EXE(PASTA_X)
                    print()
                    loading(f" Abrindo versão mais recente de {CLX}")
                    executar_login(USUARIOWEBCAM, SENHAWEBCAM, EXE)
            case "0":
                from painels.conexaoatual import painel_conexaoatual
                painel_conexaoatual()
            case "e":
                from painels.listarexes import painel_listarexes
                painel_listarexes()
            case "w":
                EXE = str(Exe.procurar_ultimo_EXE(MINHAPASTA, "Webupload"))
                PEXE = str(EXE).replace(MINHAPASTA, "").replace(PASTA_X, "").replace("\\", "")
                print(atc(f"\n Caminho encontrado: {PEXE}", "blue", "sim"))
                time.sleep(2)
                Exe.somente_abrir_exe(EXE)
            case "f":
                from painels.fastconections import painel_fastconections
                painel_fastconections()
            case "p":
                print()
                loading(f' Abrindo "{MINHAPASTA}" ')
                time.sleep(0.5)
                os.startfile(MINHAPASTA)
                painel()
            case _:
                continue


painel()