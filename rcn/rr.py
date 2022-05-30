def calculo_cinematica_rr(modo):
    l1, l2 = rr_adquirir_elos()
    if "D" in modo:
        print(f'Modo direto')
    elif "I" in modo:
        print(f'Modo inverso')


def rr_adquirir_elos():
    print(f'Por favor, insira os seguintes dados do Robô RR:')
    l1 = float(input('L1: '))
    l2 = float(input('L2: '))
    print(f'Os valores do tamanho dos elos são: \nL1 = {l1} \t\t L2 = {l2}')
    return l1, l2