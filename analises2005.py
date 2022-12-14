import pandas as pd
import matplotlib.pyplot as plt

# Análise de Dados - 2005
# Dados Gerais
dados2005_df = pd.read_csv('microdado_2005.csv', delimiter=';')


# Tema: Percepção geral sobre violência contra a mulher - 01 
# De forma geral, você acha que as mulheres são tratadas com respeito no Brasil? - P1(Pergunta) / 01(Tema)
class P1:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P1'].value_counts())
    
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
  
  def tabela(self):
    print(self.analise)

# Geral - P1 / 01(Tema)
dados2005_p1 = P1(dados2005_df)


# Tema: Violência vivida / testemunhada - 02
# Você já sofreu algum tipo de violência doméstica ou familiar? - P12(Pergunta) / 02(Tema)
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
  
  def tabela(self):
    print(self.analise_df)

# Geral - P12 / 02(Tema)
dados2005_p12 = P12(dados2005_df)


# Qual era a sua idade quando você foi agredida pela primeira vez? - P15(Pergunta) / 02(Tema)
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
    plt.title('Qual era a sua idade quando você foi agredida pela primeira vez?')
    plt.show()

  def tabela(self):
    print(self.analise_df)

# Geral - P15 / 02(Tema)
dados2005_p15 = P15(dados2005_df)


# Quem foi o agressor? - P16(Pergunta) / 02(Tema)
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

    self.analise_df = analise

  def grafico(self):
    x = list(self.analise_df['Resposta'])
    y = list(self.analise_df['Percentual'])

    plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
    plt.xlabel('N° de Respostas (em %)')
    plt.ylabel('Respostas')
    plt.title('Quem foi o agressor?')
    plt.show()
  
  def tabela(self):
    print(self.analise_df)

# Geral - P16 / 02(Tema)
dados2005_p16 = P16(dados2005_df)


# Qual foi sua atitude em relação à última agressão? - P17(Pergunta) / 02(Tema)
def dado2005_P17():
  # Função criada com objetivo de auxiliar na analise das respostas à pergunta.
  dados_2005df = pd.read_csv("microdado_2005.csv", delimiter=';')

  analise = pd.DataFrame(dados_2005df['P17'].value_counts())
  analise.columns = ['Total']
  analise = analise.rename_axis('Resposta').reset_index()
  analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

  return analise

def grafico2005_P17(anls):
  x = list(anls['Resposta'])
  y = list(anls['Percentual'])

  plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
  plt.xlabel('N° de Respostas (em %)')
  plt.ylabel('Respostas')
  plt.title('Qual foi sua atitude em relação à última agressão?')
  plt.show()

# Geral - P17 / 02(Tema)
#grafico2005_P17(dado2005_P17())


# Qual foi o tipo de violência sofrida? - P11 / 02(Tema)
def dado2005_P11():
  # Função criada com objetivo de auxiliar na analise das respostas à pergunta.
  dados2005_df = pd.read_csv("microdado_2005.csv", delimiter=';')

  analise = pd.DataFrame(dados2005_df['P11'].value_counts())
  analise.columns = ['Total']
  analise = analise.rename_axis('Resposta').reset_index()
  analise['Percentual'] = (analise['Total'] / analise['Total'].sum()) * 100

  return analise

def grafico2005_P11(anls):
  x = list(anls['Resposta'])
  y = list(anls['Percentual'])

  plt.barh(x, y, height=0.4, align='center', color='blue', linewidth=0.9)
  plt.xlabel('N° de Respostas (em %)')
  plt.ylabel('Respostas')
  plt.title('Qual foi o tipo de violência sofrida?')
  plt.show()

# Geral - P11 / 02(Tema)
#grafico2005_P11(dado2005_P11())


# Tema: Atendimento e rede de apoio / denúncia - 03
# Como você avalia o atendimento recebido na delegacia? - P18(Pergunta) / 03(Tema)
class P18:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P18'].value_counts())

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
  
  def tabela(self):
    print(self.analise_df)

# Geral - P18 / 03(Tema)
dados2005_p18 = P18(dados2005_df)


# Tema: Conhecimento e eficácia das leis (reconhecimento de ações/leis) - 04
# As leis brasileiras protegem as mulheres contra abusos e violências domésticas? - P4(Pergunta) / 04(Tema)
class P4:
  # Classe utilizada para auxiliar na análise das respostas à pergunta 
  # Possui dois métodos:
  # .grafico() -> plotar o grafico da análise
  # .tabela() -> mostrar a tabela com as análies por item
  def __init__(self, dados):
    self.dados = dados
    self.dados_resp = pd.DataFrame(self.dados['P4'].value_counts())

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
  
  def tabela(self):
    print(self.analise_df)

# Geral - P4 / 04(Tema)
dados2005_p4 = P4(dados2005_df)


