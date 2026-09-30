from core import fastConections as FASTC # Fast-conections ( Conexoes já setadas no json )
from style.style import centraliza, alterar_cor as atc, criar_faixa, pause, loading
from classes import Files, Exe
from core import config
from core.login import executar_login
import os

def painel_fastconections():
    TAMANHO_PADRAO = config.TAMANHO_PADRAO
    MINHAPASTA = config.MINHAPASTA
    USUARIOWEBCAM = config.USUARIOWEBCAM
    SENHAWEBCAM = config.SENHAWEBCAM
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
                break
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