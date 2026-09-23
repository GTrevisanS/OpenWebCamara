import os

# ================= ABAIXO DEFINO MINHAS PASTAS QUE SERAO USADAS PELO PROGRAMA  ===============

MINHAPASTA = r""
PASTA_X = r""
CLIENTE_X = "Prudente"                          # Para não deixar exposto o nome do cliente, uso como variável "sensível"

# ======================== ABAIXO DEFINO AS PREDEFINIÇÕES / DO PROGRAMA =========================

COLUNAS = "87"
LINHAS = "22"
CORPADRAO = "color 0B"
TAMANHO_PADRAO = F"mode con: cols={COLUNAS} lines={LINHAS}"

TEMPO_LOADING_PADRAO = 1        # Defino o tempo de espera padrao utilizado no sistema
TEMPO_CARREGA_BANNER = 0.0005   # Defino o tempo de carregamento do Banner do sistema (carregamento por caractere)

# ================================= CONFIGURACOES DE ATIVAMENTO =================================

# (se deixar algo vazio o codigo quebra (pqsim))

USA_BANNER = 0                # 1 = Usar o banner
FECHA_LOGIN = 0                # 1 = Fechar programa ao finalizar o login
ESPERA_LOGIN = 120             # Tempo coletado para definir o quanto o login espera antes de "desistir" no caso do programa nao carregar
MOSTRA_TITULO = 0              # 1 = Mostrar titulo nos paineis