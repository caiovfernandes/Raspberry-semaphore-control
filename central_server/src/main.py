from tcp_client import start_client_tcp

def main():
    while 1:
        print("Digite o valor de acordo com a opção selecionada\n\
                1. Modo noturno\n\
                2. Mono de Emergência\n\
                3. Modo normal\n\
                4. Modo debug\n\
                <====")
        value = input()
        if value == "1":
            start_client_tcp("True", "False","False","False")
            break
        elif value == "2":
            start_client_tcp("False", "True","False", "False")
            break
        elif value == "3":
            start_client_tcp("False", "False","True","False")
            break
        elif value == "4":
            start_client_tcp("False", "False","False","True")
            break
        else:
            print("Valor nao suportado, selecione uma das opcoes validas.\n\n")

if __name__ == '__main__':
    main()