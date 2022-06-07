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
    for tipos in robos:
        print(tipos)

    tipo_invalido = True    # Variavel utilizada para validação do tipo selecionado

    # Loop de validação. O terminal continua perguntando qual tipo será trabalho até que o usuário insira uma resposta válida.
    while(tipo_invalido):
        selecao = input('Tipo a ser trabalhado: ')
        # Transforma o input em letra maiuscula. Não há necessidade, porém o código foi utilizando letras maiúsculas.
        selecao = selecao.upper()

        # Loop de comparação do valor inserido. Caso o valor seja válido, tipo_invalido vira falso e o while é terminado.
        for tipos in robos:
            if selecao == tipos:
                tipo_invalido = False
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
    #  Variável que chama e recebe o resultado do selecionamento do modo de cinemático (direto ou inverso)
    modo_cinematica = seleciona_cinematica()
    robos[tiporobo](modo_cinematica)


if __name__ == '__main__':
    selec = seleciona_robo()
    passa_parametros(selec)
