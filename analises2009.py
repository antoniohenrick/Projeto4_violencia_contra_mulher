#  P01. De forma geral, você acha que a mulher é tratada com respeito no Brasil?
def dado2009_P01():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 1:
    De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P01'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P01'] / analise['P01'].sum()) * 100
    # respostas = ['As vezes', 'Não', 'Sim', 'NS/NR']
    # for i in range(len(respostas)):
    #     analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2009_P01(anls):
    '''
    Função que plota o gráfico da análise dos dados da 1ª pergunta do tema 1:
    De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?')
    plt.show()

# P02.Onde você acha que as mulheres são menos respeitadas?  
def dado2009_P02():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 1:
    Onde você acha que as mulheres são menos respeitadas?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P02'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P02'] / analise['P02'].sum()) * 100
    # respostas = ['Na rua', 'Na família', 'No trabalho']
    # for i in range(3):
    #     analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2009_P02(anls):
    '''
    Função que plota o gráfico da análise dos dados da 3ª pergunta do tema 1:
    Onde você acha que as mulheres são menos respeitadas?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Onde você acha que as mulheres são menos respeitadas?')
    plt.show()

# As leis brasileiras protegem as mulheres contra abusos e violências domésticas?
def dado2009_P07():
    '''
    Função que realiza a análise dos dados da 6ª pergunta do tema 4:
    As leis brasileiras protegem as mulheres contra abusos e violências domésticas?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P07'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P07'] / analise['P07'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P07(anls):
    '''
    Função que plota o gráfico da análise dos dados da 6ª pergunta do tema 4:
    As leis brasileiras protegem as mulheres contra abusos e violências domésticas?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('As leis brasileiras protegem as mulheres contra abusos e violências domésticas?')
    plt.show()

# Já ouviu falar de lei maria da penha?
def dado2009_P08():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 4:
    Você já ouviu falar da Lei Maria da Penha?'''
    import pandas as pd

    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P08'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P08'] / analise['P08'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P08(anls):
    '''
    Função que plota o gráfico da análise dos dados da 3ª pergunta do tema 4:
    Você já ouviu falar da Lei Maria da Penha?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você já ouviu falar da Lei Maria da Penha?')
    plt.show()

# Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar?
def dado2009_P11():
    '''
    Função que realiza a análise dos dados da 10ª pergunta do tema 2:
    Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar?'''
    import pandas as pd

    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise_coletiva = dados_2009df[['P111', 'P112', 'P113', 'P114']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P111 = analise_coletiva['P111'].value_counts().reset_index()
    P112 = analise_coletiva['P112'].value_counts().reset_index()
    P113 = analise_coletiva['P113'].value_counts().reset_index()
    P114 = analise_coletiva['P114'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = (
        P111.loc[1, 'P111']
        + P112.loc[1, 'P112']
        + P113.loc[1, 'P113']
        + P114.loc[1, 'P114']
    )
    
    # quantidade total de cada pergunta
    tot_1 = P111.loc[1, 'P111'] 
    tot_2 = P112.loc[1, 'P112'] 
    tot_3 = P113.loc[1, 'P113'] 
    tot_4 = P114.loc[1, 'P114']     

    # percentual para cada pergunta afirmativa
    percen_1 = (P111.loc[1, 'P111'] / tot_sim) * 100
    percen_2 = (P112.loc[1, 'P112'] / tot_sim) * 100
    percen_3 = (P113.loc[1, 'P113'] / tot_sim) * 100
    percen_4 = (P114.loc[1, 'P114'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['A vítima', 'As pessoas que presenciaram a agressão', 'Qualquer pessoa que tenha conhecimento do fato', 'NS/NR']
    total = [tot_1, tot_2, tot_3, tot_4]
    percentual = [percen_1, percen_2, percen_3, percen_4]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2009_P11(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar?')
    plt.show()

#P13. Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?
def dado2009_P13():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 4:
    Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?'''
    import pandas as pd

    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P13'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P13'] / analise['P13'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P13(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?')
    plt.show()

# P15. Você já foi vitima ou sofreu algum tipo de violência doméstica e familiar? 
def dado2009_P15():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 4:
    Você já foi vitima ou sofreu algum tipo de violência doméstica e familiar?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P15'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P15'] / analise['P15'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P15(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Você já foi vitima ou sofreu algum tipo de violência doméstica e familiar?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você já foi vitima ou sofreu algum tipo de violência doméstica e familiar?')
    plt.show()

# P16. O que motivou a violência?
def dado2009_P16():
    '''
    Função que realiza a análise dos dados da 8ª pergunta do tema 2:
    O que motivou a violência?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise_coletiva = dados_2009df[['P1601', 'P1602', 'P1603', 'P1604', 'P1605','P1606', 'P1607', 'P1608', 'P1609', 'P1610']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P1601 = analise_coletiva['P1601'].value_counts().reset_index()
    P1602 = analise_coletiva['P1602'].value_counts().reset_index()
    P1603 = analise_coletiva['P1603'].value_counts().reset_index()
    P1604 = analise_coletiva['P1604'].value_counts().reset_index()
    P1605 = analise_coletiva['P1605'].value_counts().reset_index()
    P1606 = analise_coletiva['P1606'].value_counts().reset_index()
    P1607 = analise_coletiva['P1607'].value_counts().reset_index()
    P1608 = analise_coletiva['P1608'].value_counts().reset_index()
    P1609 = analise_coletiva['P1609'].value_counts().reset_index()
    P1610 = analise_coletiva['P1610'].value_counts().reset_index()


    # # quantidade de valores 'sim'
    tot_sim = (
        P1601.loc[1, 'P1601']
        + P1602.loc[1, 'P1602']
        + P1603.loc[1, 'P1603']
        + P1604.loc[1, 'P1604']
        + P1605.loc[1, 'P1605']
        + P1606.loc[1, 'P1606']
        + P1607.loc[1, 'P1607']
        + P1609.loc[1, 'P1609']
        + P1610.loc[1, 'P1610']
    )
    
    # quantidade total de cada pergunta
    tot_1 = P1601.loc[1, 'P1601'] 
    tot_2 = P1602.loc[1, 'P1602'] 
    tot_3 = P1603.loc[1, 'P1603'] 
    tot_4 = P1604.loc[1, 'P1604'] 
    tot_5 = P1605.loc[1, 'P1605']
    tot_6 = P1606.loc[1, 'P1606']
    tot_7 = P1607.loc[1, 'P1607']
    
    tot_9 = P1609.loc[1, 'P1609']
    tot_10 = P1610.loc[1, 'P1610']

    # percentual para cada pergunta afirmativa
    percen_1 = (P1601.loc[1, 'P1601'] / tot_sim) * 100
    percen_2 = (P1602.loc[1, 'P1602'] / tot_sim) * 100
    percen_3 = (P1603.loc[1, 'P1603'] / tot_sim) * 100
    percen_4 = (P1604.loc[1, 'P1604'] / tot_sim) * 100
    percen_5 = (P1605.loc[1, 'P1605'] / tot_sim) * 100
    percen_6 = (P1606.loc[1, 'P1606'] / tot_sim) * 100
    percen_7 = (P1607.loc[1, 'P1607'] / tot_sim) * 100
    
    percen_9 = (P1609.loc[1, 'P1609'] / tot_sim) * 100
    percen_10 = (P1610.loc[1, 'P1610'] / tot_sim) * 100
    

    # criação de um Dataframe
    perguntas = [
        'Uso de álcool', 'Uso de drogas', 'Falta de dinheiro', 'Ciúmes', 'Traição conjugal',
        'Influência das amizades', 'Influência de familiares', 'Outros motivos', 'NS/NR'
    ]
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7, tot_9, tot_10]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7, percen_9, percen_10]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2009_P16(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    O que motivou a violência?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que motivou a violência?')
    plt.show()

# P17. Qual foi tipo de violência?
def dado2009_P17():
    '''
    Função que realiza a análise dos dados da 10ª pergunta do tema 2:
    Qual foi o tipo de violência sofrida?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise_coletiva = dados_2009df[['P171', 'P172', 'P173', 'P174', 'P175','P176']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P171 = analise_coletiva['P171'].value_counts().reset_index()
    P172 = analise_coletiva['P172'].value_counts().reset_index()
    P173 = analise_coletiva['P173'].value_counts().reset_index()
    P174 = analise_coletiva['P174'].value_counts().reset_index()
    P175 = analise_coletiva['P175'].value_counts().reset_index()
    P176 = analise_coletiva['P176'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = (
        P171.loc[0, 'P171']
        + P172.loc[1, 'P172']
        + P173.loc[1, 'P173']
        + P174.loc[1, 'P174']
        + P175.loc[1, 'P175']
        + P176.loc[1, 'P176']
    )
    
    # quantidade total de cada pergunta
    tot_1 = P171.loc[0, 'P171'] 
    tot_2 = P172.loc[1, 'P172'] 
    tot_3 = P173.loc[1, 'P173'] 
    tot_4 = P174.loc[1, 'P174'] 
    tot_5 = P175.loc[1, 'P175'] 
    tot_6 = P176.loc[1, 'P176']     

    # percentual para cada pergunta afirmativa
    percen_1 = (P171.loc[0, 'P171'] / tot_sim) * 100
    percen_2 = (P172.loc[1, 'P172'] / tot_sim) * 100
    percen_3 = (P173.loc[1, 'P173'] / tot_sim) * 100
    percen_4 = (P174.loc[1, 'P174'] / tot_sim) * 100
    percen_5 = (P175.loc[1, 'P175'] / tot_sim) * 100
    percen_6 = (P176.loc[1, 'P176'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Física', 'Sexual', 'Psicológica (ameaça, humilhação, chantagem)', 'Patrimonial (tirou ou destruiu seus bens)',
    'Moral (difamação, calúnia, injúria)', 'NS/NR']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2009_P17(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Qual foi tipo de violência?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual foi tipo de violência?')
    plt.show()

# P18. Quem foi o agressor? 
def dado2009_P18():
    '''
    Função que realiza a análise dos dados da 6ª pergunta do tema 2:
    Quem foi o agressor?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P18'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P18'] / analise['P18'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P18(anls):
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

# P19. Você ainda convive com ele? 
def dado2009_P19():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 2:
    Você ainda convive com o agressor?'''
    import pandas as pd

    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P19'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P19'] / analise['P19'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P19(anls):
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

# P21. Com que freqüência você sofre violência?
def dado2009_P21():
    '''
    Função que realiza a análise dos dados da 9ª pergunta do tema 2:
    Com qual frequência você sofre violência?'''
    import pandas as pd

    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P21'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P21'] / analise['P21'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P21(anls):
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

# P22. Qual foi a sua atitude em relação à última agressão?
def dado2009_P22():
    '''
    Função que realiza a análise dos dados da 7ª pergunta do tema 2:
    Qual foi sua atitude em relação à última agressão?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P22'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P22'] / analise['P22'].sum()) * 100
    
    analise.loc[4, 'Respostas'] = 'Denunciou em Delegacia da Mulher'
    
    return analise

def grafico2009_P22(anls):
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

# P24. Como foi o atendimento na delegacia?
def dado2009_P24():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 3:
    Como você avalia o atendimento recebido na delegacia?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P24'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P24'] / analise['P24'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P24(anls):
    '''
    Função que plota o gráfico da análise dos dados da 1ª pergunta do tema 3:
    Como você avalia o atendimento recebido na delegacia?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Como você avalia o atendimento recebido na delegacia?')
    plt.show()

# P25. Qual era a sua idade quando você foi agredida pela primeira vez? 
def dado2009_P25():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 2:
    Qual era a sua idade quando você foi agredida pela primeira vez?'''
    import pandas as pd

    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P25'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P25'] / analise['P25'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P25(anls):
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

# P26. O que você acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica e familiar contra a mulher?
def dado2009_P26():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 5:
    O que você acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica e familiar contra a mulher?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise_coletiva = dados_2009df[['P261', 'P262', 'P263', 'P264', 'P265','P266', 'P267', 'P268']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P261 = analise_coletiva['P261'].value_counts().reset_index()
    P262 = analise_coletiva['P262'].value_counts().reset_index()
    P263 = analise_coletiva['P263'].value_counts().reset_index()
    P264 = analise_coletiva['P264'].value_counts().reset_index()
    P265 = analise_coletiva['P265'].value_counts().reset_index()
    P266 = analise_coletiva['P266'].value_counts().reset_index()
    P267 = analise_coletiva['P267'].value_counts().reset_index()
    P268 = analise_coletiva['P268'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = (
        P261.loc[1, 'P261']
        + P262.loc[1, 'P262']
        + P263.loc[1, 'P263']
        + P264.loc[1, 'P264']
        + P265.loc[1, 'P265']
        + P266.loc[1, 'P266']
        + P267.loc[1, 'P267']
        + P268.loc[1, 'P268']
    )
    
    # quantidade total de cada pergunta
    tot_1 = P261.loc[1, 'P261'] 
    tot_2 = P262.loc[1, 'P262'] 
    tot_3 = P263.loc[1, 'P263'] 
    tot_4 = P264.loc[1, 'P264'] 
    tot_5 = P265.loc[1, 'P265'] 
    tot_6 = P266.loc[1, 'P266']
    tot_7 = P267.loc[1, 'P267']
    tot_8 = P268.loc[1, 'P268']     

    # percentual para cada pergunta afirmativa
    percen_1 = (P261.loc[1, 'P261'] / tot_sim) * 100
    percen_2 = (P262.loc[1, 'P262'] / tot_sim) * 100
    percen_3 = (P263.loc[1, 'P263'] / tot_sim) * 100
    percen_4 = (P264.loc[1, 'P264'] / tot_sim) * 100
    percen_5 = (P265.loc[1, 'P265'] / tot_sim) * 100
    percen_6 = (P266.loc[1, 'P266'] / tot_sim) * 100
    percen_7 = (P267.loc[1, 'P267'] / tot_sim) * 100
    percen_8 = (P268.loc[1, 'P268'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Denunciar', 'Intensificar as campanhas para divulgação dos direitos das mulheres'
    , 'Melhorar a assistência às vítimas', 'Capacitar lideranças comunitárias para que possam intervir nas emergências',
    'Outras opções', ' Estimular o debate social sobre o tema', ' Dividir de forma mais equilibrada as responsabilidades domésticas'
    , 'NS/NR']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7, tot_8]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7, percen_8]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2009_P26(anls):
    '''
    Função que plota o gráfico da análise dos dados da 2ª pergunta do tema 5:
    O que você acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica e familiar contra a mulher?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que você acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica e familiar contra a mulher?')
    plt.show()

# P27.  Você lembra de ter visto ou ouvido alguma campanha veiculada na mídia contra a violência às mulheres?
def dado2009_P27():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 4:
    Você lembra de ter visto ou ouvido alguma campanha veiculada na mídia contra a violência às mulheres?'''
    import pandas as pd
    dados_2009df = pd.read_csv("microdado_2009.csv", delimiter=';')

    analise = dados_2009df['P27'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P27'] / analise['P27'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2009_P27(anls):
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
