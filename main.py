import rcn

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

        print(f'Tipo selecionado inválido! Favor escolher entre os valores da lista a cima.\n')

def seleciona_cinematica():
    print(f'Por favor, insira qual cinemática deseja calcular:')
    
    modo_invalido = True
    while(modo_invalido):
        modo = input('"D" para Direta e "I" para Inversa: ')
        modo = modo.upper()
        if modo == 'D':
            print(f'Modo Selecionado: Cinemática Direta;')
            modo_invalido = False
            return modo
        elif modo == 'I':
            print(f'Modo Selecionado: Cinemática Inversa;')
            modo_invalido = False
            return modo
        else:
            print(f'Modo selecionado inválido! Favor escolher entre os valores da lista a cima.\n')


def passa_parametros(tiporobo):
    selecao = robos[tiporobo]
    modo_cinematica = seleciona_cinematica()
    match selecao:
        case 1:
            rcn.rr.calculo_cinematica_rr(modo_cinematica)
        case 2:
            rcn.rl.calculo_cinematica_rl(modo_cinematica)
        case 3:
            rcn.rrr.calculo_cinematica_rrr(modo_cinematica)
        case 4:
            rcn.rlr.calculo_cinematica_rlr(modo_cinematica)
        case 5:
            rcn.trr.calculo_cinematica_trr(modo_cinematica)
        case 6:
            rcn.vrr.calculo_cinematica_vrr(modo_cinematica)        
        case 7:
            rcn.trlr.calculo_cinematica_trlr(modo_cinematica)
        case 8:
            rcn.vvlr.calculo_cinematica_vvlr(modo_cinematica)


def adquirir_elos(num_elos):
    print(f'Por favor, insira os seguintes dados do Robô RR:')
    l1 = float(input('L1: '))
    l2 = float(input('L2: '))
    print(f'Os valores do tamanho dos elos são: \nL1 = {l1} \t\t L2 = {l2}')

if __name__ == '__main__':
    selec = seleciona_robo()
    passa_parametros(selec)