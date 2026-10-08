from core.config import PALETA_UTILIZADA, MOSTRA_TITULO, TAMANHO_PADRAO, MINHAPASTA, USUARIOWEBCAM, SENHAWEBCAM, FECHA_LOGIN
from style.style import centraliza, alterarCor as atc, criar_faixa, pause, loading, redimensionar, cls, coletarPaleta
from core import fastConections as FASTC # Fast-conections ( Conexoes já setadas no json )
from core.login import executarLogin
from classes import Files, Exe

CorPri, CorSec, CorTer, CorQua, CorFail, CorSuccess, CorLoading  = coletarPaleta(PALETA_UTILIZADA)

def painel_fastconections():
    while True:
        limite = 31
        FC1 = FASTC.disponiveis[0]
        espace1 = (' '*(limite - len(FC1)))
        FC2 = FASTC.disponiveis[1]
        espace2 = (' '*(limite - len(FC2)))
        FC3 = FASTC.disponiveis[2]
        espace3 = (' '*(limite - len(FC3)))
        cls()
        redimensionar()
        print(atc("",CorQua))
        if MOSTRA_TITULO == 1:
            print(centraliza(' DEFINA QUE TIPO DE AÇÃO DESEJA REALIZAR ','='))
        else: 
            print(centraliza('','='))
        print(atc("", CorPri))
        print(f'                FastC1 "{FC1}"{espace1}DIGITE...    [1]')
        print(f'                FastC2 "{FC2}"{espace2}DIGITE...    [2]')
        print(f'                FastC3 "{FC3}"{espace3}DIGITE...    [3]')
        print()
        print(f"                Reabrir último EXE                      DIGITE...    [U]")
        print()
        print(centraliza(atc(" Visuzalizar conexões                    DIGITE...    [V]", CorTer)," "))
        print(centraliza(atc(" Editar uma conexão                      DIGITE...    [E]", CorTer)," "))
        print()
        print(centraliza(atc(" Voltar ao painel                        DIGITE...    [X]", CorQua)," "))
        print(atc("", CorQua))
        print(criar_faixa("="))
        resposta = input("\n> ")
        resposta = str(resposta).strip().lower()

        def coletarConexaoJson(n): # Utilizada para buscar / printar os dados do json (as conexoes)
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
            Nome, IP, DB1, DB2, Porta, EXE, nEXE = coletarConexaoJson(n)
            print()
            loading(f' Abrindo WebCamara "{Nome}"')
            Files.alterarConexao(IP, DB1, DB2, Porta)
            EXE = Exe.procurarExeManualmente(MINHAPASTA, str(EXE), str(nEXE))
            if EXE:
                executarLogin(USUARIOWEBCAM, SENHAWEBCAM, EXE)

            if FECHA_LOGIN == 1:
                sys.exit()

        match resposta:
            case "x":
                break
            case "u":
                print()
                loading(f" Reabrindo último executável")
                EXE = Files.checarConexaoAtual(LAST_ACCESS, 1)
                executarLogin(USUARIOWEBCAM, SENHAWEBCAM, EXE)
            case "1":
                abrir_conexao_json("1")
            case "2":
                abrir_conexao_json("2")
            case "3":
                abrir_conexao_json("3")
            case "e":
                qual = ""
                while qual not in ("1", "2", "3"):
                    qual = input(atc('\nQual conexão deseja editar? ', CorLoading)).strip()
                    if qual not in ("1", "2", "3"):
                        print(atc('\n Digite um número de 1 a 3 para escolher a conexão alterada!\n', CorFail))
                cls()
                print(atc(f'\n Você selecionou [{FASTC.conexoes[qual]["NOME"]}]', CorSuccess))
                print(atc(f' Deixe os campos que não deseja alterar em branco.', CorQua))
                NOME = input(atc("\n> Defina um nome para a conexão: ", CorPri)).strip()
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
                print(atc('\n Conexão alterada com sucesso!', CorSuccess))
                print(atc(' (Reinicie o terminal para utilizar da conexão alterada) \n', CorQua))
                input()

            case "v":
                cls()
                redimensionar(36)
                print()
                contador = 1
                cores = [CorTer, CorSuccess, CorPri]
                for cor in cores: # Deixei o range no tamanho da lista de cores pq é a mesma quantidade de conexoes que tem no json
                    Nome, IP, DB1, DB2, Porta, EXE, nEXE = coletarConexaoJson(f"{contador}")
                    EXE = f"{EXE}({nEXE})"
                    print(atc('', cor))
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