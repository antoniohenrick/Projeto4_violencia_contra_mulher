# Onde você acha que as mulheres são menos respeitadas? (P06) (tema 1)
def dado2017_P06():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 1:
    Onde você acha que as mulheres são menos respeitadas?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P05'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P05'] / analise['P05'].sum()) * 100
    respostas = ['Na rua', 'Na família', 'No trabalho']
    for i in range(3):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P06(anls):
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


# Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades: (P12)
def dado2017_P12():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 3:
    Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades:'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P08'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise_real = analise.loc[:4]
    analise_real.loc[3, 'P08'] += 2
    
    analise_real['Percentual'] = (analise_real['P08'] / analise_real['P08'].sum()) * 100
    respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    for i in range(len(respostas)):
        analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise_real

def grafico2017_P12(anls):
    '''
    Função que plota o gráfico da análise dos dados da 2ª pergunta do tema 3:
    Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades:'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades:')
    plt.show()

# Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar? (P21)
def dado2017_P21():
    '''
    Função que realiza a análise dos dados da 4ª pergunta do tema 2:
    Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P21'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P21'] / analise['P21'].sum()) * 100
    respostas = ['Sim', 'Não', 'NS/NR']
    for i in range(3):
        analise.loc[i, "Respostas"] = respostas[i]
       
    return analise

def grafico2017_P21(anls):
    '''
    Função que plota o gráfico da análise dos dados da 4ª pergunta do tema 2:
    Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?')
    plt.show()

# Em sua opinião, nos últimos doze meses, como a violência doméstica e familiar se comportou? (P08)
def dado2017_P08():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 1:
    Em sua opinião, nos últimos doze meses, como a violência doméstica e familiar se comportou?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P07'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P07'] / analise['P07'].sum()) * 100
    respostas = ['Aumentou', 'Continuou igual', 'Diminuiu', 'NS/NR']
    for i in range(4):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P08(anls):
    '''
    Função que plota o gráfico da análise dos dados da 2ª pergunta do tema 1:
    Em sua opinião, nos últimos doze meses, como a violência doméstica e familiar se comportou?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em sua opinião, nos últimos doze meses, como a violência doméstica e familiar se comportou?')
    plt.show()

# Quão machista você considera o Brasil? (P07)
def dado2017_P07():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 5:
    Quão machista você considera o Brasil?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P06'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise = analise.loc[:2]
    analise['Percentual'] = (analise['P06'] / analise['P06'].sum()) * 100
    respostas = ['Muito machista', 'Pouco machista', 'Nada machista']
    for i in range(3):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P07(anls):
    '''
    Função que plota o gráfico da análise dos dados da 1ª pergunta do tema 5:
    Quão machista você considera o Brasil?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quão machista você considera o Brasil?')
    plt.show()

# O que leva uma mulher a não denunciar a agressão? (P13)
def dado2017_P13():
    '''
    Função que realiza a análise dos dados da 4ª pergunta do tema 1:
    O que leva uma mulher a não denunciar a agressão?'''
    import pandas as pd
    
    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise_coletiva = dados_2017df[['P12', 'P1301', 'P1302', 'P1303', 'P1304','P1305', 'P1306', 'P1307', 'P1308']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P12 = analise_coletiva['P12'].value_counts().reset_index()
    P1301 = analise_coletiva['P1301'].value_counts().reset_index()
    P1302 = analise_coletiva['P1302'].value_counts().reset_index()
    P1303 = analise_coletiva['P1303'].value_counts().reset_index()
    P1304 = analise_coletiva['P1304'].value_counts().reset_index()
    P1305 = analise_coletiva['P1305'].value_counts().reset_index()
    P1306 = analise_coletiva['P1306'].value_counts().reset_index()
    P1307 = analise_coletiva['P1307'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = P12.loc[1, 'P12'] + P1301.loc[1,'P1301'] + P1302.loc[1, 'P1302'] + P1303.loc[0, 'P1303'] + P1304.loc[1, 'P1304'] + P1305.loc[1, 'P1305'] 
    + P1306.loc[1, 'P1306'] + P1307.loc[1, 'P1307']
    
    # quantidade total de cada pergunta
    tot_1 = P12.loc[1, 'P12'] 
    tot_2 = P1301.loc[1, 'P1301'] 
    tot_3 = P1302.loc[1, 'P1302'] 
    tot_4 = P1303.loc[0, 'P1303'] 
    tot_5 = P1304.loc[1, 'P1304'] 
    tot_6 = P1305.loc[1, 'P1305'] 
    tot_7 = P1306.loc[1, 'P1306'] 
    tot_8 = P1307.loc[1, 'P1307']
    

    # percentual para cada pergunta afirmativa
    percen_1 = (P12.loc[1, 'P12'] / tot_sim) * 100
    percen_2 = (P1301.loc[1, 'P1301'] / tot_sim) * 100
    percen_3 = (P1302.loc[1, 'P1302'] / tot_sim) * 100
    percen_4 = (P1303.loc[0, 'P1303'] / tot_sim) * 100
    percen_5 = (P1304.loc[1, 'P1304'] / tot_sim) * 100
    percen_6 = (P1305.loc[1, 'P1305'] / tot_sim) * 100
    percen_7 = (P1306.loc[1, 'P1306'] / tot_sim) * 100
    percen_8 = (P1307.loc[1, 'P1307'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Não existir punição', 'Depender financeiramente do agressor', 'Não conhecer seus direitos', 'Ter medo do agressor',
    'Preocupar-se com a criação dos filhos','Ter vergonha da agressão', 'Acreditar que seria a última vez',
    'Outros']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7, tot_8]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7, percen_8]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2017_P13(anls):
    '''
    Função que plota o gráfico da análise dos dados da 4ª pergunta do tema 1:
    O que leva uma mulher a não denunciar a agressão?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que leva uma mulher a não denunciar a agressão?')
    plt.show()

# Se você presenciasse um ato de agressão contra um mulher, você denunciaria? (P19)
def dado2017_P19():
    '''
    Função que realiza a análise dos dados da 4ª pergunta do tema 5:
    Se você presenciasse um ato de agressão contra um mulher, você denunciaria?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P16'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    
    analise['Percentual'] = (analise['P16'] / analise['P16'].sum()) * 100
    respostas = ['Sim', 'Não', 'NS/NR']
    for i in range(3):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P19(anls):
    '''
    Função que plota o gráfico da análise dos dados da 4ª pergunta do tema 5:
    Se você presenciasse um ato de agressão contra um mulher, você denunciaria?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Se você presenciasse um ato de agressão contra um mulher, você denunciaria?')
    plt.show()

# Você já sofreu algum tipo de violência doméstica ou familiar provocada por um homem?
def dado2017_P24():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 2:
    Você já sofreu algum tipo de violência doméstica ou familiar provocada por um homem?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P238'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    
    analise['Percentual'] = (analise['P238'] / analise['P238'].sum()) * 100
    respostas = ['Não', 'Sim', 'NS/NR']
    for i in range(3):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P24(anls):
    '''
    Função que plota o gráfico da análise dos dados da 1ª pergunta do tema 2:
    Você já sofreu algum tipo de violência doméstica ou familiar provocada por um homem?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você já sofreu algum tipo de violência doméstica ou familiar provocada por um homem?')
    plt.show()

# Qual foi o tipo de violência sofrida? (P25)
def dado2017_P25():
    '''
    Função que realiza a análise dos dados da 10ª pergunta do tema 2:
    Qual foi o tipo de violência sofrida?'''
    import pandas as pd
    
    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise_coletiva = dados_2017df[['P24', 'P251', 'P252', 'P253', 'P254','P255']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P24 = analise_coletiva['P24'].value_counts().reset_index()
    P251 = analise_coletiva['P251'].value_counts().reset_index()
    P252 = analise_coletiva['P252'].value_counts().reset_index()
    P253 = analise_coletiva['P253'].value_counts().reset_index()
    P254 = analise_coletiva['P254'].value_counts().reset_index()
    P255 = analise_coletiva['P255'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = P24.loc[1, 'P24'] + P251.loc[1,'P251'] + P252.loc[1, 'P252'] + P253.loc[1, 'P253'] + P254.loc[1, 'P254'] + P255.loc[1, 'P255']
    
    # quantidade total de cada pergunta
    tot_1 = P24.loc[1, 'P24'] 
    tot_2 = P251.loc[1, 'P251'] 
    tot_3 = P252.loc[1, 'P252'] 
    tot_4 = P253.loc[1, 'P253'] 
    tot_5 = P254.loc[1, 'P254'] 
    tot_6 = P255.loc[1, 'P255']     

    # percentual para cada pergunta afirmativa
    percen_1 = (P24.loc[1, 'P24'] / tot_sim) * 100
    percen_2 = (P251.loc[1, 'P251'] / tot_sim) * 100
    percen_3 = (P252.loc[1, 'P252'] / tot_sim) * 100
    percen_4 = (P253.loc[1, 'P253'] / tot_sim) * 100
    percen_5 = (P254.loc[1, 'P254'] / tot_sim) * 100
    percen_6 = (P255.loc[1, 'P255'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Física', 'Sexual', 'Psicológica (ameaça, humilhação, chantagem)', 'Patrimonial (tirou ou destruiu seus bens)',
    'Moral (difamação, calúnia, injúria)', 'Todas']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2017_P25(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Qual foi o tipo de violência sofrida?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual foi o tipo de violência sofrida?')
    plt.show()

# O que motivou a violência?
def dado2017_P26():
    '''
    Função que realiza a análise dos dados da 8ª pergunta do tema 2:
    O que motivou a violência?'''
    import pandas as pd
    
    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise_coletiva = dados_2017df[['P258', 'P2601', 'P2602', 'P2603', 'P2604','P2605', 'P2606', 'P2607', 'P2608', 'P2609', 'P2610', 'P2611', 'P2612']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P258 = analise_coletiva['P258'].value_counts().reset_index()
    P2601 = analise_coletiva['P2601'].value_counts().reset_index()
    P2602 = analise_coletiva['P2602'].value_counts().reset_index()
    P2603 = analise_coletiva['P2603'].value_counts().reset_index()
    P2604 = analise_coletiva['P2604'].value_counts().reset_index()
    P2605 = analise_coletiva['P2605'].value_counts().reset_index()
    P2606 = analise_coletiva['P2606'].value_counts().reset_index()
    P2607 = analise_coletiva['P2607'].value_counts().reset_index()
    P2608 = analise_coletiva['P2608'].value_counts().reset_index()
    P2609 = analise_coletiva['P2609'].value_counts().reset_index()
    P2610 = analise_coletiva['P2610'].value_counts().reset_index()
    P2611 = analise_coletiva['P2611'].value_counts().reset_index()
    P2612 = analise_coletiva['P2612'].value_counts().reset_index()


    # quantidade de valores 'sim'
    tot_sim = P258.loc[1, 'P258'] + P2601.loc[1,'P2601'] + P2602.loc[1, 'P2602'] + P2603.loc[1, 'P2603'] + P2604.loc[1, 'P2604']
    + P2606.loc[1, 'P2606'] + P2608.loc[1, 'P2608'] + P2609.loc[1, 'P2609'] + P2610.loc[1, 'P2610'] + P2611.loc[1, 'P2611'] 
    + P2612.loc[1, 'P2612']
    
    # quantidade total de cada pergunta
    tot_1 = P258.loc[1, 'P258'] 
    tot_2 = P2601.loc[1,'P2601'] 
    tot_3 = P2602.loc[1, 'P2602'] 
    tot_4 = P2603.loc[1, 'P2603'] 
    tot_5 = P2604.loc[1, 'P2604']
    tot_7 = P2606.loc[1, 'P2606']
    tot_9 = P2608.loc[1, 'P2608']
    tot_10 = P2609.loc[1, 'P2609']
    tot_11 = P2610.loc[1, 'P2610']
    tot_12 = P2611.loc[1, 'P2611']
    tot_13 = P2612.loc[1, 'P2612']

    # percentual para cada pergunta afirmativa
    percen_1 = (P258.loc[1, 'P258'] / tot_sim) * 100
    percen_2 = (P2601.loc[1,'P2601'] / tot_sim) * 100
    percen_3 = (P2602.loc[1, 'P2602'] / tot_sim) * 100
    percen_4 = (P2603.loc[1, 'P2603'] / tot_sim) * 100
    percen_5 = (P2604.loc[1, 'P2604'] / tot_sim) * 100
    percen_7 = (P2606.loc[1, 'P2606'] / tot_sim) * 100
    percen_9 = (P2608.loc[1, 'P2608'] / tot_sim) * 100
    percen_10 = (P2609.loc[1, 'P2609'] / tot_sim) * 100
    percen_11 = (P2610.loc[1, 'P2610'] / tot_sim) * 100
    percen_12 = (P2611.loc[1, 'P2611'] / tot_sim) * 100
    percen_13 = (P2612.loc[1, 'P2612'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Uso de álcool', 'Uso de drogas', 'Falta de dinheiro', 'Ciúmes','Traição conjugal',
    'Influência de familiares', 'Pedido de separação',
    'Índole do agressor', 'Briga/Discussão', 'Machismo', 'Outros motivos']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_7, tot_9, tot_10, tot_11, tot_12, tot_13]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_7, percen_9, percen_10, percen_11, percen_12, percen_13]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2017_P26(anls):
    '''
    Função que plota o gráfico da análise dos dados da 8ª pergunta do tema 2:
    O que motivou a violência?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que motivou a violência?')
    plt.show()

# Quem foi o agressor? (P27)
def dado2017_P27():
    '''
    Função que realiza a análise dos dados da 6ª pergunta do tema 2:
    Quem foi o agressor?'''
    import pandas as pd
    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise_coletiva = dados_2017df[['P2615', 'P2701', 'P2702', 'P2703', 'P2704','P2705', 'P2706', 'P2707', 'P2708', 'P2710', 'P2712', 'P2713', 'P2714', 'P2715']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P2615 = analise_coletiva['P2615'].value_counts().reset_index()
    P2701 = analise_coletiva['P2701'].value_counts().reset_index()
    P2702 = analise_coletiva['P2702'].value_counts().reset_index()
    P2703 = analise_coletiva['P2703'].value_counts().reset_index()
    P2704 = analise_coletiva['P2704'].value_counts().reset_index()
    P2705 = analise_coletiva['P2705'].value_counts().reset_index()
    P2706 = analise_coletiva['P2706'].value_counts().reset_index()
    P2707 = analise_coletiva['P2707'].value_counts().reset_index()
    P2708 = analise_coletiva['P2708'].value_counts().reset_index()
    P2710 = analise_coletiva['P2710'].value_counts().reset_index()
    P2712 = analise_coletiva['P2712'].value_counts().reset_index()
    P2713 = analise_coletiva['P2713'].value_counts().reset_index()
    P2714 = analise_coletiva['P2714'].value_counts().reset_index()
    P2715 = analise_coletiva['P2715'].value_counts().reset_index()


    # quantidade de valores 'sim'
    tot_sim = P2615.loc[1, 'P2615'] + P2701.loc[1,'P2701'] + P2702.loc[1, 'P2702'] + P2703.loc[1, 'P2703'] + P2704.loc[1, 'P2704'] + P2705.loc[1, 'P2705']
    + P2706.loc[1, 'P2706'] + P2707.loc[1, 'P2707'] + P2708.loc[1, 'P2708'] + P2710.loc[1, 'P2710']
    + P2712.loc[1, 'P2712'] + P2713.loc[1, 'P2713'] + P2714.loc[1, 'P2714'] + P2715.loc[1, 'P2715']
    
    # quantidade total de cada pergunta
    tot_1 = P2615.loc[1, 'P2615'] 
    tot_2 = P2701.loc[1,'P2701'] 
    tot_3 = P2702.loc[1, 'P2702'] 
    tot_4 = P2703.loc[1, 'P2703'] 
    tot_5 = P2704.loc[1, 'P2704']
    tot_6 = P2705.loc[1, 'P2705']
    tot_7 = P2706.loc[1, 'P2706']
    tot_8 = P2707.loc[1, 'P2707']
    tot_9 = P2708.loc[1, 'P2708']
    tot_11 = P2710.loc[1, 'P2710']
    tot_13 = P2712.loc[1, 'P2712']
    tot_14 = P2713.loc[1, 'P2713']
    tot_15 = P2714.loc[1, 'P2714']
    tot_16 = P2715.loc[1, 'P2715']

    # percentual para cada pergunta afirmativa
    percen_1 = (P2615.loc[1, 'P2615'] / tot_sim) * 100
    percen_2 = (P2701.loc[1,'P2701'] / tot_sim) * 100
    percen_3 = (P2702.loc[1, 'P2702'] / tot_sim) * 100
    percen_4 = (P2703.loc[1, 'P2703'] / tot_sim) * 100
    percen_5 = (P2704.loc[1, 'P2704'] / tot_sim) * 100
    percen_6 = (P2705.loc[1, 'P2705'] / tot_sim) * 100
    percen_7 = (P2706.loc[1, 'P2706'] / tot_sim) * 100
    percen_8 = (P2707.loc[1, 'P2707'] / tot_sim) * 100
    percen_9 = (P2708.loc[1, 'P2708'] / tot_sim) * 100
    percen_11 = (P2710.loc[1, 'P2710'] / tot_sim) * 100
    percen_13 = (P2712.loc[1, 'P2712'] / tot_sim) * 100
    percen_14 = (P2713.loc[1, 'P2713'] / tot_sim) * 100
    percen_15 = (P2714.loc[1, 'P2714'] / tot_sim) * 100
    percen_16 = (P2715.loc[1, 'P2715'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Marido/companheiro', 'Namorado', 'Ex-marido ou Ex-companheiro', 'Ex-namorado', 'Pai',
    'Padrasto', 'Amigo', 'Colega de trabalho', 'Enteado', 'Genro',
    'Sobrinho', 'Tio', 'Vizinho', 'Outro',]
    
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7, tot_8, tot_9, tot_11, tot_13, tot_14, tot_15, tot_16]

    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7, percen_8, percen_9, percen_11, percen_13, percen_14, percen_15, percen_16]

    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2017_P27(anls):
    '''
    Função que plota o gráfico da análise dos dados da 6ª pergunta do tema 2:
    Quem foi o agressor?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quem foi o agressor?')
    plt.show()

# E essa violência aconteceu nos últimos 12 meses?
def dado2017_P28():
    '''
    Função que realiza a análise dos dados da 5ª pergunta do tema 2:
    E essa violência aconteceu nos últimos 12 meses?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P2718'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    
    analise['Percentual'] = (analise['P2718'] / analise['P2718'].sum()) * 100
    respostas = ['Não', 'Sim', 'NS/NR']
    for i in range(3):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P28(anls):
    '''
    Função que plota o gráfico da análise dos dados da 5ª pergunta do tema 2:
    E essa violência aconteceu nos últimos 12 meses?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('E essa violência aconteceu nos últimos 12 meses?')
    plt.show()

# Por causa dessa violência, você buscou algum tipo de assistência de saúde?
def dado2017_P29():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 3:
    Por causa dessa violência, você buscou algum tipo de assistência de saúde?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P28'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    
    analise['Percentual'] = (analise['P28'] / analise['P28'].sum()) * 100
    respostas = ['Não', 'Sim', 'NS/NR']
    for i in range(3):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P29(anls):
    '''
    Função que plota o gráfico da análise dos dados da 5ª pergunta do tema 2:
    Por causa dessa violência, você buscou algum tipo de assistência de saúde?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Por causa dessa violência, você buscou algum tipo de assistência de saúde?')
    plt.show()

# Você ainda convive com o agressor? (P30)
def dado2017_P30():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 2:
    Você ainda convive com o agressor?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P29'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    
    analise['Percentual'] = (analise['P29'] / analise['P29'].sum()) * 100
    respostas = ['Não', 'Sim']
    for i in range(2):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P30(anls):
    '''
    Função que plota o gráfico da análise dos dados da 3ª pergunta do tema 2:
    Você ainda convive com o agressor?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você convive com o agressor?')
    plt.show()

# Qual foi sua atitude em relação a última agressão? (P31)
def dado2017_P31():
    '''
    Função que plota o gráfico da análise dos dados da 7ª pergunta do tema 2:
    Qual foi sua atitude em relação a última agressão?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise_coletiva = dados_2017df[['P32', 'P3101', 'P3102', 'P3103', 'P3104','P3105', 'P3106', 'P3107']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P32 = analise_coletiva['P32'].value_counts().reset_index()
    P3101 = analise_coletiva['P3101'].value_counts().reset_index()
    P3102 = analise_coletiva['P3102'].value_counts().reset_index()
    P3103 = analise_coletiva['P3103'].value_counts().reset_index()
    P3104 = analise_coletiva['P3104'].value_counts().reset_index()
    P3105 = analise_coletiva['P3105'].value_counts().reset_index()
    P3106 = analise_coletiva['P3106'].value_counts().reset_index()
    P3107 = analise_coletiva['P3107'].value_counts().reset_index()
    # quantidade de valores 'sim'
    tot_sim = P32.loc[1, 'P32'] + P3101.loc[1, 'P3101'] + P3102.loc[1, 'P3102'] + P3103.loc[1, 'P3103'] + P3104.loc[1, 'P3104'] + P3105.loc[1, 'P3105'] 
    + P3106.loc[1, 'P3106'] + P3107.loc[1, 'P3107']
    
    # quantidade total de cada pergunta
    tot_1 = P32.loc[1, 'P32'] 
    tot_2 = P3101.loc[1, 'P3101'] 
    tot_3 = P3102.loc[1, 'P3102']
    tot_4 = P3103.loc[1, 'P3103']
    tot_5 = P3104.loc[1, 'P3104'] 
    tot_6 = P3105.loc[1, 'P3105'] 
    tot_7 = P3106.loc[1, 'P3106'] 
    tot_8 = P3107.loc[1, 'P3107'] 

    # percentual para cada pergunta afirmativa
    percen_1 = (P32.loc[1, 'P32']  / tot_sim) * 100
    percen_2 = (P3101.loc[1, 'P3101'] / tot_sim) * 100
    percen_3 = (P3102.loc[1, 'P3102'] / tot_sim) * 100
    percen_4 = (P3103.loc[1, 'P3103'] / tot_sim) * 100
    percen_5 = (P3104.loc[1, 'P3104'] / tot_sim) * 100
    percen_6 = (P3105.loc[1, 'P3105'] / tot_sim) * 100
    percen_7 = (P3106.loc[1, 'P3106'] / tot_sim) * 100
    percen_8 = (P3107.loc[1, 'P3107'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Denunciou em uma Delegacia da Mulher', 'Denunciou em uma delegacia comum', 'Procurou ajuda dos amigos', 'Procurou ajuda da família',
    'Ligou para a Central de Atendimento à Mulher','Procurou a Igreja', 'Procurou uma associação ou entidade especializada (ONG)',
    'Não fez nada']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7, tot_8]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7, percen_8]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2017_P31(anls):
    '''
    Função que plota o gráfico da análise dos dados da 7ª pergunta do tema 2:
    Qual foi sua atitude em relação a última agressão?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual foi sua atitude em relação a última agressão?')
    plt.show()

# Qual era a sua idade quando você foi agredida pela primeira vez? (P32)
def dado2017_P32():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 2:
    Qual era a sua idade quando você foi agredida pela primeira vez?'''
    import pandas as pd

    dados_2017df = pd.read_csv("microdado_2017.csv", delimiter=';')

    analise = dados_2017df['P30'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    
    analise['Percentual'] = (analise['P30'] / analise['P30'].sum()) * 100
    respostas = ['20 a 29 anos', '30 a 39 anos', '0 a 15 anos', '18 a 19 anos', '15 a 17 anos', '40 a 49 anos',
    'Não sei', '50 a 59 anos','Prefiro não responder', '60 anos ou mais']
    for i in range(len(respostas)):
        analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2017_P32(anls):
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

