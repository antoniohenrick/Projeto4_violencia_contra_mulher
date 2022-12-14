import pandas as pd
import matplotlib.pyplot as plt

# Análise de Dados - 2021
# Dados Gerais
dados2021_df = pd.read_csv('microdado_2021.csv', delimiter=';') 


# Tema: Percepção geral sobre violência contra a mulher - 01 
# De forma geral, você acha que as mulheres são tratadas com respeito no Brasil? - P03(Pergunta) / 01(Tema)
class P03:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P03'].value_counts())
    
    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    respostas = ['Não', 'Às vezes', 'Sim', 'NS/NR']
    for i in range(4):
      analise.loc[i, 'Resposta'] = respostas[i]
    self.analise = analise
  
  def grafico(self):
    x = list(self.analise['Resposta'])
    y = list(self.analise['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?')
    plt.show()
  

# Geral - P03 / 01(Tema)
dados2021_p03 = P03(dados2021_df)


# Onde você acha que as mulheres são menos respeitadas? - P04(Pergunta) / 01(Tema)
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
    analise = analise.loc[0:3]
    respostas = ['Na rua', 'Na família(em casa)', 'No trabalho', 'NS/NR']
    for i in range(4):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Onde você acha que as mulheres são menos respeitadas?')
    plt.show()
    

# Geral - P04 / 01(Tema)
dados2021_p04 = P04(dados2021_df)


# Para você, nos últimos doze meses, a violência doméstica e familiar contra as mulheres: - P06(Pergunta) / 01(Tema)
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
    respostas = ['Aumentou', 'Permaneceu igual', 'Diminuiu', 'NS/NR']
    for i in range(4):
        analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Para você, nos últimos doze meses, a violência doméstica e familiar contra as mulheres:')
    plt.show()
  

# Geral - P06 / 01(Tema)
dados2021_p06 = P06(dados2021_df)


# O que leva uma mulher a não denunciar a agressão? - P08(Pergunta) / 01(Tema)
class P08:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp1 = pd.DataFrame(self.dados['P08_1'].value_counts())
    self.dados_resp2 = pd.DataFrame(self.dados['P08_2'].value_counts())
    self.dados_resp3 = pd.DataFrame(self.dados['P08_3'].value_counts())
    self.dados_resp4 = pd.DataFrame(self.dados['P08_4'].value_counts())
    self.dados_resp5 = pd.DataFrame(self.dados['P08_5'].value_counts())
    self.dados_resp6 = pd.DataFrame(self.dados['P08_6'].value_counts())
    self.dados_resp7 = pd.DataFrame(self.dados['P08_7'].value_counts())

    # Analise - P08_1
    analise1 = self.dados_resp1
    analise1.columns = ['Total']
    analise1 = analise1.rename_axis('Resposta').reset_index()
    teste = analise1.shape
    if teste[0] == 3:
      analise1 = analise1.loc[0:1]
    analise1 = analise1.sort_values(by='Resposta', axis=0, ascending=True)
    analise1.index = [0, 1]
    analise1_total = analise1.loc[0, 'Total']

    # Analise - P08_2
    analise2 = self.dados_resp2
    analise2.columns = ['Total']
    analise2 = analise2.rename_axis('Resposta').reset_index()
    teste = analise2.shape
    if teste[0] == 3:
      analise2 = analise2.loc[0:1]
    analise2 = analise2.sort_values(by='Resposta', axis=0, ascending=True)
    analise2.index = [0, 1]
    analise2_total = analise2.loc[0, 'Total']

    # Analise - P08_3
    analise3 = self.dados_resp3
    analise3.columns = ['Total']
    analise3 = analise3.rename_axis('Resposta').reset_index()
    teste = analise3.shape
    if teste[0] == 3:
      analise3 = analise3.loc[0:1]
    analise3 = analise3.sort_values(by='Resposta', axis=0, ascending=True)
    analise3.index = [0, 1]
    analise3_total = analise3.loc[0, 'Total']

    # Analise - P08_4
    analise4 = self.dados_resp4
    analise4.columns = ['Total']
    analise4 = analise4.rename_axis('Resposta').reset_index()
    teste = analise4.shape
    if teste[0] == 3:
      analise4 = analise4.loc[0:1]
    analise4 = analise4.sort_values(by='Resposta', axis=0, ascending=True)
    analise4.index = [0, 1]
    analise4_total = analise4.loc[0, 'Total']

    # Analise - P08_5
    analise5 = self.dados_resp5
    analise5.columns = ['Total']
    analise5 = analise5.rename_axis('Resposta').reset_index()
    teste = analise5.shape
    if teste[0] == 3:
      analise5 = analise5.loc[0:1]
    analise5 = analise5.sort_values(by='Resposta', axis=0, ascending=True)
    analise5.index = [0, 1]
    analise5_total = analise5.loc[0, 'Total']

    # Analise - P08_6
    analise6 = self.dados_resp6
    analise6.columns = ['Total']
    analise6 = analise6.rename_axis('Resposta').reset_index()
    teste = analise6.shape
    if teste[0] == 3:
      analise6 = analise6.loc[0:1]
    analise6 = analise6.sort_values(by='Resposta', axis=0, ascending=True)
    analise6.index = [0, 1]
    analise6_total = analise6.loc[0, 'Total']

    # Analise - P08_7
    analise7 = self.dados_resp7
    analise7.columns = ['Total']
    analise7 = analise7.rename_axis('Resposta').reset_index()
    teste = analise7.shape
    if teste[0] == 3:
      analise7 = analise7.loc[0:1]
    analise7 = analise7.sort_values(by='Resposta', axis=0, ascending=True)
    analise7.index = [0, 1]
    analise7_total = analise7.loc[0, 'Total']

    # Soma total das respostas afirmativas para cada uma das declarações
    list_analises = [analise1_total, analise2_total, analise3_total, analise4_total, analise5_total, analise6_total, analise7_total]
    analise_total = sum(list_analises)

    # Percentual de cada uma das analises afirmativas
    analise1_percent = (analise1_total / analise_total) * 100 # P08_1
    analise2_percent = (analise2_total / analise_total) * 100 # P08_2
    analise3_percent = (analise3_total / analise_total) * 100 # P08_3
    analise4_percent = (analise4_total / analise_total) * 100 # P08_4
    analise5_percent = (analise5_total / analise_total) * 100 # P08_5
    analise6_percent = (analise6_total / analise_total) * 100 # P08_6
    analise7_percent = (analise7_total / analise_total) * 100 # P08_7

    # Criando novo dataframe
    final_df = analise1.copy()
    final_df = final_df.drop(1, axis=0)
    final_df.iat[0,0] = 'Não existir punição'
    final_df.iat[0,1] = analise1_total
    for i in range(6):
      final_df = final_df.append({'Resposta':None, 'Total':None}, ignore_index=True)
      
    respostas = ['Depender financeiramente do agressor', 'Não conhecer seus direitos', 'Ter medo do agressor', 'Preocupar-se com a criação dos filhos', 'Ter vergonha da agressão', 'Acreditar que seria a última vez']
    total = [analise2_total, analise3_total, analise4_total, analise5_total, analise6_total, analise7_total]
    i = 1
    for resp, tot in zip(respostas, total):
      final_df.loc[i, 'Resposta'] = resp
      final_df.loc[i, 'Total'] = tot
      i += 1
      
    final_df['Percentual'] = [analise1_percent, analise2_percent, analise3_percent, analise4_percent, analise5_percent, analise6_percent, analise7_percent]
    final_df = final_df.sort_values(by='Percentual', axis=0, ascending=False)
    
    self.analise_df = final_df

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('O que leva uma mulher a não denunciar a agressão?')
    plt.show()
  

# Geral - P08 / 01(Tema)
dados2021_p08 = P08(dados2021_df)


# Tema: Violência vivida / testemunhada - 02
# Você já sofreu algum tipo de violência doméstica ou familiar? - P18_A(Pergunta) / 02(Tema)
class P18:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P18_A'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    respostas = ['Não', 'Sim', 'NS/NR']
    for i in range(3):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise
    
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você já sofreu algum tipo de violência doméstica ou familiar?')
    plt.show()
  

# Geral - P18 / 02(Tema)
dados2021_p18 = P18(dados2021_df)


# Qual era a sua idade quando você foi agredida pela primeira vez? - P29(Pergunta) / 02(Tema)
class P29:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P29'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    respostas = ['20 a 29 anos', '30 a 39 anos', '0 a 15 anos', '18 a 19 anos', '16 a 17 anos', '40 a 49 anos', 'NS/NR', '50 a 59 anos', '60 anos ou mais']
    for i in range(9):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Qual era a sua idade quando você foi agredida pela primeira vez?')
    plt.show()


# Geral - P29 / 02(Tema)
dados2021_p29 = P29(dados2021_df)


# Você convive com o agressor? - P26(Pergunta) / 02(Tema)
class P26:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P26'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    respostas = ['Não', 'Sim', 'NS/NR']
    for i in range(3):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise
  
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você convive com o agressor?')
    plt.show()


# Geral - P26 / 02(Tema)
dados2021_p26 = P26(dados2021_df)


# Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar? - P16 / 02(Tema)
class P16:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P16'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    analise = analise.sort_values(by='Resposta', axis=0, ascending=True)
    analise.index = [0, 1, 2, 3]
    novo_tot = analise.loc[0, 'Total'] + analise.loc[1, 'Total']
    novo_percent = analise.loc[0, 'Percentual'] + analise.loc[1, 'Percentual']
    analise = analise.drop(0, axis=0)
    analise.index = [0, 1, 2]
    analise.iat[0,1] = novo_tot
    analise.iat[0,2] = novo_percent
    respostas = ['Sim', 'Não', 'NS/NR']
    for i in range(3):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise
  
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?')
    plt.show()
  


# Geral - P16 / 02(Tema)
dados2021_p16 = P16(dados2021_df)


# E essa violência ocorreu nos últimos 12 meses? - P23(Pergunta) / 02(Tema)
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
    analise = analise.sort_values(by='Resposta')
    analise.index = list(range(3))
    respostas = ['Sim', 'Não', 'NS/NR']
    for i in range(3):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('E essa violência ocorreu nos últimos 12 meses?')
    plt.show()
  

# Geral - P23 / 02(Tema)
dados2021_p23 = P23(dados2021_df)


# Quem foi o agressor? - P21_A(Pergunta) / 02(Tema)
class P21:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P21_A'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    analise = analise.sort_values(by='Resposta')
    analise.index = list(range(21))
    respostas = ['Marido/companheiro', 'Namorado', 'Ex-marido ou ex-companheiro', 'Ex-namorado', 'Pai', 'Padrasto', 'Amigo', 'Colega de trabalho', 'Cunhado', 'Filho', 'Genro', 'Sobrinho', 'Tio', 'Irmão', 'Vizinho', 'Outro', 'Primo', 'Avô', 'Familiar próximo ou não identificado', 'Sogro', 'NS/NR']
    for i in range(21):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quem foi o agressor?')
    plt.show()
  


# Geral - P21 / 02(Tema)
dados2021_p21 = P21(dados2021_df)


# Qual foi sua atitude em relação à última agressão? - P28(Pergunta) / 02(Tema)
def P28():
  # Função criada com objetivo de auxiliar na analise das respostas à pergunta.
  dados_2021df = pd.read_csv("microdado_2021.csv", delimiter=';')

  analise_coletiva = dados_2021df[['P28_1', 'P28_2', 'P28_3', 'P28_4', 'P28_5','P28_6', 'P28_7', 'P28_8']]
  analise_coletiva = analise_coletiva.reset_index()
  # divisão por perguntas
  P28_1 = analise_coletiva['P28_1'].value_counts()
  P28_2 = analise_coletiva['P28_2'].value_counts()
  P28_3 = analise_coletiva['P28_3'].value_counts()
  P28_4 = analise_coletiva['P28_4'].value_counts()
  P28_5 = analise_coletiva['P28_5'].value_counts()
  P28_6 = analise_coletiva['P28_6'].value_counts()
  P28_7 = analise_coletiva['P28_7'].value_counts()
  P28_8 = analise_coletiva['P28_8'].value_counts()
  # quantidade de valores 'sim'
  tot_sim = P28_1.loc[1] + P28_2.loc[1] + P28_3.loc[1] + P28_4.loc[1] + P28_5.loc[1] + P28_6.loc[1] + P28_7.loc[1] + P28_8.loc[1]
    
  # quantidade total de cada pergunta
  tot_1 = P28_1.loc[1] 
  tot_2 = P28_2.loc[1] 
  tot_3 = P28_3.loc[1] 
  tot_4 = P28_4.loc[1] 
  tot_5 = P28_5.loc[1] 
  tot_6 = P28_6.loc[1] 
  tot_7 = P28_7.loc[1] 
  tot_8 = P28_8.loc[1] 

  # percentual para cada pergunta afirmativa
  percen_1 = (P28_1.loc[1] / tot_sim) * 100
  percen_2 = (P28_2.loc[1] / tot_sim) * 100
  percen_3 = (P28_3.loc[1] / tot_sim) * 100
  percen_4 = (P28_4.loc[1] / tot_sim) * 100
  percen_5 = (P28_5.loc[1] / tot_sim) * 100
  percen_6 = (P28_6.loc[1] / tot_sim) * 100
  percen_7 = (P28_7.loc[1] / tot_sim) * 100
  percen_8 = (P28_8.loc[1] / tot_sim) * 100

  # criação de um Dataframe
  perguntas = ['Denunciou em uma Delegacia da Mulher', 'Denunciou em uma delegacia comum', 'Procurou ajuda dos amigos', 'Procurou ajuda da família',
  'Ligou para a Central de Atendimento à Mulher','Procurou a Igreja', 'Procurou uma associação ou entidade especializada (ONG)',
  'Não fez nada']
  total = [tot_1, tot_2, tot_3, tot_4, tot_5, tot_6, tot_7, tot_8]
  percentual = [percen_1, percen_2, percen_3, percen_4, percen_5, percen_6, percen_7, percen_8]
  analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
  analise_final_df = pd.DataFrame(analise_final)
    
  return analise_final_df

def grafico2021_P28(anls):
  x = list(anls['Resposta'])
  y = list(anls['Percentual'])

  plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
  plt.xlabel('N° de Respostas (em %)')
  plt.ylabel('Respostas')
  plt.title('Qual foi sua atitude em relação à última agressão?')
  plt.show()

# Geral - P28 / 02(Tema)
#grafico2021_P28(P28())


# Qual foi o tipo de violência sofrida? - P19 / 02(Tema)
def P19():
  # Função criada com objetivo de auxiliar na analise das respostas à pergunta.
  dados_2021df = pd.read_csv("microdado_2021.csv", delimiter=';')

  analise_coletiva = dados_2021df[['P19_1', 'P19_2', 'P19_3', 'P19_4', 'P19_5']]
  analise_coletiva = analise_coletiva.reset_index()
  # divisão por perguntas
  P19_1 = analise_coletiva['P19_1'].value_counts()
  P19_2 = analise_coletiva['P19_2'].value_counts()
  P19_3 = analise_coletiva['P19_3'].value_counts()
  P19_4 = analise_coletiva['P19_4'].value_counts()
  P19_5 = analise_coletiva['P19_5'].value_counts()
  
  # quantidade de valores 'sim'
  tot_sim = P19_1.loc[1] + P19_2.loc[1] + P19_3.loc[1] + P19_4.loc[1] + P19_5.loc[1]
  
  # quantidade total de cada pergunta
  tot_1 = P19_1.loc[1] 
  tot_2 = P19_2.loc[1] 
  tot_3 = P19_3.loc[1] 
  tot_4 = P19_4.loc[1] 
  tot_5 = P19_5.loc[1]

  # percentual para cada pergunta afirmativa
  percen_1 = (P19_1.loc[1] / tot_sim) * 100
  percen_2 = (P19_2.loc[1] / tot_sim) * 100
  percen_3 = (P19_3.loc[1] / tot_sim) * 100
  percen_4 = (P19_4.loc[1] / tot_sim) * 100
  percen_5 = (P19_5.loc[1] / tot_sim) * 100

  # criação de um Dataframe
  perguntas = ['Física','Sexual', 'Psicológica (ameaça, humilhação, chantagem)', 'Patrimonial (tirou ou destruiu seus bens)', 'Moral (difamação, calúnia, injúria)']
  total = [tot_1, tot_2, tot_3, tot_4, tot_5]
  percentual = [percen_1, percen_2, percen_3, percen_4, percen_5]
  analise_final = {'Resposta' : perguntas, 'Total' : total, 'Percentual' : percentual}
  analise_final_df = pd.DataFrame(analise_final)
    
  display(analise_final_df)
    
  return analise_final_df

def grafico2021_P19(anls):
  x = list(anls['Resposta'])
  y = list(anls['Percentual'])

  plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
  plt.xlabel('N° de Respostas (em %)')
  plt.ylabel('Respostas')
  plt.title('Qual foi o tipo de violência sofrida?')
  plt.show()

# Geral - P19 / 02(Tema)
#grafico2021_P19(P19())


# Tema: Atendimento e rede de apoio / denúncia - 03
# Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades: - P07(Pergunta) / 03(Tema)
class P07:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P07'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    analise = analise.sort_values(by='Resposta') # Organizando o dataframe por ordem das respostas
    analise.index = [0, 1, 2, 3, 4] # Reorganizando os indices do dataframe
    respostas = ['Sempre', 'Na maioria das vezes', 'Na minoria das vezes', 'Não denunciam', 'NS/NR']
    for i in range(5):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise
    
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Em sua opinião, as mulheres que sofrem agressão denunciam o fato às autoridades:')
    plt.show()
  

# Geral - P07 / 03(Tema)
dados2021_p07 = P07(dados2021_df)


# Por causa dessa violência, você buscou algum tipo de assistência de saúde? - P25(Pergunta) / 03(Tema)
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
    analise = analise.sort_values(by='Resposta')
    analise.index = [0, 1, 2]
    respostas = ['Sim', 'Não', 'NS/NR']
    for i in range(3):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise
    
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Por causa dessa violência, você buscou algum tipo de assistência de saúde?')
    plt.show()
  

# Geral - P25 / 03(Tema)
dados2021_p25 = P25(dados2021_df)


# Quais dos serviços de proteção à mulher prestados você conhece? - P12(Pergunta) / 03(Tema)
class P12:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp1 = pd.DataFrame(self.dados['P12_01'].value_counts())
    self.dados_resp2 = pd.DataFrame(self.dados['P12_02'].value_counts())
    self.dados_resp3 = pd.DataFrame(self.dados['P12_03'].value_counts())
    self.dados_resp4 = pd.DataFrame(self.dados['P12_04'].value_counts())

    # Analise - P12_01
    analise1 = self.dados_resp1
    analise1.columns = ['Total']
    analise1 = analise1.rename_axis('Resposta').reset_index()
    analise1['Percentual'] = (analise1['Total'] / analise1['Total'].sum()) * 100
    analise1_tot = analise1.loc[0, 'Total']

    # Analise - P12_02
    analise2 = self.dados_resp2
    analise2.columns = ['Total']
    analise2 = analise2.rename_axis('Resposta').reset_index()
    analise2['Percentual'] = (analise2['Total'] / analise2['Total'].sum()) * 100
    analise2_tot = analise2.loc[0, 'Total']

    # Analise - P12_03
    analise3 = self.dados_resp3
    analise3.columns = ['Total']
    analise3 = analise3.rename_axis('Resposta').reset_index()
    analise3['Percentual'] = (analise3['Total'] / analise3['Total'].sum()) * 100
    analise3_tot = analise3.loc[0, 'Total']

    # Analise - P12_04
    analise4 = self.dados_resp4
    analise4.columns = ['Total']
    analise4 = analise4.rename_axis('Resposta').reset_index()
    analise4['Percentual'] = (analise4['Total'] / analise4['Total'].sum()) * 100
    analise4_tot = analise4.loc[1, 'Total']

    # Soma total das respostas afirmativas para cada uma das declarações
    list_analises = [analise1_tot, analise2_tot, analise3_tot, analise4_tot]
    analise_total = sum(list_analises)

    # Percentual de cada uma das analises afirmativas
    analise1_percent = (analise1_tot / analise_total) * 100 # P12_01
    analise2_percent = (analise2_tot / analise_total) * 100 # P12_02
    analise3_percent = (analise3_tot / analise_total) * 100 # P12_03
    analise4_percent = (analise4_tot / analise_total) * 100 # P12_04

    # Criando novo dataframe
    final_df = analise1.copy()
    final_df = final_df.drop(1, axis=0)
    final_df.iat[0,0] = 'Delegacia da Mulher'
    final_df.iat[0,1] = analise1_tot
    for i in range(2):
      final_df = final_df.append({'Resposta':None, 'Total':None}, ignore_index=True)
          
    respostas = ['Defensoria Pública', 'Casas Abrigo', 'Casa da Mulher Brasileira']
    total = [analise2_tot, analise3_tot, analise4_tot]
    i = 1
    for resp, tot in zip(respostas, total):
      final_df.loc[i, 'Resposta'] = resp
      final_df.loc[i, 'Total'] = tot
      i += 1
          
    final_df['Percentual'] = [analise1_percent, analise2_percent, analise3_percent, analise4_percent]
    final_df = final_df.sort_values(by='Percentual', axis=0, ascending=False)

    self.analise_df = final_df

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quais dos serviços de proteção à mulher prestados você conhece?')
    plt.show()
  

# Geral - P12 / 03(Tema)
dados2021_p12 = P12(dados2021_df)


# Tema: Conhecimento e eficácia das leis (reconhecimento de ações/leis) - 04
# Você acha que a Lei Maria da Penha protege as mulheres contra a violência doméstica e familiar? - P10(Pergunta) / 04(Tema)
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
    analise = analise.sort_values(by='Resposta')
    analise.index = list(range(4))
    respostas = ['Sim', 'Em parte', 'Não', 'NS/NR']
    for i in range(4):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Você acha que a Lei Maria da Penha protege as mulheres contra a violência doméstica e familiar?')
    plt.show()
  

# Geral - P10 / 04(Tema)
dados2021_p10 = P10(dados2021_df)


# Quanto você conhece sobre a Lei Maria da Penha? - P09(Pergunta) / 04(Tema)
class P09:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P09'].value_counts())

    analise = self.dados_resp
    analise.columns = ['Total']
    analise = analise.rename_axis('Resposta').reset_index()
    analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100
    analise = analise.sort_values(by='Resposta')
    analise.index = list(range(4))
    respostas = ['Muito', 'Pouco', 'Nada', 'NS/NR']
    for i in range(4):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise
  
  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quanto você conhece sobre a Lei Maria da Penha?')
    plt.show()
  

# Geral - P09 / 04(Tema)
dados2021_p09 = P09(dados2021_df)


# Tema: A sociedade e a violência doméstica e familiar - 05
# Quão machista você considera o Brasil? - P05(Pergunta) / 05(Tema)
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
    analise = analise.sort_values(by='Resposta')
    analise.index = list(range(4))
    respostas = ['Muito machista', 'Pouco machista', 'Nada machista', 'NS/NR']
    for i in range(4):
      analise.loc[i, 'Resposta'] = respostas[i]
    
    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quão machista você considera o Brasil?')
    plt.show()
  

# Geral - P05 / 05(Tema)
dados2021_p05 = P05(dados2021_df)











