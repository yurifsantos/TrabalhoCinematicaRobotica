#  Importando apenas as funções utilizadas no algoritmo do módulo Math do python
from math import sqrt, pow, radians, degrees, cos, sin, acos, asin, atan


#  Função base do algoritmo que chama as funções que adquirem os valores e realizam os calculos
def calculo_cinematica_rl(modo):
    if "D" in modo:
        print(f'Modo direto.\n')
        t, d = rl_adquirir_parametros() #  Chamando a função que adquire os ângulos do robô e desempacotando a resposta.
        rl_calculo_direto(t, d) # Chamando a função que realiza o calculo da cinemática direta.
    elif "I" in modo:
        print(f'Modo inverso.\n')
        x, y = rl_adquirir_ponto() #  Chamando a função que adquire a posição final do robô e desempacotando a resposta.
        rl_calculo_inverso(x, y) # Chamando a função que realiza o calculo da cinemática inversa.


#  Função que adquiri o valor dos ângulos do robô e os retorna para realizar o calculo.
def rl_adquirir_parametros():
    print(f'Por favor, insira os seguintes dados do Robô RL:')
    t = float(input('Teta: '))
    d = float(input('D: '))
    print(f'\nOs valores dos parâmetros dos elos são: \nTeta = {t}º \t\t D = {d}')
    return t, d


#  Função que adquiri o valor do ponto final do ôrgão terminal do robô e os retorna para realizar o calculo.
def rl_adquirir_ponto():
    print(f'Por favor, insira os seguintes dados do Robô RL:')
    x = float(input('Posição X: '))
    y = float(input('Posição Y: '))
    print(f'\nOs valores da posição do orgão terminal são: \nX = {x} \t\t Y = {y}')
    return x, y


#  Função que realiza o calculo direto da cinemática do robô e imprime a resposta no terminal.
def rl_calculo_direto(t, d):
    x = d * cos(radians(t))
    y = d * sin(radians(t))
    
    print(f'O orgão terminal se posicionará em ({x:.2f}, {y:.2f})\n')


#  Função que realiza o calculo direto da cinemática do robô e imprime a resposta no terminal.
def rl_calculo_inverso(x, y):
    #  Condicional para caso o valor de X venha a ser zero, o que implica em um ângulo de 90º.
    if x == 0:
        t = 90
    else:
        t = degrees(atan(y/x))

    d = sqrt((pow(x, 2) + pow(y, 2)))

    print(f'Para chegar no ponto desejado, o robô utiliza os seguintes parâmetros:\nTeta: {t:.2f}º \t\tD: {d:.2f} ')
