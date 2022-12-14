# P04.De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?
def dado2013_P04():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 1:
    De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P04'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P04'] / analise['P04'].sum()) * 100
    # respostas = ['As vezes', 'Não', 'Sim', 'NS/NR']
    # for i in range(len(respostas)):
    #     analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2013_P04(anls):
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

# P05. Onde você acha que as mulheres são menos respeitadas?
def dado2013_P05():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 1:
    Onde você acha que as mulheres são menos respeitadas?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P05'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P05'] / analise['P05'].sum()) * 100
    # respostas = ['Na rua', 'Na família', 'No trabalho']
    # for i in range(3):
    #     analise.loc[i, "Respostas"] = respostas[i]
    
    return analise

def grafico2013_P05(anls):
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

# P07. Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar? 
def dado2013_P07():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 5:
    Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar? '''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise_coletiva = dados_2013df[['P071', 'P072', 'P073', 'P074']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P071 = analise_coletiva['P071'].value_counts().reset_index()
    P072 = analise_coletiva['P072'].value_counts().reset_index()
    P073 = analise_coletiva['P073'].value_counts().reset_index()
    P074 = analise_coletiva['P074'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = P071.loc[0, 'P071'] + P072.loc[1,'P072'] + P073.loc[0, 'P073'] + P074.loc[1, 'P074']
    
    # quantidade total de cada pergunta
    tot_1 = P071.loc[0, 'P071'] 
    tot_2 = P072.loc[1, 'P072'] 
    tot_3 = P073.loc[0, 'P073'] 
    tot_4 = P074.loc[1, 'P074'] 
    

    # percentual para cada pergunta afirmativa
    percen_1 = (P071.loc[0, 'P071'] / tot_sim) * 100
    percen_2 = (P072.loc[1, 'P072'] / tot_sim) * 100
    percen_3 = (P073.loc[0, 'P073'] / tot_sim) * 100
    percen_4 = (P074.loc[1, 'P074'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['A vítima', 'As pessoas que presenciaram a agressão', 'Qualquer pessoa que tenha conhecimento do fato'
    , 'Não sei/Prefiro não responder']
    total = [tot_1, tot_2, tot_3, tot_4]
    percentual = [percen_1, percen_2, percen_3, percen_4]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2013_P07(anls):
    '''
    Função que plota o gráfico da análise dos dados da 3ª pergunta do tema 5:
    Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar? '''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar?')
    plt.show()

# P08. Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades?
def dado2013_P08():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 3:
    Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades:'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P08'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P08'] / analise['P08'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P08(anls):
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

# P09. O que leva uma mulher a NÃO denunciar a agressão?
def dado2013_P09():
    '''
    Função que realiza a análise dos dados da 4ª pergunta do tema 1:
    O que leva uma mulher a não denunciar a agressão?'''
    import pandas as pd
    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise_coletiva = dados_2013df[['P091', 'P092', 'P093', 'P094', 'P095','P096', 'P097', 'P098']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P091 = analise_coletiva['P091'].value_counts().reset_index()
    P092 = analise_coletiva['P092'].value_counts().reset_index()
    P093 = analise_coletiva['P093'].value_counts().reset_index()
    P094 = analise_coletiva['P094'].value_counts().reset_index()
    P095 = analise_coletiva['P095'].value_counts().reset_index()
    P096 = analise_coletiva['P096'].value_counts().reset_index()
    P097 = analise_coletiva['P097'].value_counts().reset_index()
    P098 = analise_coletiva['P098'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = P091.loc[1, 'P091'] + P092.loc[1,'P092'] + P093.loc[1, 'P093'] + P094.loc[0, 'P094'] + P095.loc[1, 'P095'] + P096.loc[1, 'P096'] 
    + P097.loc[1, 'P097'] + P098.loc[1, 'P098']
    
    # quantidade total de cada pergunta
    tot_1 = P091.loc[1, 'P091'] 
    tot_2 = P092.loc[1, 'P092'] 
    tot_3 = P093.loc[1, 'P093'] 
    tot_4 = P094.loc[0, 'P094'] 
    tot_5 = P095.loc[1, 'P095'] 
    tot_6 = P096.loc[1, 'P096'] 
    tot_7 = P097.loc[1, 'P097'] 
    tot_8 = P098.loc[1, 'P098']
    

    # percentual para cada pergunta afirmativa
    percen_1 = (P091.loc[1, 'P091'] / tot_sim) * 100
    percen_2 = (P092.loc[1, 'P092'] / tot_sim) * 100
    percen_3 = (P093.loc[1, 'P093'] / tot_sim) * 100
    percen_4 = (P094.loc[0, 'P094'] / tot_sim) * 100
    percen_5 = (P095.loc[1, 'P095'] / tot_sim) * 100
    percen_6 = (P096.loc[1, 'P096'] / tot_sim) * 100
    percen_7 = (P097.loc[1, 'P097'] / tot_sim) * 100
    percen_8 = (P098.loc[1, 'P098'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Não existir punição', 'Depender financeiramente do agressor', 'Não conhecer seus direitos', 'Ter medo do agressor',
    'Preocupar-se com a criação dos filhos','Ter vergonha da agressão', 'Acreditar que seria a última vez',
    'Outros']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7, tot_8]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7, percen_8]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2013_P09(anls):
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

# P10. Você acha que as leis brasileiras protegem as mulheres contra a violência doméstica e familiar?
def dado2013_P10():
    '''
    Função que realiza a análise dos dados da 6ª pergunta do tema 4:
    Você acha que as leis brasileiras protegem as mulheres contra a violência doméstica e familiar?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P10'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P10'] / analise['P10'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P10(anls):
    '''
    Função que plota o gráfico da análise dos dados da 6ª pergunta do tema 4:
    Você acha que as leis brasileiras protegem as mulheres contra a violência doméstica e familiar?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você acha que as leis brasileiras protegem as mulheres contra a violência doméstica e familiar?')
    plt.show()

# P11. Você já ouviu falar da Lei Maria da Penha?
def dado2013_P11():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 4:
    Você já ouviu falar da Lei Maria da Penha?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P11'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P11'] / analise['P11'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P11(anls):
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

# P14. Na sua opinião, o agressor deve ou não deve ser processado mesmo contra a vontade da vítima?
def dado2013_P14():
    '''
    Função que realiza a análise dos dados da 5ª pergunta do tema 4:
    Na sua opinião, o agressor deve ou não deve ser processado mesmo contra a vontade da vítima?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P14'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P14'] / analise['P14'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P14(anls):
    '''
    Função que plota o gráfico da análise dos dados da 5ª pergunta do tema 4:
    Na sua opinião, o agressor deve ou não deve ser processado mesmo contra a vontade da vítima?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Na sua opinião, o agressor deve ou não deve ser processado mesmo contra a vontade da vítima?')
    plt.show()

# P15. Se você presenciasse um ato de agressão contra uma mulher, você denunciaria?
def dado2013_P15():
    '''
    Função que realiza a análise dos dados da 4ª pergunta do tema 5:
    Se você presenciasse um ato de agressão contra uma mulher, você denunciaria?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P15'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P15'] / analise['P15'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P15(anls):
    '''
    Função que plota o gráfico da análise dos dados da 4ª pergunta do tema 5:
    Se você presenciasse um ato de agressão contra uma mulher, você denunciaria?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Se você presenciasse um ato de agressão contra uma mulher, você denunciaria?')
    plt.show()

# P17.  Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?
def dado2013_P17():
    '''
    Função que realiza a análise dos dados da 4ª pergunta do tema 2:
    Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P17'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P17'] / analise['P17'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P17(anls):
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

# P18.  E qual foi o tipo de violência sofrida pela pessoa conhecida? 
def dado2013_P18():
    '''
    Função que realiza a análise dos dados da 10ª pergunta do tema 2:
    E qual foi o tipo de violência sofrida pela pessoa conhecida?'''
    import pandas as pd
    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise_coletiva = dados_2013df[['P181', 'P182', 'P183', 'P184', 'P185','P186']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P181 = analise_coletiva['P181'].value_counts().reset_index()
    P182 = analise_coletiva['P182'].value_counts().reset_index()
    P183 = analise_coletiva['P183'].value_counts().reset_index()
    P184 = analise_coletiva['P184'].value_counts().reset_index()
    P185 = analise_coletiva['P185'].value_counts().reset_index()
    P186 = analise_coletiva['P186'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = (
        P181.loc[0, 'P181']
        + P182.loc[1, 'P182']
        + P183.loc[1, 'P183']
        + P184.loc[1, 'P184']
        + P185.loc[1, 'P185']
        + P186.loc[1, 'P186']
    )
    
    # quantidade total de cada pergunta
    tot_1 = P181.loc[0, 'P181'] 
    tot_2 = P182.loc[1, 'P182'] 
    tot_3 = P183.loc[1, 'P183'] 
    tot_4 = P184.loc[1, 'P184'] 
    tot_5 = P185.loc[1, 'P185'] 
    tot_6 = P186.loc[1, 'P186']     

    # percentual para cada pergunta afirmativa
    percen_1 = (P181.loc[0, 'P181'] / tot_sim) * 100
    percen_2 = (P182.loc[1, 'P182'] / tot_sim) * 100
    percen_3 = (P183.loc[1, 'P183'] / tot_sim) * 100
    percen_4 = (P184.loc[1, 'P184'] / tot_sim) * 100
    percen_5 = (P185.loc[1, 'P185'] / tot_sim) * 100
    percen_6 = (P186.loc[1, 'P186'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Física', 'Sexual', 'Psicológica (ameaça, humilhação, chantagem)', 'Patrimonial (tirou ou destruiu seus bens)',
    'Moral (difamação, calúnia, injúria)', 'Todas']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2013_P18(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    E qual foi o tipo de violência sofrida pela pessoa conhecida?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('E qual foi o tipo de violência sofrida pela pessoa conhecida?')
    plt.show()

# P19. Você já foi vitima ou sofreu algum tipo de violência doméstica ou familiar provocada por um homem?
def dado2013_P19():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 2:
    Você já foi vitima ou sofreu algum tipo de violência doméstica ou familiar provocada por um homem?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P19'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P19'] / analise['P19'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]

    return analise

def grafico2013_P19(anls):
    '''
    Função que plota o gráfico da análise dos dados da 1ª pergunta do tema 2:
    Você já foi vitima ou sofreu algum tipo de violência doméstica ou familiar provocada por um homem?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você já foi vitima ou sofreu algum tipo de violência doméstica ou familiar provocada por um homem?')
    plt.show()

# P20. O que motivou essa violência?
def dado2013_P20():
    '''
    Função que realiza a análise dos dados da 8ª pergunta do tema 2:
    O que motivou a violência?'''
    import pandas as pd
    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise_coletiva = dados_2013df[['P2001', 'P2002', 'P2003', 'P2004', 'P2005','P2006', 'P2007', 'P2008', 'P2009', 'P2010']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P2001 = analise_coletiva['P2001'].value_counts().reset_index()
    P2002 = analise_coletiva['P2002'].value_counts().reset_index()
    P2003 = analise_coletiva['P2003'].value_counts().reset_index()
    P2004 = analise_coletiva['P2004'].value_counts().reset_index()
    P2005 = analise_coletiva['P2005'].value_counts().reset_index()
    P2006 = analise_coletiva['P2006'].value_counts().reset_index()
    P2007 = analise_coletiva['P2007'].value_counts().reset_index()
    P2008 = analise_coletiva['P2008'].value_counts().reset_index()
    P2009 = analise_coletiva['P2009'].value_counts().reset_index()
    P2010 = analise_coletiva['P2010'].value_counts().reset_index()


    # # quantidade de valores 'sim'
    tot_sim = (
        P2001.loc[1, 'P2001']
        + P2002.loc[1, 'P2002']
        + P2003.loc[1, 'P2003']
        + P2004.loc[1, 'P2004']
        + P2005.loc[1, 'P2005']
        + P2006.loc[1, 'P2006']
        + P2007.loc[1, 'P2007']
        + P2008.loc[1, 'P2008']
        + P2009.loc[1, 'P2009']
        + P2010.loc[1, 'P2010']
    )
    
    # quantidade total de cada pergunta
    tot_1 = P2001.loc[1, 'P2001'] 
    tot_2 = P2002.loc[1, 'P2002'] 
    tot_3 = P2003.loc[1, 'P2003'] 
    tot_4 = P2004.loc[1, 'P2004'] 
    tot_5 = P2005.loc[1, 'P2005']
    tot_6 = P2006.loc[1, 'P2006']
    tot_7 = P2007.loc[1, 'P2007']
    tot_8 = P2008.loc[1, 'P2008']
    tot_9 = P2009.loc[1, 'P2009']
    tot_10 = P2010.loc[1, 'P2010']

    # percentual para cada pergunta afirmativa
    percen_1 = (P2001.loc[1, 'P2001'] / tot_sim) * 100
    percen_2 = (P2002.loc[1, 'P2002'] / tot_sim) * 100
    percen_3 = (P2003.loc[1, 'P2003'] / tot_sim) * 100
    percen_4 = (P2004.loc[1, 'P2004'] / tot_sim) * 100
    percen_5 = (P2005.loc[1, 'P2005'] / tot_sim) * 100
    percen_6 = (P2006.loc[1, 'P2006'] / tot_sim) * 100
    percen_7 = (P2007.loc[1, 'P2007'] / tot_sim) * 100
    percen_8 = (P2008.loc[1, 'P2008'] / tot_sim) * 100
    percen_9 = (P2009.loc[1, 'P2009'] / tot_sim) * 100
    percen_10 = (P2010.loc[1, 'P2010'] / tot_sim) * 100
    

    # criação de um Dataframe
    perguntas = [
        'Uso de álcool', 'Uso de drogas', 'Falta de dinheiro', 'Ciúmes', 'Traição conjugal',
        'Influência das amizades', 'Influência de familiares', 'Vício em jogos', 'Pedido de separação', 'Outros motivos'
    ]
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7, tot_8, tot_9, tot_10]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7, percen_8, percen_9, percen_10]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2013_P20(anls):
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

# P21.  Qual foi o tipo de violência? 
def dado2013_P21():
    '''
    Função que realiza a análise dos dados da 10ª pergunta do tema 2:
    Qual foi o tipo de violência sofrida?'''
    import pandas as pd
    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise_coletiva = dados_2013df[['P211', 'P212', 'P213', 'P214', 'P215','P216']]
    analise_coletiva = analise_coletiva.reset_index()
    # divisão por perguntas
    P211 = analise_coletiva['P211'].value_counts().reset_index()
    P212 = analise_coletiva['P212'].value_counts().reset_index()
    P213 = analise_coletiva['P213'].value_counts().reset_index()
    P214 = analise_coletiva['P214'].value_counts().reset_index()
    P215 = analise_coletiva['P215'].value_counts().reset_index()
    P216 = analise_coletiva['P216'].value_counts().reset_index()

    # quantidade de valores 'sim'
    tot_sim = (
        P211.loc[0, 'P211']
        + P212.loc[1, 'P212']
        + P213.loc[1, 'P213']
        + P214.loc[1, 'P214']
        + P215.loc[1, 'P215']
        + P216.loc[1, 'P216']
    )
    
    # quantidade total de cada pergunta
    tot_1 = P211.loc[0, 'P211'] 
    tot_2 = P212.loc[1, 'P212'] 
    tot_3 = P213.loc[1, 'P213'] 
    tot_4 = P214.loc[1, 'P214'] 
    tot_5 = P215.loc[1, 'P215'] 
    tot_6 = P216.loc[1, 'P216']     

    # percentual para cada pergunta afirmativa
    percen_1 = (P211.loc[0, 'P211'] / tot_sim) * 100
    percen_2 = (P212.loc[1, 'P212'] / tot_sim) * 100
    percen_3 = (P213.loc[1, 'P213'] / tot_sim) * 100
    percen_4 = (P214.loc[1, 'P214'] / tot_sim) * 100
    percen_5 = (P215.loc[1, 'P215'] / tot_sim) * 100
    percen_6 = (P216.loc[1, 'P216'] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['Física', 'Sexual', 'Psicológica (ameaça, humilhação, chantagem)', 'Patrimonial (tirou ou destruiu seus bens)',
    'Moral (difamação, calúnia, injúria)', 'Todas']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    return analise_final_df

def grafico2013_P21(anls):
    '''
    Função que plota o gráfico da análise dos dados da 10ª pergunta do tema 2:
    Qual foi o tipo de violência?'''
    import matplotlib.pyplot as plt
    x = list(anls['Resposta'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual foi o tipo de violência?')
    plt.show()

# P22.  Quem foi o agressor? 
def dado2013_P22():
    '''
    Função que realiza a análise dos dados da 6ª pergunta do tema 2:
    Quem foi o agressor?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P22'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P22'] / analise['P22'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P22(anls):
    '''
    Função que plota o gráfico da análise dos dados da 6ª pergunta do tema 2:
    Quem foi o agressor?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quem foi o agressor?')
    plt.show()

# P23.  Você ainda convive com o agressor? 
def dado2013_P23():
    '''
    Função que realiza a análise dos dados da 3ª pergunta do tema 2:
    Você ainda convive com o agressor?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P23'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P23'] / analise['P23'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P23(anls):
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

# P25. Com qual frequência você sofre violência?
def dado2013_P25():
    '''
    Função que realiza a análise dos dados da 9ª pergunta do tema 2:
    Com qual frequência você sofre violência?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P25'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P25'] / analise['P25'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P25(anls):
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

# P26.  Qual foi sua atitude em relação à última agressão?
def dado2013_P26():
    '''
    Função que realiza a análise dos dados da 7ª pergunta do tema 2:
    Qual foi sua atitude em relação à última agressão?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P26'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P26'] / analise['P26'].sum()) * 100
    
    indic = [4, 7]
    for item in indic:
        if item == 4:
            analise.loc[item, 'Respostas'] = 'Outra opção'
        else:
            analise.loc[item, 'Respostas'] = 'NS/NR'

    return analise

def grafico2013_P26(anls):
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

# P28. Como você avalia o atendimento recebido na delegacia?
def dado2013_P28():
    '''
    Função que realiza a análise dos dados da 1ª pergunta do tema 3:
    Como você avalia o atendimento recebido na delegacia?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P28'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P28'] / analise['P28'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P28(anls):
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

# P30.  Qual era a sua idade quando você foi agredida pela primeira vez? 
def dado2013_P30():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 2:
    Qual era a sua idade quando você foi agredida pela primeira vez?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P30'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P30'] / analise['P30'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P30(anls):
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

# P31. Após quantos ocorrências você procurou ajuda?
def dado2013_P31():
    '''
    Função que realiza a análise dos dados da 2ª pergunta do tema 2:
    Após quantos ocorrências você procurou ajuda?'''
    import pandas as pd

    dados_2013df = pd.read_csv("microdado_2013.csv", delimiter=';')

    analise = dados_2013df['P31'].value_counts()
    analise = analise.rename_axis("Respostas").reset_index()
    analise['Percentual'] = (analise['P31'] / analise['P31'].sum()) * 100
    # respostas = ['Na minoria das vezes', 'Não denunciam', 'Na maioria das vezes', 'NS/NR', 'Sempre']
    # for i in range(len(respostas)):
    #     analise.loc[i, 'Respostas'] = respostas[i]
    
    return analise

def grafico2013_P31(anls):
    '''
    Função que plota o gráfico da análise dos dados da 2ª pergunta do tema 2:
    Após quantos ocorrências você procurou ajuda?'''
    import matplotlib.pyplot as plt
    x = list(anls['Respostas'])
    y = list(anls['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Após quantos ocorrências você procurou ajuda?')
    plt.show()
