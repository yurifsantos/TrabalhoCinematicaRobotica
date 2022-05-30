from math import sqrt, pow, radians, degrees, cos, sin, acos, asin, atan


def calculo_cinematica_rr(modo):
    l1, l2 = rr_adquirir_elos()
    if "D" in modo:
        print(f'Modo direto.\n')
        t1, t2 = rr_adquirir_tetas()
        rr_calculo_direto(l1, l2, t1, t2)
    elif "I" in modo:
        print(f'Modo inverso.\n')
        x, y = rr_adquirir_ponto()
        rr_calculo_inverso(l1, l2, x, y)


def rr_adquirir_elos():
    print(f'Por favor, insira os seguintes dados do Robô RR:')
    l1 = float(input('L1: '))
    l2 = float(input('L2: '))
    print(f'Os valores do tamanho dos elos são: \nL1 = {l1} \t\t L2 = {l2}')
    return l1, l2


def rr_adquirir_tetas():
    print(f'Por favor, insira os seguintes dados do Robô RR:')
    t1 = float(input('Teta 1: '))
    t2 = float(input('Teta 2: '))
    print(f'\nOs valores dos ângulos entre os elos são: \nTeta 1 = {t1} \t\t Teta 2 = {t2}')
    return t1, t2


def rr_adquirir_ponto():
    print(f'Por favor, insira os seguintes dados do Robô RR:')
    x = float(input('Posição X: '))
    y = float(input('Posição Y: '))
    print(f'\nOs valores da posição do orgão terminal são: \nX = {x} \t\t Y = {y}')
    return x, y


def rr_calculo_direto(l1, l2, t1, t2):
    x = l1 * cos(radians(t1)) + l2 * cos(radians(t1 + t2))
    y = l1 * sin(radians(t1)) + l2 * sin(radians(t1 + t2))
    
    print(f'O orgão terminal se posicionará em ({x:.2f}, {y:.2f})\n')


def rr_calculo_inverso(l1, l2, x, y):
    t2_num = pow(x, 2) + pow(y, 2) - pow(l1, 2) - pow(l2, 2)
    t2_den = 2 * l1 * l2
    t2 = degrees(acos(t2_num / t2_den))

    t1_num = y *(l1 + l2 * cos(radians(t2))) - x * l2 * sin(radians(t2))
    t1_den = x *(l1 + l2 * cos(radians(t2))) + y * l2 * sin(radians(t2))
    t1 = degrees(atan(t1_num / t1_den))

    print(f'Para chegar no ponto desejado, o robô utiliza os seguintes parâmetros:\nTeta 1: {t1:.2f} \t\tTeta 2: {t2:.2f} ')
