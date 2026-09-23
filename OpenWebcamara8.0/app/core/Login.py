import os
import time
import subprocess
from pywinauto import Desktop
from core.config import ESPERA_LOGIN, MINHAPASTA, PASTA_X
from style.Style import alterar_cor as atc

def executar_login(usuario, senha, exe):
    oexe = str(exe).replace(MINHAPASTA, "").replace(PASTA_X, "").replace("\\", "")
    # pasta_exe = str(exe).replace(str(oexe), "")
    print(atc(f" EXE.......{oexe}", "black", "sim"))
    # print(atc(f" CAMINHO...{pasta_exe}", "black", "sim"))

    if not os.path.exists(exe): # VERIFICA SE O EXE EXISTE
        print("\n Executável não encontrado pelo Pywinauto!")
        print(" (Verifique a formatação utilizada)")
        input("")
        return False

    print(atc("\n Executável encontrado!, iniciando login.", "blue", "sim"))

    subprocess.Popen([exe]) # ABRE O EXE
    login = Desktop(backend="win32").window(class_name="TLogin_") # IDENTIFICA A TELA DE LOGIN DO PROGRAMA

    # ESPERA A TELA APARECER
    while not login.exists():
        time.sleep(0.1)
    login.wait("ready", timeout=ESPERA_LOGIN)

    # IDENTIFICA OS BOTÕES DE SENHA E LOGIN
    botaologin = login.child_window(class_name="TEdit")
    botaosenha = login.child_window(class_name="TMaskEdit")


    # PREENCHE OS CAMPOS DE LOGIN
    botaologin.click_input()
    botaologin.set_edit_text("")
    botaologin.set_edit_text(usuario)

    # PREENCHE OS CAMPOS DE SENHA
    botaosenha.click_input()
    botaosenha.set_edit_text(senha)

    # LOCALIZA E ESPERA O BOTÃO DE LOGIN ESTAR VISIVEL PARA CLICAR
    botaoentrar = login.child_window(title="OK")
    while not botaoentrar.exists():
        time.sleep(0.1)
    botaoentrar.wait("ready", timeout=ESPERA_LOGIN)

    # ESPERA UM POUCO ANTES DE CLICAR PARA NÃO DAR ERRO
    time.sleep(0.7)
    botaoentrar.click()
    
    return True