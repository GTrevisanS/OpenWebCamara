from classes import Exe, Files
from core import config
from core.Login import executar_login
from style import Style
import random
import time
import sys
import os
from pathlib import Path
import subprocess

if config.USA_BANNER == 1: # Se a configuração definir que o banner deve ser chamado, ele executa
    from style import Banner

from dotenv import load_dotenv
load_dotenv(dotenv_path='data/.env') # Puxo os dados da env

BASE_DIR = Path(__file__).resolve().parent.parent
LAST_ACCESS = BASE_DIR / "app" / "data" / "last_access.txt"
MINHAPASTA = config.MINHAPASTA
PASTA_X = config.PASTA_X

USUARIOWEBCAM = os.getenv('USUARIOWEBCAM')
SENHAWEBCAM = os.getenv('SENHAWEBCAM')
IP = os.getenv('IP')
DB = os.getenv('DB')
DBF = os.getenv('DBF')
PORTA = os.getenv('PORTA')

atc = Style.alterar_cor
loading = Style.loading
centraliza = Style.centraliza
criar_faixa = Style.criar_faixa
pause = Style.pause
alert = Style.alert


def painel():
    LAST_ACCESS = BASE_DIR / "app" / "data" / "last_access.txt"
    CORPADRAO = config.CORPADRAO
    TAMANHO_PADRAO = config.TAMANHO_PADRAO
    os.system(CORPADRAO)
    os.system(TAMANHO_PADRAO)
    MINHAPASTA = config.MINHAPASTA
    PASTA_X = config.PASTA_X
    CONFIG_INI = Path(MINHAPASTA) / "configuracao.ini"
    ENDERECO_INI = Path(MINHAPASTA) / "endereco_ip_servidor.ini"
    USUARIOWEBCAM = os.getenv('USUARIOWEBCAM')
    SENHAWEBCAM = os.getenv('SENHAWEBCAM')
    IP = os.getenv('IP')
    DB = os.getenv('DB')
    DBF = os.getenv('DBF')
    PORTA = os.getenv('PORTA')
    CLX = config.CLIENTE_X



    os.system("cls")
    print()
    print(criar_faixa("="))
    print()
    if config.MOSTRA_TITULO == 1:
        print(centraliza("DEFINA QUE TIPO DE AÇÃO VOCÊ DESEJA REALIZAR PELO PAINEL"," "))
        print()
    print(centraliza("WebCamara Homologacão              DIGITE...        [1]"," "))
    print(centraliza("Conexão rápida (apenas abrir)      DIGITE...        [2]"," "))
    print(centraliza("Conexão Personalizada              DIGITE...        [3]"," "))
    print(centraliza(f"WebCamara {CLX}                 DIGITE...        [4]"," "))
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
                painel() # Retorna ao painel se algum dos 4 campos dos arquivos estiver vazio
    
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
            painel() 
        case "e":
            while True:
                os.system("cls")
                print()
                if config.MOSTRA_TITULO == 1:
                    print(centraliza(" DEFINA A PASTA EM QUE DESEJA LISTAR OS EXE ABAIXO ", "="))
                else:
                    print(centraliza("", "="))
                print("")
                print(centraliza("Minha Pasta                         DIGITE...    [1]", " "))
                print(centraliza(f"Pasta {CLX}                      DIGITE...    [2]", " "))
                print(centraliza("Pasta Personalizada                 DIGITE...    [3]", " "))
                print()
                print(centraliza(atc("      Busca filtrada na minha pasta       DIGITE...    [B]", "yellow", "nao"), " "))
                print(centraliza(atc("      Voltar ao painel                    DIGITE...    [X]", "black", "sim"), " "))
                print(atc("", "cyan", "sim"))
                print(criar_faixa("="))
                QUAL = input("\n> ")
                QUAL = str(QUAL).lower().strip()
                CONTADOR = 8
                match QUAL:
                    case "1":
                        P = MINHAPASTA
                        lista = Files.listar_executaveis_para_print(P,"")
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: lines={CONTADOR}")
                        break
                    case "2":
                        P = PASTA_X
                        lista = Files.listar_executaveis_para_print(P,"")
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: lines={CONTADOR}")
                        break
                    case "3":
                        SELECIONADA = input("\n Digite o caminho da pasta que deseja listar: ")
                        P = SELECIONADA
                        lista = Files.listar_executaveis_para_print(P,"")
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: lines={CONTADOR}")
                        break
                    case "b":
                        P = MINHAPASTA
                        inicio = input(atc("\n Digite os primeiros números da versão filtrada: ", "magenta", "sim"))
                        lista = Files.listar_executaveis_para_print(P, inicio)
                        for i in lista:
                            CONTADOR+=1
                        os.system(f"mode con: lines={CONTADOR}")
                        break
                    case "x":
                        painel()
                    case _:
                        pass
            CONTADOR = CONTADOR - 8
            TAMANHOMAX = 83
            if CONTADOR == 0:
                print('\n')
                print(centraliza(atc(' NENHUMA VERSÃO ENCONTRADA !', 'RED', 'sim'), " "))
                pause()
                painel()
            else:
                print()
                TITULO = f' ({CONTADOR}) VERSÕES DISPONÍVEIS '
                TITULO = TITULO.center(TAMANHOMAX, "=")
                print(atc(TITULO, "green", "sim"))
                print()
                for versao in lista:
                    print(atc(f' ➤ {versao}', "cyan", "sim"))
                print()
                P = (f" {P} ").center(TAMANHOMAX, "=")
                print(atc(P, "green", "sim"))
                input()
                painel()
        case "w":
            EXE = str(Exe.procurar_ultimo_EXE(MINHAPASTA, "Webupload"))
            PEXE = str(EXE).replace(MINHAPASTA, "").replace(PASTA_X, "").replace("\\", "")
            print(atc(f"\n Caminho encontrado: {PEXE}", "blue", "sim"))
            time.sleep(2)
            Exe.somente_abrir_exe(EXE)
        case "f":
            from core import FastConections as FASTC # Fast-conections ( Conexoes já setadas no json )
            while True:
                limite = 31
                FC1 = FASTC.disponiveis[0]
                espace1 = (' '*(limite - len(FC1)))
                FC2 = FASTC.disponiveis[1]
                espace2 = (' '*(limite - len(FC2)))
                FC3 = FASTC.disponiveis[2]
                espace3 = (' '*(limite - len(FC3)))
                os.system("cls")
                os.system(TAMANHO_PADRAO)
                print(atc("","black","sim"))
                if config.MOSTRA_TITULO == 1:
                    print(centraliza(' DEFINA QUE TIPO DE AÇÃO DESEJA REALIZAR ','='))
                else: 
                    print(centraliza('','='))
                print(atc("", "cyan", "sim"))
                print(f'                FastC1 "{FC1}"{espace1}DIGITE...    [1]')
                print(f'                FastC2 "{FC2}"{espace2}DIGITE...    [2]')
                print(f'                FastC3 "{FC3}"{espace3}DIGITE...    [3]')
                print()
                print(f"                Reabrir último EXE                      DIGITE...    [U]")
                print()
                print(centraliza(atc("     Visuzalizar conexões                    DIGITE...    [V]", "blue", "sim")," "))
                print(centraliza(atc("     Editar uma conexão                      DIGITE...    [E]", "blue", "sim")," "))
                print()
                print(centraliza(atc("     Voltar ao painel                        DIGITE...    [X]", "black", "sim")," "))
                print(atc("", "black", "sim"))
                print(criar_faixa("="))
                resposta = input("\n> ")
                resposta = str(resposta).strip().lower()

                def retornar_conexão_json(n): # Utilizada para buscar / printar os dados do json (as conexoes)
                    n = str(n)
                    Nome = FASTC.conexoes[n]["NOME"]
                    IP = FASTC.conexoes[n]["IP"]
                    DB1 = FASTC.conexoes[n]["DB1"]
                    DB2 = FASTC.conexoes[n]["DB2"]
                    Porta = FASTC.conexoes[n]["PORTA"]
                    EXE = FASTC.conexoes[n]["EXE"]["VERSAO"]
                    nEXE = FASTC.conexoes[n]["EXE"]["EXECUTAVEL"]
                    return Nome, IP, DB1, DB2, Porta, EXE, nEXE

                def abrir_conexao_json(n): # Utiliza a funçao de buscar para retornar os valores e trabalha com eles para fazer o login
                    Nome, IP, DB1, DB2, Porta, EXE, nEXE = retornar_conexão_json(n)
                    print()
                    loading(f' Abrindo WebCamara "{Nome}"')
                    Files.alterar_conexao(IP, DB1, DB2, Porta)
                    EXE = Exe.procurar_exe_manual(MINHAPASTA, str(EXE), str(nEXE))
                    if EXE:
                        executar_login(USUARIOWEBCAM, SENHAWEBCAM, EXE)

                    if config.FECHA_LOGIN == 1:
                        sys.exit()

                match resposta:
                    case "x":
                        painel()
                    case "u":
                        print()
                        loading(f" Reabrindo último executável")
                        EXE = Files.ver_conexao_atual(LAST_ACCESS, 1)
                        executar_login(USUARIOWEBCAM, SENHAWEBCAM, EXE)
                    case "1":
                        abrir_conexao_json("1")
                    case "2":
                        abrir_conexao_json("2")
                    case "3":
                        abrir_conexao_json("3")
                    case "e":
                        qual = ""
                        while qual not in ("1", "2", "3"):
                            qual = input(atc('\nQual conexão deseja editar? ', 'white', 'sim')).strip()
                            if qual not in ("1", "2", "3"):
                                print(atc('\n Digite um número de 1 a 3 para escolher a conexão alterada!\n','red','sim'))
                        os.system("cls")
                        print(atc(f'\n Você selecionou [{FASTC.conexoes[qual]["NOME"]}]', 'green','sim'))
                        print(atc(f' Deixe os campos que não deseja alterar em branco.', 'black','sim'))
                        NOME = input(atc("\n> Defina um nome para a conexão: ","cyan","sim")).strip()
                        if NOME:
                            FASTC.editar_json(qual, "NOME", "", NOME)
                        IP = input("\n> IP: ").replace(" ","")
                        if IP:
                            FASTC.editar_json(qual, "IP", "", IP)
                        PORTA = input("> Porta: ").replace(" ","")
                        if PORTA:
                            FASTC.editar_json(qual, "PORTA", "", PORTA)
                        DB1 = input("\n> Banco de Registros: ").replace(" ","").lower()
                        if DB1:
                            FASTC.editar_json(qual, "DB1", "", DB1)
                        DB2 = input("> Banco de Arquivos: ").replace(" ","").lower()
                        if DB2:
                            FASTC.editar_json(qual, "DB2", "", DB2)
                        VERSAO = input("> Versão do EXE : ").replace(" ","").lower()
                        if VERSAO: 
                            FASTC.editar_json(qual, "EXE", "VERSAO", VERSAO)
                        EXECUTAVEL = input("> Número da versão do EXE: ").replace(" ","").lower()
                        if EXECUTAVEL == "":
                            EXECUTAVEL = '1'
                        FASTC.editar_json(qual, "EXE", "EXECUTAVEL", EXECUTAVEL)
                        print(atc('\n Conexão alterada com sucesso!', "green", "sim"))
                        print(atc(' (Reinicie o terminal para utilizar da conexão alterada) \n', "black", "sim"))
                        input()

                    case "v":
                        os.system("cls")
                        os.system(f"mode con: lines=36")
                        print()
                        contador = 1
                        cores = ["blue", "green", "cyan"]
                        for i in range(len(cores)): # Deixei o range no tamanho da lista de cores pq é a mesma quantidade de conexoes que tem no json
                            Nome, IP, DB1, DB2, Porta, EXE, nEXE = retornar_conexão_json(f"{contador}")
                            cor = cores[int(i)]
                            cor = str(cor).upper()
                            EXE = f"{EXE}({nEXE})"
                            
                            print(atc('', cor, "sim"))
                            print(centraliza(f'[ FC{contador} "{Nome}" ]','-'))
                            print()
                            print(f"> IP........  {IP}")
                            print(f"> BANCO 1...  {DB1}")
                            print(f"> BANCO 2...  {DB2}")
                            print(f"> PORTA.....  {Porta}")
                            print()
                            print(f"> EXE.......  {EXE}")
                            contador += 1
                        print()
                        pause()

        case "p":
            os.startfile(MINHAPASTA)
            painel()
        case _:
            painel()           
painel()