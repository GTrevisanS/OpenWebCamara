
from core.config import JSON_CONFIGURACOES, PALETA_UTILIZADA, MOSTRA_TITULO
from style.style import (
    centraliza,
    alterarCor as atc,
    criar_faixa,
    pause,
    redimensionar,
    cls,
    coletarPaleta
)
from utils.json import abrirJson, editarJson

CorPri, CorSec, CorTer, CorQua, CorFail, CorSuccess, CorLoading = coletarPaleta(PALETA_UTILIZADA)

configuracoes = abrirJson(JSON_CONFIGURACOES)


def printarOpcoes():
    contador = 1
    primeiroLimite = 20
    segundoLimite = 16
    for nomeConfiguracao, valor in configuracoes.items():
        nomeConfiguracao = nomeConfiguracao.replace('_', ' ').strip().title()
        espacoNome = ' ' * (primeiroLimite - len(nomeConfiguracao))
        espacoValor = atc(' ' * (segundoLimite - len(str(valor))), CorPri)
        valor = atc('"' + str(valor) + '"',CorSuccess)
        print(centraliza(
            f'{nomeConfiguracao}{espacoNome}{valor}{espacoValor}DIGITE...      [{str(contador).zfill(2)}]',
            ' '
        ))
        contador += 1


def encontrarConfig(numero):
    for contador, (config, valor) in enumerate(configuracoes.items(), start=1):
        if numero == contador:
            return config, valor

    return None


regrasEspecificas = {
    "tempo_banner": "O tempo do for do banner deve estar entre 0.005 e 0.000001",
    "colunas": "O número de colunas deve estar entre 80 e 110.",
    "linhas": "O número de linhas deve estar entre 15 e 30.",
    "espera_login": "O tempo de espera deve estar entre 5 e 300 segundos.",
    "paleta_de_cores": 'A paleta selecionada deve estar disponivel em "palettes.json"'
}


def editarConfig(numero, novo_valor):
    configEscolhida = encontrarConfig(numero)

    if not configEscolhida:
        return False

    chave, valorOriginal = configEscolhida

    # Validações de acordo com o tipo original
    if isinstance(valorOriginal, bool):
        if novo_valor.lower() in ("true", "1", "sim"):
            novo_valor = True
        elif novo_valor.lower() in ("false", "0", "nao", "não"):
            novo_valor = False
        else:
            print(atc("\n Digite true ou false!\n", CorFail))
            pause()
            return False

    elif isinstance(valorOriginal, int):
        if not novo_valor.isdigit():
            print(atc("\n Digite um número inteiro válido!\n", CorFail))
            pause()
            return False

        novo_valor = int(novo_valor)

    elif isinstance(valorOriginal, float):
        try:
            novo_valor = float(novo_valor.replace(",", "."))
        except ValueError:
            print(atc("\n Digite um número válido!", CorFail))
            pause()
            return False

        if novo_valor < 0:
            print(atc("\n O valor não pode ser negativo!", CorFail))
            pause()
            return False

    elif isinstance(valorOriginal, str):
        if not novo_valor.strip():
            print(atc("\n O valor não pode ficar vazio!", CorFail))
            pause()
            return False

        if chave == "paleta_de_cores":
            if novo_valor.lower() not in ("principal", "natalina", "halloween"):
                print(atc("\n Paleta não encontrada disponível!", CorFail))
                pause()
                return False

            novo_valor = novo_valor.lower()

    # Validações específicas
    if chave == "colunas" and not (80 <= novo_valor <= 110):
        print(atc(f"\n {regrasEspecificas['colunas']}", CorFail))
        pause()
        return False

    if chave == "linhas" and not (15 <= novo_valor <= 30):
        print(atc(f"\n {regrasEspecificas['linhas']}", CorFail))
        pause()
        return False

    if chave == "espera_login" and (novo_valor > 300 or novo_valor < 5):
        print(atc(f"\n {regrasEspecificas['espera_login']}", CorFail))
        pause()
        return False

    if chave in ("colunas", "linhas") and novo_valor <= 0:
        print(atc("\n O valor deve ser maior que zero!", CorFail))
        pause()
        return False

    if chave == "tempo_banner" and (novo_valor > 0.005 or novo_valor < 0.000001):
        print(atc(f"\n {regrasEspecificas['tempo_banner']}", CorFail))
        pause()
        return False

    if chave == "paleta_de_cores" and novo_valor not in ("principal", "natalina", "hallowen"):
        print(atc(f"\n {regrasEspecificas['paleta_de_cores']}", CorFail))
        pause()
        return False

    editarJson(JSON_CONFIGURACOES, chave, novo_valor)
    configuracoes[chave] = novo_valor

    print(atc("\n Configuração alterada com sucesso!", CorSuccess))
    pause()
    return True

def painel_configuracoes():
    while True:
        cls()
        redimensionar()
        print(atc("", CorQua))
        if MOSTRA_TITULO:
            print(centraliza(' DEFINA QUAL CONFIG DESEJA EDITAR ', '='))
        else:
            print(centraliza('', '='))
        print(atc("", CorPri))
        printarOpcoes()
        print()
        print(centraliza(atc("Voltar ao painel                      DIGITE...       [X]", CorQua), " "))
        print(atc("", CorQua))
        print(criar_faixa("="))

        resposta = input("\n> ").strip().lower()

        if resposta == "x":
            break

        elif resposta.isdigit():
            resposta = int(resposta)
            configEscolhida = encontrarConfig(resposta)
            if configEscolhida:
                cls()
                chave = configEscolhida[0]
                regra = regrasEspecificas.get(chave, "Não há regras específicas para esta configuração.")

                print(atc("", CorPri))
                print(centraliza(f" CONFIGURAÇÃO DE {chave.upper().replace('_', ' ')} ", "="))
                print(atc(f' ', CorSec))
                print(centraliza(f'{regra}', " "))
                print(centraliza(atc(f' O valor atual definido na configuração é "{configEscolhida[1]}" ', CorQua), " "))
                print(centraliza(atc(f'Digite o novo valor abaixo para alterar a config', CorQua), " "))
                print(atc("\n", CorPri))
                valorAlterado = input("\n> ").strip()

                if valorAlterado:
                    editarConfig(resposta, valorAlterado)
                else:
                    print(atc(" O valor não pode ficar vazio!", CorFail))
                    pause()
            else:
                print(atc(" Opção inválida!", CorFail))
                pause()
