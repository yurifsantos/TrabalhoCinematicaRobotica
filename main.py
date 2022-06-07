import rcn      # Incluindo o módulo rcn (Robótica - Cinemática )

# Dicionário contendo os valores associados ao robôs
robos = {"RR": rcn.rr.calculo_cinematica_rr,
         "RL": rcn.rl.calculo_cinematica_rl,
         "RRR": rcn.rrr.calculo_cinematica_rrr,
         "RLR": rcn.rlr.calculo_cinematica_rlr,
         "TRR": rcn.trr.calculo_cinematica_trr,
         "TRLR": rcn.trlr.calculo_cinematica_trlr,
         "VVLR": rcn.vvlr.calculo_cinematica_vvlr}


# Função que seleciona o tipo de robo a ser calculado os valores
def seleciona_robo():
    print(f'Escolha um dos seguintes tipos de robô: ')

    # Imprimindo a lista de tipos de robos do dicionários robos[]
    print(*robos.keys())

    # Loop de validação. O terminal continua perguntando qual tipo será trabalho até que o usuário insira uma resposta válida.
    while(1):
        selecao = input('Tipo a ser trabalhado: ').upper()

        if selecao in robos.keys():
            return selecao

        print(f'Tipo selecionado inválido! Favor escolher entre os valores da lista a cima.\n')


# Função que seleciona a cinemática a ser calculada: direta ou inversa
def seleciona_cinematica():
    print(f'\nPor favor, insira qual cinemática deseja calcular:')

    # Loop de validação. O terminal continua perguntando qual modo será trabalho até que o usuário insira uma resposta válida.
    modo_invalido = True
    while(modo_invalido):
        modo = input('"D" para Direta e "I" para Inversa: ')
        # Transforma o input em letra maiuscula. Novamente, não há necessidade, porém exige restruturação caso removido.
        modo = modo.upper()

        #  Comparação do valor inserido. Caso seja um valor válido, retorna o modo para a variavel que chamou a função.
        if modo == 'D':
            print(f'Modo Selecionado: Cinemática Direta;\n')
            modo_invalido = False
            return modo
        elif modo == 'I':
            print(f'Modo Selecionado: Cinemática Inversa;\n')
            modo_invalido = False
            return modo
        else:
            print(f'Modo selecionado inválido! Favor escolher entre os valores da lista a cima.\n')



#  Função que serve para passar os parâmetros para serem calculadas em seus respectivos algoritmos.
#  Cada algoritmo relacionado a cada tipo de robô deve ser escrito em seus respectivo arquivo na pasta do módulo rcn.
def passa_parametros(tiporobo):
    robos[tiporobo](seleciona_cinematica())

if __name__ == '__main__':
    selec = seleciona_robo()
    passa_parametros(selec)
