from utils.json import abrirJson
from dotenv import load_dotenv
load_dotenv(dotenv_path='data/.env')
from pathlib import Path
import time, os

# ====================== ABAIXO DEFINO A COLETA DOS DADOS QUE VEM DO ENV ======================

USUARIOWEBCAM = os.getenv('USUARIOWEBCAM')
SENHAWEBCAM = os.getenv('SENHAWEBCAM')
IP = os.getenv('IP')
DB = os.getenv('DB')
DBF = os.getenv('DBF')
PORTA = os.getenv('PORTA')

# ================= ABAIXO DEFINO MINHAS PASTAS QUE SERAO USADAS PELO PROGRAMA  ===============

MINHAPASTA = os.getenv('MINHAPASTA')
PASTA_X = os.getenv('PASTA_X')
CLIENTE_X = os.getenv('NOME_X')  

PASTAPRINCIPAL = Path(__file__).resolve().parent.parent
CONFIG_INI = Path(MINHAPASTA) / "configuracao.ini"
ENDERECO_INI = Path(MINHAPASTA) / "endereco_ip_servidor.ini"  
LAST_ACCESS = PASTAPRINCIPAL  / "data" / "last_access.txt"
JSON_CONFIGURACOES = PASTAPRINCIPAL / "core" / "configs.json"
configuracoesEditaveis = abrirJson(JSON_CONFIGURACOES)
JSON_PALETAS = PASTAPRINCIPAL / "style" / "palettes.json"
todasPaletas = abrirJson(JSON_PALETAS)

# ======================== ABAIXO DEFINO AS PREDEFINIÇÕES / DO PROGRAMA ========================

COLUNAS = configuracoesEditaveis["[ESTILO] colunas"]                         # Define a largura do CMD
LINHAS =  configuracoesEditaveis["[ESTILO] linhas"]                           # Define a altura do CMD

TAMANHO_PADRAO = f"mode con: cols={COLUNAS} lines={LINHAS}"
CORPADRAO = "color 0B"

TEMPO_LOADING_PADRAO = configuracoesEditaveis["[TEMPO ] tempo_loading"]      # Defino o tempo de espera padrao utilizado no sistema
TEMPO_CARREGA_BANNER = configuracoesEditaveis["[TEMPO ] tempo_banner"]       # Defino o tempo de carregamento do Banner do sistema (carregamento por caractere)
ESPERA_LOGIN = configuracoesEditaveis["[TEMPO ] espera_login"]               # Tempo coletado para definir o quanto o login espera antes de "desistir" no caso do programa nao carregar

# ================================= CONFIGURACOES DE ATIVAMENTO =================================

USA_BANNER = configuracoesEditaveis["[DEFINE] usa_banner"]                   # 1 = Usar o banner
FECHA_LOGIN = configuracoesEditaveis["[DEFINE] fecha_login"]                 # 1 = Fechar programa ao finalizar o login
MOSTRA_TITULO = configuracoesEditaveis["[DEFINE] mostra_titulo"]             # 1 = Mostrar titulo nos paineis

# ============= ABAIXO DEFINO A DATA ATUAL QUE É UTILIZADA NAS PALETAS E NO BANNER ============

def definirEpoca(DATA):
    DATA = str(DATA)
    MES = DATA.replace(DATA[5:], '')
    MES = MES.replace(MES[:3], '')
    match MES:
        case '10':
            return "hallowen"
        case '11':
            return "dia-de-muertos"
        case '12':
            return "natalina"
        case _:
            return "principal"
            
tempo_atual = time.localtime()
HOJE = time.strftime("%d/%m/%Y", tempo_atual)

if configuracoesEditaveis["[ESTILO] paletas_temporais"]:
    PALETA_UTILIZADA = definirEpoca(HOJE)
else:
    PALETA_UTILIZADA = configuracoesEditaveis["[ESTILO] paleta_de_cores"]

if configuracoesEditaveis["[DEFINE] mensagem_banner"]:
    MENSAGEM_PALETA = todasPaletas[PALETA_UTILIZADA]["mensagem"]
else:
    MENSAGEM_PALETA = ""

