#  Importando apenas as funções utilizadas no algoritmo do módulo Math do python
from math import sqrt, pow, radians, degrees, cos, sin, acos, asin, atan


#  Função base do algoritmo que chama as funções que adquirem os valores e realizam os calculos
def calculo_cinematica_trr(modo):
    l1, l2, l3 = trr_adquirir_elos() #  Chamando a função que adquire os elos do robô e desempacotando a resposta.
    if "D" in modo:
        print(f'Modo direto.\n')
        t1, t2, t3 = trr_adquirir_tetas() #  Chamando a função que adquire os ângulos do robô e desempacotando a resposta.
        trr_calculo_direto(l1, l2, l3, t1, t2, t3) # Chamando a função que realiza o calculo da cinemática direta.
    elif "I" in modo:
        print(f'Modo inverso.\n')
        x, y, z = trr_adquirir_ponto() #  Chamando a função que adquire a posição final do robô e desempacotando a resposta.
        trr_calculo_inverso(l1, l2, l3, x, y, z) # Chamando a função que realiza o calculo da cinemática inversa.


#  Função que adquiri o valor dos elos do robô e os retorna para realizar o calculo.
def trr_adquirir_elos():
    print(f'Por favor, insira os seguintes dados do Robô TRR:')
    l1 = float(input('L1: '))
    l2 = float(input('L2: '))
    l3 = float(input('L3: '))
    print(f'Os valores do tamanho dos elos são: \nL1 = {l1}\t\tL2 = {l2}\t\t L3 = {l3}')
    return l1, l2, l3


#  Função que adquiri o valor dos ângulos do robô e os retorna para realizar o calculo.
def trr_adquirir_tetas():
    print(f'Por favor, insira os seguintes dados do Robô TRR:')
    t1 = float(input('Teta 1: '))
    t2 = float(input('Teta 2: '))
    t3 = float(input('Teta 3: '))
    print(f'\nOs valores dos ângulos entre os elos são: \nTeta 1 = {t1}º\t\tTeta 2 = {t2}º\t\tTeta 3 = {t3}º')
    return t1, t2, t3


#  Função que adquiri o valor do ponto final do ôrgão terminal do robô e os retorna para realizar o calculo.
def trr_adquirir_ponto():
    print(f'Por favor, insira os seguintes dados do Robô TRR:')
    x = float(input('Posição X: '))
    y = float(input('Posição Y: '))
    z = float(input('Posição Z: '))
    print(f'\nOs valores da posição do orgão terminal são: \nX = {x}\t\tY = {y}\t\tZ = {z}º')
    return x, y, z


#  Função que realiza o calculo direto da cinemática do robô e imprime a resposta no terminal.
def trr_calculo_direto(l1, l2, l3, t1, t2, t3):
    x = (l2 * cos(radians(t2)) + l3 * cos(radians(t2 + t3))) * cos(radians(t1))
    y = (l2 * cos(radians(t2)) + l3 * cos(radians(t2 + t3))) * sin(radians(t1))
    z = l1 + l2 * sin(radians(t2)) + l3 * sin(radians(t2 + t3))
    
    print(f'O orgão terminal se posicionará em ({x:.2f}, {y:.2f}, {z:.2f})\n')


#  Função que realiza o calculo direto da cinemática do robô e imprime a resposta no terminal.
def trr_calculo_inverso(l1, l2, l3, x, y, z):
    #  Try..Except utilizado para definir que a posição insirida não pode ser alcançada com as medidas inseridas;
    try:
        #  Numerador da formula do Teta 3
        t3_num = pow(x, 2) + pow(y, 2) + pow((z-l1), 2) - pow(l2, 2) - pow(l3, 2)
        t3_den = 2 * l2 * l3 #  Denominador da formula do Teta 2
        t3 = degrees(acos(t3_num / t3_den)) #  Transforma-se o valor final de volta para graus.
    except ValueError:
        print(f'Desculpe, porém a posição inserida não é possível de ser alcançada.')
        return

    try:
        #  Numerador da formula do Teta 2
        t2_num = (z - l1) * (l2 + l3 * cos(radians(t3))) - (sqrt((pow(x, 2) + pow(y, 2))) * l3 * sin(radians(t3)))
        t2_den = sqrt((pow(x, 2) + pow(y, 2))) * (l2 + l3 * cos(radians(t3))) + ((z - l1) * l3 * sin(radians(t3)))
        t2 = degrees(atan(t2_num / t2_den)) #  Transforma-se o valor final de volta para graus.
    except ValueError:
        print(f'Desculpe, porém a posição inserida não é possível de ser alcançada.')
        return

    if x == 0:
        t1 = 90
    else:
        t1 = degrees(atan(y/x))

    if t1 < 0 or t2 < 0 or t3 < 0:
        print(f'Desculpe, porém a posição inserida não é possível de ser alcançada.')
    else:
        print(f'Para chegar no ponto desejado, o robô utiliza os seguintes parâmetros:\nTeta 1: {t1:.2f}º \t\tTeta 2: {t2:.2f}º\t\tTeta 3: {t3:.2f}º')
