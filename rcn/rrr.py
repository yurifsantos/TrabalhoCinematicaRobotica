#  Importando apenas as funções utilizadas no algoritmo do módulo Math do python
from math import sqrt, pow, radians, degrees, cos, sin, acos, asin, atan


#  Função base do algoritmo que chama as funções que adquirem os valores e realizam os calculos
def calculo_cinematica_rrr(modo):
    l1, l2, l3 = rrr_adquirir_elos() #  Chamando a função que adquire os elos do robô e desempacotando a resposta.
    if "D" in modo:
        print(f'Modo direto.\n')
        t1, t2, t3 = rrr_adquirir_tetas() #  Chamando a função que adquire os ângulos do robô e desempacotando a resposta.
        rrr_calculo_direto(l1, l2, l3, t1, t2, t3) # Chamando a função que realiza o calculo da cinemática direta.
    elif "I" in modo:
        print(f'Modo inverso.\n')
        x, y, delta = rrr_adquirir_ponto() #  Chamando a função que adquire a posição final do robô e desempacotando a resposta.
        rrr_calculo_inverso(l1, l2, l3, x, y, delta) # Chamando a função que realiza o calculo da cinemática inversa.


#  Função que adquiri o valor dos elos do robô e os retorna para realizar o calculo.
def rrr_adquirir_elos():
    print(f'Por favor, insira os seguintes dados do Robô RRR:')
    l1 = float(input('L1: '))
    l2 = float(input('L2: '))
    l3 = float(input('L3: '))
    print(f'Os valores do tamanho dos elos são: \nL1 = {l1}\t\tL2 = {l2}\t\t L3 = {l3}')
    return l1, l2, l3


#  Função que adquiri o valor dos ângulos do robô e os retorna para realizar o calculo.
def rrr_adquirir_tetas():
    print(f'Por favor, insira os seguintes dados do Robô RRR:')
    t1 = float(input('Teta 1: '))
    t2 = float(input('Teta 2: '))
    t3 = float(input('Teta 3: '))
    print(f'\nOs valores dos ângulos entre os elos são: \nTeta 1 = {t1}º\t\tTeta 2 = {t2}º\t\tTeta 3 = {t3}º')
    return t1, t2, t3


#  Função que adquiri o valor do ponto final do ôrgão terminal do robô e os retorna para realizar o calculo.
def rrr_adquirir_ponto():
    print(f'Por favor, insira os seguintes dados do Robô RRR:')
    x = float(input('Posição X: '))
    y = float(input('Posição Y: '))
    delta = float(input('Para realizar os calculos, necessita-se do valor de delta:'))
    print(f'\nOs valores da posição do orgão terminal são: \nX = {x}\t\tY = {y}\t\tDelta = {delta}º')
    return x, y, delta


#  Função que realiza o calculo direto da cinemática do robô e imprime a resposta no terminal.
def rrr_calculo_direto(l1, l2, l3, t1, t2, t3):
    x = l1 * cos(radians(t1)) + l2 * cos(radians(t1 + t2)) + l3 * cos(radians(t1 + t2 + t3))
    y = l1 * sin(radians(t1)) + l2 * sin(radians(t1 + t2)) + l3 * sin(radians(t1 + t2 + t3))
    
    print(f'O orgão terminal se posicionará em ({x:.2f}, {y:.2f})\n')


#  Função que realiza o calculo direto da cinemática do robô e imprime a resposta no terminal.
def rrr_calculo_inverso(l1, l2, l3, x, y, delta):
    try:
        t2_num = pow((x - l3 * cos(radians(delta))), 2) + pow((y - l3 * sin(radians(delta))), 2) - pow(l1, 2) - pow(l2, 2)
        t2_den = 2 * l1 * l2
        t2 = degrees(acos(t2_num / t2_den))
    except ValueError:
        print(f'Desculpe, porém a posição inserida não é possível de ser alcançada.')
        return

    try:
        t1_num = (y - l3 * sin(radians(delta))) * (l1 - l2 * cos(radians(t2))) - (x - l3 * cos(radians(delta))) * (l2 * sin(radians(t2)))
        t1_den = (x - l3 * cos(radians(delta))) * (l1 - l2 * cos(radians(t2))) + (y - l3 * sin(radians(delta))) * (l2 * sin(radians(t2)))
        t1 = degrees(atan(t1_num / t1_den))
    except ValueError:
        print(f'Desculpe, porém a posição inserida não é possível de ser alcançada.')
        return

    t3 = delta - t1 - t2

    print(f'Para chegar no ponto desejado, o robô utiliza os seguintes parâmetros:\nTeta 1: {t1:.2f}º \t\tTeta 2: {t2:.2f}º\t\tTeta 3: {t3:.2f}º')
