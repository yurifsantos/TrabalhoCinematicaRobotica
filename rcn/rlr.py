#  Importando apenas as funções utilizadas no algoritmo do módulo Math do python
from math import sqrt, pow, radians, degrees, cos, sin, acos, asin, atan


#  Função base do algoritmo que chama as funções que adquirem os valores e realizam os calculos
def calculo_cinematica_rlr(modo):
    l3 = rlr_adquirir_elos() #  Chamando a função que adquire os elos do robô e desempacotando a resposta.
    if "D" in modo:
        print(f'Modo direto.\n')
        t1, l2, t3 = rlr_adquirir_parametros() #  Chamando a função que adquire os parâmetros do robô e desempacotando a resposta.
        rlr_calculo_direto(l2, l3, t1, t3) # Chamando a função que realiza o calculo da cinemática direta.
    elif "I" in modo:
        print(f'Modo inverso.\n')
        x, y, delta = rlr_adquirir_ponto() #  Chamando a função que adquire a posição final do robô e desempacotando a resposta.
        rlr_calculo_inverso(l3, x, y, delta) # Chamando a função que realiza o calculo da cinemática inversa.


#  Função que adquiri o valor dos elos do robô e os retorna para realizar o calculo.
def rlr_adquirir_elos():
    print(f'Por favor, insira os seguintes dados do Robô RLR:')
    l3 = float(input('L3: '))
    print(f'Os valores do tamanho dos elos são: \nL3 = {l3}')
    return l3


#  Função que adquiri o valor dos ângulos do robô e os retorna para realizar o calculo.
def rlr_adquirir_parametros():
    print(f'Por favor, insira os seguintes dados do Robô RLR:')
    t1 = float(input('Teta 1: '))
    l2 = float(input('Elo 2: '))
    t3 = float(input('Teta 3: '))
    print(f'\nOs valores dos ângulos entre os elos são: \nTeta 1 = {t1}º\t\tElo 2 = {l2}\t\tTeta 3 = {t3}º')
    return t1, l2, t3


#  Função que adquiri o valor do ponto final do ôrgão terminal do robô e os retorna para realizar o calculo.
def rlr_adquirir_ponto():
    print(f'Por favor, insira os seguintes dados do Robô RLR:')
    x = float(input('Posição X: '))
    y = float(input('Posição Y: '))
    delta = float(input('Para realizar os calculos, necessita-se do valor de delta:'))
    print(f'\nOs valores da posição do orgão terminal são: \nX = {x}\t\tY = {y}\t\tDelta = {delta}º')
    return x, y, delta


#  Função que realiza o calculo direto da cinemática do robô e imprime a resposta no terminal.
def rlr_calculo_direto(l2, l3, t1, t3):
    x = l2 * cos(radians(t1)) + l3 * cos(radians(t1 + t3))
    y = l2 * sin(radians(t1)) + l3 * sin(radians(t1 + t3))
    
    print(f'O orgão terminal se posicionará em ({x:.2f}, {y:.2f})\n')


#  Função que realiza o calculo direto da cinemática do robô e imprime a resposta no terminal.
def rlr_calculo_inverso(l3, x, y, delta):
    #  Try..Except utilizado para definir que a posição insirida não pode ser alcançada com as medidas inseridas;
    try:
        l2 = sqrt(pow((x - l3 * cos(radians(delta))), 2) + pow((y - l3 * sin(radians(delta))), 2))
    except ValueError:
        print(f'Desculpe, porém a posição inserida não é possível de ser alcançada.')
        return

    try:
        t1_num = y - l3 * sin(radians(delta))
        t1_den = x - l3 * cos(radians(delta))
        t1 = degrees(atan(t1_num / t1_den)) #  Transforma-se o valor final de volta para graus.
    except ValueError:
        print(f'Desculpe, porém a posição inserida não é possível de ser alcançada.')
        return

    t3 = delta - t1 #  Transforma-se o valor final de volta para graus.

    print(f'Para chegar no ponto desejado, o robô utiliza os seguintes parâmetros:\nTeta 1: {t1:.2f}º \t\tElo 2: {l2:.2f}\t\tTeta 3: {t3:.2f}º')
