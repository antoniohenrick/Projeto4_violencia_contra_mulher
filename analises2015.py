import pandas as pd
import matplotlib.pyplot as plt

# Análise de Dados - 2015
# Dados Gerais
dados2015_df = pd.read_csv('microdado_2015.csv', delimiter=';')


# Tema: Percepção geral sobre violência contra a mulher - 01 
# De forma geral, você acha que as mulheres são tratadas com respeito no Brasil? - P04(Pergunta) / 01(Tema)
class P04:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P04'].value_counts())
    
    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
 
    self.analise = analise
  
  def grafico(self):
    x = list(self.analise['Resposta'])
    y = list(self.analise['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?')
    plt.show()
  

# Geral - P04 / 01(Tema)
dados2015_p04 = P04(dados2015_df)


# Onde você acha que as mulheres são menos respeitadas? - P05(Pergunta) / 01(Tema)
class P05:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P05'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Onde você acha que as mulheres são menos respeitadas?')
    plt.show()
    


# Geral - P05 / 01(Tema)
dados2015_p05 = P05(dados2015_df)


# Em sua opinião, nos últimos doze meses, como a violência doméstica e familiar se comportou? - P06(Pergunta) / 01(Tema)
class P06:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P06'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em sua opinião, nos últimos doze meses, como a violência doméstica e familiar se comportou?')
    plt.show()
  


# Geral - P06 / 01(Tema)
dados2015_p06 = P06(dados2015_df)


# O que leva uma mulher a não denunciar a agressão? - P09(Pergunta) / 01(Tema)
class P09:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = self.dados[['P091', 'P092', 'P093', 'P094', 'P095','P096', 'P097']]

    analise_coletiva = self.dados_resp
    analise_coletiva = analise_coletiva.reset_index()

    # divisão por perguntas
    P091 = analise_coletiva['P091'].value_counts()
    P092 = analise_coletiva['P092'].value_counts()
    P093 = analise_coletiva['P093'].value_counts()
    P094 = analise_coletiva['P094'].value_counts() 
    P095 = analise_coletiva['P095'].value_counts()
    P096 = analise_coletiva['P096'].value_counts()
    P097 = analise_coletiva['P097'].value_counts()

    # Fazendo reindexação para facilitar anánlise
    P091.index = [0, 1, 2]
    P092.index = [0, 1, 2]
    P093.index = [0, 1, 2]
    P094.index = [1, 0, 2]
    P095.index = [0, 1, 2]
    P096.index = [0, 1, 2]
    P097.index = [0, 1, 2]

    # quantidade de valores 'sim'
    tot_sim = P091.loc[1] + P092.loc[1] + P093.loc[1] + P094.loc[1] + P095.loc[1] + P096.loc[1] + P097.loc[1] 
        
    # quantidade total de cada pergunta
    tot_1 = P091.loc[1] 
    tot_2 = P092.loc[1] 
    tot_3 = P093.loc[1] 
    tot_4 = P094.loc[1] 
    tot_5 = P095.loc[1] 
    tot_6 = P096.loc[1] 
    tot_7 = P097.loc[1] 

    # percentual para cada pergunta afirmativa
    percen_1 = (P091.loc[1] / tot_sim) * 100
    percen_2 = (P092.loc[1] / tot_sim) * 100
    percen_3 = (P093.loc[1] / tot_sim) * 100
    percen_4 = (P094.loc[1] / tot_sim) * 100
    percen_5 = (P095.loc[1] / tot_sim) * 100
    percen_6 = (P096.loc[1] / tot_sim) * 100
    percen_7 = (P097.loc[1] / tot_sim) * 100


    # criação de um Dataframe
    perguntas = ['Não existir punição', 'Depender financeiramente do agressor', 'Não conhecer seus direitos', 'Ter medo do agressor', 'Preocupar-se com a criação dos filhos', 'Ter vergonha da agressão', 'Acreditar que seria a última vez']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)
    
    self.analise_df = analise_final_df

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que leva uma mulher a não denunciar a agressão?')
    plt.show()
  


# Geral - P09 / 01(Tema)
dados2015_p09 = P09(dados2015_df)


# Tema: Violência vivida / testemunhada - 02
# Você já sofreu algum tipo de violência doméstica ou familiar? - P19(Pergunta) / 02(Tema)
class P19:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P19'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    
    self.analise_df = analise
    
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você já sofreu algum tipo de violência doméstica ou familiar?')
    plt.show()
  


# Geral - P19 / 02(Tema)
dados2015_p19 = P19(dados2015_df)


# Qual era a sua idade quando você foi agredida pela primeira vez? - P30(Pergunta) / 02(Tema)
class P30:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P30'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual era a sua idade quando você foi agredida pela primeira vez?')
    plt.show()



# Geral - P30 / 02(Tema)
dados2015_p30 = P30(dados2015_df)


# Você convive com o agressor? - P23(Pergunta) / 02(Tema)
class P23:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P23'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    analise.iat[0,0] = 'NS/NR'
    
    self.analise_df = analise
  
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você convive com o agressor?')
    plt.show()



# Geral - P23 / 02(Tema)
dados2015_p23 = P23(dados2015_df)


# Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar? - P17 / 02(Tema)
class P17:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P17'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    
    self.analise_df = analise
  
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?')
    plt.show()
  


# Geral - P17 / 02(Tema)
dados2015_p17 = P17(dados2015_df)


# Quem foi o agressor? - P22(Pergunta) / 02(Tema)
class P22:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P22'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quem foi o agressor?')
    plt.show()
  

# Geral - P22 / 02(Tema)
dados2015_p22 = P22(dados2015_df)


# Qual foi sua atitude em relação à última agressão? - P26(Pergunta) / 02(Tema)
def dado2015_P26():
  # Função criada com objetivo de auxiliar na analise das respostas à pergunta.
  dados_2015df = pd.read_csv("novo_microdado_2015.csv", delimiter=';')

  analise = pd.DataFrame(dados_2015df['P26'].value_counts())
  analise.columns = ['Total']
  analise = analise.rename_axis('Resposta').reset_index()
  analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

  return analise

def grafico2015_P26(anls):
  x = list(anls['Resposta'])
  y = list(anls['Percentual'])

  plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
  plt.xlabel('N° de Respostas (em %)')
  plt.ylabel('Respostas')
  plt.title('Qual foi sua atitude em relação à última agressão?')
  plt.show()

# Geral - P26 / 02(Tema)
#grafico2015_P26(P26())

# O que motivou a violência? - P20(Pergunta) / 02(Tema)
class P20:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = self.dados[['P2001', 'P2002', 'P2003', 'P2004', 'P2005', 'P2009']]

    analise_coletiva = self.dados_resp
    analise_coletiva = analise_coletiva.reset_index()

    # divisão por perguntas
    P2_1 = analise_coletiva['P2001'].value_counts()
    P2_2 = analise_coletiva['P2002'].value_counts()
    P2_3 = analise_coletiva['P2003'].value_counts()
    P2_4 = analise_coletiva['P2004'].value_counts() 
    P2_5 = analise_coletiva['P2005'].value_counts()
    P2_9 = analise_coletiva['P2009'].value_counts()

    # Fazendo reindexação para facilitar anánlise
    P2_1.index = [2, 0, 1]
    P2_2.index = [2, 0, 1]
    P2_3.index = [2, 0, 1]
    P2_4.index = [2, 0, 1]
    P2_5.index = [2, 0, 1]
    P2_9.index = [2, 0, 1]

    # quantidade de valores 'sim'
    tot_sim = P2_1.loc[1] + P2_2.loc[1] + P2_3.loc[1] + P2_4.loc[1] + P2_5.loc[1] + P2_9.loc[1] 
        
    # quantidade total de cada pergunta
    tot_1 = P2_1.loc[1] 
    tot_2 = P2_2.loc[1]
    tot_3 = P2_3.loc[1] 
    tot_4 = P2_4.loc[1]
    tot_5 = P2_5.loc[1]
    tot_9 = P2_9.loc[1]

    # percentual para cada pergunta afirmativa
    percen_1 = (P2_1.loc[1] / tot_sim) * 100
    percen_2 = (P2_2.loc[1] / tot_sim) * 100
    percen_3 = (P2_3.loc[1] / tot_sim) * 100
    percen_4 = (P2_4.loc[1] / tot_sim) * 100
    percen_5 = (P2_5.loc[1] / tot_sim) * 100
    percen_9 = (P2_9.loc[1] / tot_sim) * 100


    # criação de um Dataframe
    perguntas = ['Uso de álcool', 'Uso de drogas', 'Falta de dinheiro', 'Ciúmes', 'Traição conjungal', 'Pedido de separação']
    total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_9]
    percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_9]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)

    self.analise_df = analise_final_df

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que motivou a violência?')
    plt.show()
  


# Geral - P20 / 02(Tema)
dados2015_p20 = P20(dados2015_df)

# Com qual frequência você sofre violência? - P25(Pergunta) / 02(Tema)
class P25:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P25'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Com qual frequência você sofre violência?')
    plt.show()
  


# Geral - P25 / 02(Tema)
dados2015_p25 = P25(dados2015_df)


# Qual foi o tipo de violência sofrida? - P21 / 02(Tema)
def dado2015_P21():
  # Função criada com objetivo de auxiliar na analise das respostas à pergunta.
  dados2015_df = pd.read_csv("novo_microdado_2015.csv", delimiter=';')

  analise_coletiva = dados2015_df[['P211', 'P212', 'P213', 'P214', 'P215']]
  analise_coletiva = analise_coletiva.reset_index()

  # divisão por perguntas
  P2_1 = analise_coletiva['P211'].value_counts()
  P2_2 = analise_coletiva['P212'].value_counts()
  P2_3 = analise_coletiva['P213'].value_counts()
  P2_4 = analise_coletiva['P214'].value_counts() 
  P2_5 = analise_coletiva['P215'].value_counts()

  # Fazendo reindexação para facilitar anánlise
  P2_1.index = [1, 0]
  P2_2.index = [0, 1]
  P2_3.index = [0, 1]
  P2_4.index = [0, 1]
  P2_5.index = [0, 1]

  # quantidade de valores 'sim'
  tot_sim = P2_1.loc[1] + P2_2.loc[1] + P2_3.loc[1] + P2_4.loc[1] + P2_5.loc[1]
      
  # quantidade total de cada pergunta
  tot_1 = P2_1.loc[1] 
  tot_2 = P2_2.loc[1]
  tot_3 = P2_3.loc[1] 
  tot_4 = P2_4.loc[1]
  tot_5 = P2_5.loc[1]

  # percentual para cada pergunta afirmativa
  percen_1 = (P2_1.loc[1] / tot_sim) * 100
  percen_2 = (P2_2.loc[1] / tot_sim) * 100
  percen_3 = (P2_3.loc[1] / tot_sim) * 100
  percen_4 = (P2_4.loc[1] / tot_sim) * 100
  percen_5 = (P2_5.loc[1] / tot_sim) * 100

  # criação de um Dataframe
  perguntas = ['Física', 'Sexual', 'Psicológica', 'Patrimonial', 'Moral']
  total = [tot_1, tot_2, tot_3, tot_4, tot_5]
  percentual = [percen_1, percen_2, percen_3, percen_4, percen_5]
  analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
  analise_final_df = pd.DataFrame(analise_final)

    
  return analise_final_df

def grafico2015_P21(anls):
  x = list(anls['Resposta'])
  y = list(anls['Percentual'])

  plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
  plt.xlabel('N° de Respostas (em %)')
  plt.ylabel('Respostas')
  plt.title('Qual foi o tipo de violência sofrida?')
  plt.show()

# Geral - P21 / 02(Tema)
#grafico2015_P21(P21())


# Tema: Atendimento e rede de apoio / denúncia - 03
# Como você avalia o atendimento recebido na delegacia? - P28(Pergunta) / 03(Tema)
class P28:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P28'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Como você avalia o atendimento recebido na delegacia?')
    plt.show()
  


# Geral - P28 / 03(Tema)
dados2015_p28 = P28(dados2015_df)


# Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades? - P08(Pergunta) / 03(Tema)
class P08:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P08'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    
    self.analise_df = analise
    
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades?')
    plt.show()
  


# Geral - P08 / 03(Tema)
dados2015_p08 = P08(dados2015_df)


# Após quantas ocorrências você procurou ajuda? - P31(Pergunta) / 03(Tema)
class P31:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P31'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise = analise.drop(0)
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Após quantas ocorrências você procurou ajuda?')
    plt.show()
  

# Geral - P31 / 03(Tema)
dados2015_p31 = P31(dados2015_df)


# Tema: Conhecimento e eficácia das leis (reconhecimento de ações/leis) - 04
# As leis brasileiras protegem as mulheres contra abusos e violências domésticas? - P10(Pergunta) / 04(Tema)
class P10:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P10'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('As leis brasileiras protegem as mulheres contra abusos e violências domésticas?')
    plt.show()
  


# Geral - P10 / 04(Tema)
dados2015_p10 = P10(dados2015_df)

# Já ouviu falar da Lei Maria da Penha? - P11(Pergunta) - 04(Tema)
class P11:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P11'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Já ouviu falar da Lei Maria da Penha?')
    plt.show()
  


# Geral - P11 / 04(Tema)
dados2015_p11 = P11(dados2015_df)

# Depois da Lei Maria da Penha, qual a situção da proteção da mulher? - P12 / 04(Tema)
class P12:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P12'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise = analise.drop(4)
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Depois da Lei Maria da Penha, qual a situção da proteção da mulher?')
    plt.show()
  


# Geral - P12 / 04(Tema)
dados2015_p12 = P12(dados2015_df)


# Tema: A sociedade e a violência doméstica e familiar - 05 
# Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar? - P07(Pergunta) / 05(Tema)
class P07:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = self.dados[['P071', 'P072', 'P073']]

    analise_coletiva = self.dados_resp
    analise_coletiva = analise_coletiva.reset_index()

    # divisão por perguntas
    P2_1 = analise_coletiva['P071'].value_counts()
    P2_2 = analise_coletiva['P072'].value_counts()
    P2_3 = analise_coletiva['P073'].value_counts()

    # Fazendo reindexação para facilitar anánlise
    P2_1.index = [1, 0]
    P2_2.index = [0, 1]
    P2_3.index = [1, 0]

    # quantidade de valores 'sim'
    tot_sim = P2_1.loc[1] + P2_2.loc[1] + P2_3.loc[1]
        
    # quantidade total de cada pergunta
    tot_1 = P2_1.loc[1] 
    tot_2 = P2_2.loc[1]
    tot_3 = P2_3.loc[1] 

    # percentual para cada pergunta afirmativa
    percen_1 = (P2_1.loc[1] / tot_sim) * 100
    percen_2 = (P2_2.loc[1] / tot_sim) * 100
    percen_3 = (P2_3.loc[1] / tot_sim) * 100

    # criação de um Dataframe
    perguntas = ['A vítima', 'As pessoas que presenciaram a agressão', 'Qualquer pessoa que tenha conhecimento do fato']
    total = [tot_1, tot_2, tot_3]
    percentual = [percen_1, percen_2, percen_3]
    analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
    analise_final_df = pd.DataFrame(analise_final)

    self.analise_df = analise_final_df

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar?')
    plt.show()
  

# Geral - P07 / 05(Tema)
dados2015_p07 = P07(dados2015_df)


# Se você presenciasse um ato de agressão contra uma mulher, você denunciaria? - P15(Pergunta) / 05(Tema)
class P15:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P15'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
   
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Se você presenciasse um ato de agressão contra uma mulher, você denunciaria?')
    plt.show()
  

# Geral - P15 / 05(Tema)
dados2015_p15 = P15(dados2015_df)







