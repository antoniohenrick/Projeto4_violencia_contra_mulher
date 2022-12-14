# P03. De forma geral a senhora acha que a mulher é tratada com respeito no Brasil?
def dado2007_P3():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 1:
    De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P3'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P3'] / analise['P3'].sum()) * 100
    # respostas = ['As vezes', 'Não', 'Sim', 'NS/NR']
    # for i in range(len(respostas)):
    #     analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2007_P3(anls):
    '''
    Função que plota o gráfico da análise dos dados da 1ª pergunta do tema 1:
    De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('De forma geral a senhora acha que as mulheres são tratadas com respeito no Brasil?')
    plt.show()

# P04. Em qual dos ambientes a seguir a Sra. acha que a mulher é mais desrespeitada, na família, no trabalho, na sociedade ou em outros ambientes?
def dado2007_P4():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 1:
    Onde você acha que as mulheres são menos respeitadas?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P4'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P4'] / analise['P4'].sum()) * 100
    # respostas = ['Na rua', 'Na família', 'No trabalho']
    # for i in range(3):
    #     analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2007_P4(anls):
    '''
    Função que plota o gráfico da análise dos dados da 3ª pergunta do tema 1:
    Onde você acha que as mulheres são menos respeitadas?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em qual dos ambientes a seguir a Sra. acha que a mulher é mais desrespeitada, na família, no trabalho, na sociedade ou em outros ambientes?')
    plt.show()

# P05. A Sra. acha que as leis brasileiras protegem as mulheres contra a violência doméstica?
def dado2007_P5():
    '''
    Função que realiza a análise dos dados da 6ª pergunta do tema 4:
    As leis brasileiras protegem as mulheres contra abusos e violências domésticas?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P5'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P5'] / analise['P5'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P5(anls):
    '''
    Função que plota o gráfico da análise dos dados da 6ª pergunta do tema 4:
    As leis brasileiras protegem as mulheres contra abusos e violências domésticas?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('A Sra. acha que as leis brasileiras protegem as mulheres contra a violência doméstica?')
    plt.show()

# P07. A senhora já foi vitima ou sofreu algum tipo de violência doméstica?
def dado2007_P7():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 4:
    Você já foi vitima ou sofreu algum tipo de violência doméstica e familiar?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P7'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P7'] / analise['P7'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P7(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Você já foi vitima ou sofreu algum tipo de violência doméstica e familiar?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('A senhora já foi vitima ou sofreu algum tipo de violência doméstica?')
    plt.show()

# P08. O que motivou a violência?
def dado2007_P8():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 4:
    O que motivou a violência?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P8'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.drop(0, axis=0)
    analise['Percentual'] = (analise['P8'] / analise['P8'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P8(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    O que motivou a violência?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que motivou a violência?')
    plt.show()

# P09. Qual foi tipo de violência?
def dado2007_P9():
    '''
    Função que realiza a análise dos dados da 10ª pergunta do tema 2:
    Qual foi tipo de violência?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P9'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.drop(0, axis=0)
    analise['Percentual'] = (analise['P9'] / analise['P9'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P9(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Qual foi tipo de violência?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual foi tipo de violência?')
    plt.show()

# P10. Quem foi o agressor?
def dado2007_P10():
    '''
    Função que realiza a análise dos dados da 6ª pergunta do tema 2:
    Quem foi o agressor?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P10'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.drop(0, axis= 0)
    analise['Percentual'] = (analise['P10'] / analise['P10'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P10(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Quem foi o agressor?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quem foi o agressor?')
    plt.show()

# P11. A senhora ainda convive com ele?
def dado2007_P11():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 2:
    Você ainda convive com o agressor?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P11'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.drop(0, axis=0)
    analise['Percentual'] = (analise['P11'] / analise['P11'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P11(anls):
    '''
    Função que plota o gráfico da análise dos dados da 3ª pergunta do tema 2:
    Você ainda convive com o agressor?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você ainda convive com o agressor?')
    plt.show()

# P12. Com que freqüência a senhora sofre violência?
def dado2007_P12():
    '''
    Função que realiza a análise dos dados da 9ª pergunta do tema 2:
    Com que freqüência a senhora sofre violência?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P12'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.drop(0, axis=0)
    analise['Percentual'] = (analise['P12'] / analise['P12'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P12(anls):
    '''
    Função que plota o gráfico da análise dos dados da 9ª pergunta do tema 2:
    Com qual frequência você sofre violência?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Com qual frequência você sofre violência?')
    plt.show()

# P13. Qual foi a sua atitude em relação à sua última agressão?
def dado2007_P13():
    '''
    Função que realiza a análise dos dados da 7ª pergunta do tema 2:
    Qual foi a sua atitude em relação à sua última agressão?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P13'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.drop(0, axis=0)
    analise['Percentual'] = (analise['P13'] / analise['P13'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P13(anls):
    '''
    Função que plota o gráfico da análise dos dados da 7ª pergunta do tema 2:
    Qual foi sua atitude em relação à última agressão?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual foi sua atitude em relação à última agressão?')
    plt.show()

# P14. Como foi o atendimento na Delegacia?
def dado2007_P14():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 3:
    Como foi o atendimento na Delegacia?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P14'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.drop(0, axis=0)
    analise['Percentual'] = (analise['P14'] / analise['P14'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P14(anls):
    '''
    Função que plota o gráfico da análise dos dados da 1ª pergunta do tema 3:
    Como você avalia o atendimento recebido na delegacia?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Como foi o atendimento na Delegacia da Mulher?')
    plt.show()

# P15. Qual era a sua idade quando você foi agredida pela primeira vez?
def dado2007_P15():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 2:
    Qual era a sua idade quando você foi agredida pela primeira vez?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P15'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.drop(0, axis=0)
    analise['Percentual'] = (analise['P15'] / analise['P15'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2007_P15(anls):
    '''
    Função que plota o gráfico da análise dos dados da 2ª pergunta do tema 2:
    Qual era a sua idade quando você foi agredida pela primeira vez?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual era a sua idade quando você foi agredida pela primeira vez?')
    plt.show()

# P16. O que a Sra. acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica contra a mulher?
def dado2007_P16():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 5:
    O que a Sra. acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica contra a mulher?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P16'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise.loc[4, 'P16'] += 2
    analise = analise.drop(8, axis=0)
    analise['Percentual'] = (analise['P16'] / analise['P16'].sum()) * 100
    
    respostas = ['Denunciar', 'Intensificar as campanhas para divulgação dos direitos das mulheres',
    'Melhorar a assistência às vítimas', 'Capacitar lideranças comunitárias para que possam intervir nas emergências',
    'Outra opção', 'Estimular o debate social sobre o tema', 'Dividir de forma mais equilibrada as responsabilidades domésticas ',
    'NS/NR']
    for i in range(len(respostas)):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2007_P16(anls):
    '''
    Função que plota o gráfico da análise dos dados da 2ª pergunta do tema 5:
    O que você acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica e familiar contra a mulher?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que a Sra. acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica contra a mulher?')
    plt.show()

# P17. A senhora lembra de alguma campanha veiculada nos jornais impressos, no último ano, contra a violência às mulheres?
def dado2007_P17():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 5:
    A senhora lembra de alguma campanha veiculada nos jornais impressos, no último ano, contra a violência às mulheres?'''
    import pandas as pd
    dados_2007df = pd.read_csv("microdado_2007.csv", delimiter=';')

    analise = dados_2007df['P17'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P17'] / analise['P17'].sum()) * 100
    
    # respostas = ['Na rua', 'Na família', 'No trabalho']
    # for i in range(3):
    #     analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2007_P17(anls):
    '''
    Função que plota o gráfico da análise dos dados da 2ª pergunta do tema 4:
    Você lembra de ter visto ou ouvido alguma campanha veiculada na mídia contra a violência às mulheres?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você lembra de ter visto ou ouvido alguma campanha veiculada na mídia contra a violência às mulheres?')
    plt.show()

