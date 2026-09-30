import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='data/.env')
from pathlib import Path

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

# ======================== ABAIXO DEFINO AS PREDEFINIÇÕES / DO PROGRAMA =========================

COLUNAS = "87"
LINHAS = "22"
CORPADRAO = "color 0B"
TAMANHO_PADRAO = F"mode con: cols={COLUNAS} lines={LINHAS}"

TEMPO_LOADING_PADRAO = 1        # Defino o tempo de espera padrao utilizado no sistema
TEMPO_CARREGA_BANNER = 0.0005   # Defino o tempo de carregamento do Banner do sistema (carregamento por caractere)

# ================================= CONFIGURACOES DE ATIVAMENTO =================================

# (se deixar algo vazio o codigo quebra (pqsim))

USA_BANNER = 0                 # 1 = Usar o banner
FECHA_LOGIN = 0                # 1 = Fechar programa ao finalizar o login
ESPERA_LOGIN = 120             # Tempo coletado para definir o quanto o login espera antes de "desistir" no caso do programa nao carregar
MOSTRA_TITULO = 0              # 1 = Mostrar titulo nos paineis
