
arquivo = open('arquivo_text.txt', 'r')
# abre o arquivo de texto com a definição do autômado

conteudo = arquivo.read()
# lê o arquivo de texto com a definição do autômado

dfa = eval(conteudo)
# transforma o arquivo de texto em dicionário

entrada = input("Digite a cadeia: ")
# input do usuário 


# função simulador
def simulador_dfa(dfa, entrada):
    estado = dfa['initial_state']
    aceitar = False

    while len(entrada) > 0:
        #  c lê o primeiro caractere da cadeia
        c = entrada[0]
        # entrada remove o primeiro caractere da cadeia e atualiza o valor em c = entrada[0]
        entrada = entrada [1:]

        if c not in dfa['sigma']:
            print(f'O símbolo "{c}" não pertence ao alfabeto do autômato!')
            break

        if estado not in dfa['states']:
            print(f'O estado "{estado}" não pertence ao conjunto de estados do autômato!')
            break
        
        estado = dfa['delta'].get((estado, c), None)

        # estado realiza a transição no DFA
        # a função get obtem o próximo estado do dfa (chave do dicionário) --> (valor).

        print(f"({dfa['delta'].get((estado, c))}, '{c}') --> {estado}")
        # imprimi a transição do estados e o próximo estado


        if estado is None:
            print(f'Não foi possível realizar a transição do estado "{estado}" com entrada "{c}"!')
            break

    if estado in dfa['final_states'] and entrada == '':
        aceitar = True

    if aceitar == True:
        print('A cadeia', entrada, 'foi aceita pelo autômato!')


    else:
        print('A cadeia', entrada, 'foi rejeitada pelo autômato!')


simulador_dfa(dfa, entrada)


