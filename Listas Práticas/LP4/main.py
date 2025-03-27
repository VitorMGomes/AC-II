def expressao(mnemonico):
    if mnemonico == "umL":
        return '0'
    elif mnemonico == "AonB":
        return '1'
    elif mnemonico == "copiaA":
        return '2'
    elif mnemonico == "nAxnB":
        return '3'
    elif mnemonico == "AeBn":
        return '4'
    elif mnemonico == "nA":
        return '5'
    elif mnemonico == "AenB":
        return '6'
    elif mnemonico == "nAonB":
        return '7'
    elif mnemonico == "AxB":
        return '8'
    elif mnemonico == "zeroL":
        return '9'
    elif mnemonico == "copiaB":
        return 'A'
    elif mnemonico == "AeB":
        return 'B'
    elif mnemonico == "nB":
        return 'C'
    elif mnemonico == "nAeBn":
        return 'D'
    elif mnemonico == "AoB":
        return 'E'
    elif mnemonico == "nAeB":
        return 'F'
    else:
        return 'X'


def main():
    x = "0"
    y = "0"
    w = "0"
    A = "0"
    B = "0"

    try:
        with open("testeula.ula", "r") as arquivo, open("testeula.hex", "w") as arquivoHex:
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith("X="):
                    x = linha[2:].rstrip(';')
                elif linha.startswith("Y="):
                    y = linha[2:].rstrip(';')
                elif linha.startswith("W="):
                    mnemonico = linha[2:].rstrip(';')
                    A = x
                    B = y
                    w = expressao(mnemonico)
                    arquivoHex.write(f"{A}{B}{w}\n")

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
