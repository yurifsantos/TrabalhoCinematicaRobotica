robos = {"RR": 1,
         "RL": 2,
         "RRR": 3,
         "RLR": 4,
         "TRR": 5,
         "VRR": 6,
         "TRLR": 7,
         "VVLR": 8}


def seleciona_robo():
    print(f'Escolha um dos seguintes tipos de robô: ')
    for tipos in robos:
        print(tipos)

    tipo_invalido = True
    while(tipo_invalido):
        selecao = input('Tipo a ser trabalhado: ')
        selecao = selecao.upper()

        for tipos in robos:
            if selecao == tipos:
                tipo_invalido = False
                return selecao
                break

        print(f'Tipo selecionado inválido! Favor escolher entre os valores da lista a cima.\n')


def adquirir_elos(num_elos):
    print(f'Por favor, insira os seguintes dados do Robô RR:')
    l1 = float(input('L1: '))
    l2 = float(input('L2: '))
    print(f'Os valores do tamanho dos elos são: \nL1 = {l1} \t\t L2 = {l2}')
