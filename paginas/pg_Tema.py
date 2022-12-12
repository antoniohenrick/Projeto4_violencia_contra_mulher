import flet as ft
from flet import (Text, Page,Row, Container, Column, LinearGradient, Icon, Dropdown, 
ButtonStyle, icons, animation, column, Alignment,alignment, RadialGradient, View, BottomSheet)

def pagina():
    #Algumas funções precisam ser definidas aqui, antes de entrar no escopo do view
    #Ações ao clicar os botões do bottomsheet
    def abrir_janela(e):
        """
        Abrir a janela com os dados
        """
        bottom_Dados.open = True
        bottom_Dados.update()

    def fechar_janela(e):
        """
        Fechar a janela com os dados
        """
        bottom_Dados.open = False
        bottom_Dados.update()
    
    #Dropdown com os anos para o BottomSheet
    anos = Dropdown(
            width=10,
            hint_text = "Selecione o ano",
            border = "underline",
            text_size= 12,
            options = [
            ft.dropdown.Option("2005"), ft.dropdown.Option("2006"), 
            ft.dropdown.Option("2007"), ft.dropdown.Option("2008"), 
            ft.dropdown.Option("2009"), ft.dropdown.Option("2010"),
            ft.dropdown.Option("2011"), ft.dropdown.Option("2012"), 
            ft.dropdown.Option("2013"), ft.dropdown.Option("2014"), 
            ft.dropdown.Option("2015"), ft.dropdown.Option("2016"),
            ft.dropdown.Option("2017"), ft.dropdown.Option("2018"), 
            ft.dropdown.Option("2019"), ft.dropdown.Option("2020"), 
            ft.dropdown.Option("2021")]
        )

    #Poode ser que a gente precise fazer mais de um bottomsheet, um pra cada tema, mas só um copia e cola msm
    bottom_Dados = ft.BottomSheet(
        Row( #Uma linha geral que recebe COLUNAS cujo conteúdo são CONTAINERS
            alignment= "start",
            controls=[
                Column(
                    controls = [#Primeira coluna, tem o dropdown com os anos e o botão de busca 
                        Container(
                            anos,
                            margin=10,
                            width=150
                        ),
                        Container(#O botão pode ser que a gente faça a parte tbm, mas deixa assim só pra visusalizar
                            ft.FilledButton("Busca"),
                            margin=10,
                            alignment= alignment.top_left
                                )
                    ]
                ),
                Column(
                    width = 1000,
                    height = 1000,
                    controls = [
                        Container(
                            Text(f"O gráfico vai ficar por aqui, eu acho eeeeeeeeeeee"),
                            alignment = alignment.center,
                            margin = 40
                        )
                    ]
                ),
                Column(
                    height = 1000,
                    alignment = "end",
                    controls = [
                        Container(
                            ft.FilledButton(f"Download"),
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)


    #Dropdown com os temas (boteii assim pra tentar pegar o value depois, tipo tema1.value)
    tema1 = Dropdown(
            hint_text = "Percepção geral sobre violência contra as mulheres",
            width = 600,
            border = "underline",
            text_size= 15,
            options = [ ft.dropdown.Option("De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?"),
                        ft.dropdown.Option("Para você, nos últimos doze meses, a violência doméstica e familiar contra as mulheres:"),
                        ft.dropdown.Option("Onde você acha que as mulheres são menos respeitadas?"),
                        ft.dropdown.Option("O que leva uma mulher a não denunciar a agressão")]       
            )
    tema2 = Dropdown(
            hint_text = "A violência vivida/testemunhada",
            width = 600,
            border = "underline",
            text_size= 15,
            options=[
                ft.dropdown.Option("Você já sofreu algum tipo de violência doméstica ou familiar \n provocada por um homem?"),
                ft.dropdown.Option("Qual era a sua idade quando você foi agredida pela primeira vez?"),
                ft.dropdown.Option("Você convive com o agressor?"),
                ft.dropdown.Option("Você conhece alguma mulher que já sofreu algum tipo \n de violência doméstica ou familiar?"),
                ft.dropdown.Option("E essa violência ocorreu nos últimos 12 meses?"),
                ft.dropdown.Option("Quem foi o agressor?"),
                ft.dropdown.Option("Qual foi sua atitude em relação à última agressão?"),
                ft.dropdown.Option("O que motivou a violência?"),
                ft.dropdown.Option("Você sofre violência:"),
                ft.dropdown.Option("E qual foi o tipo de violência sofrida?")
                ],
            )
    tema3 = Dropdown(
            hint_text = "Atendimento e rede de apoio/denúncia",
            width = 600,
            border = "underline",
            text_size= 15,
            options=[
                ft.dropdown.Option("Como você avalia o atendimento recebido na delegacia?"),
                ft.dropdown.Option("Em sua opinião, as mulheres que sofrem agressão costumam denunciar o fato \nàs autoridades?"),
                ft.dropdown.Option("Por causa dessa violência, você buscou algum tipo de assistência de saúde?"),
                ft.dropdown.Option("Você conhece ou já ouviu falar dos serviços de proteção à mulher prestados:"),
                ft.dropdown.Option("Você procurou ajuda quando foi agredida na:")
                ],
            )
    tema4 = Dropdown(
            hint_text = "Conhecimento e eficácia das leis (reconhecimento de ações/leis)",
            width = 600,
            border = "underline",
            text_size= 15,
            options=[
                ft.dropdown.Option("As leis brasileiras protegem as mulheres contra abusos e violências domésticas?"),
                ft.dropdown.Option("Você lembra de ter visto ou ouvido alguma campanha veiculada na mídia contra \n a violência às mulheres?"),
                ft.dropdown.Option("Já ouviu falar da Lei Maria da Penha?"),
                ft.dropdown.Option("Depois da Lei Maria da Penha, a proteção da mulher está:"),
                ft.dropdown.Option("Na sua opinião, o agressor deve ou não deve ser processado mesmo \n contra a vontade da vítima?"),
                ft.dropdown.Option("Você acha que a Lei Maria da Penha protege as mulheres contra a \n violência doméstica e familiar?"),
                ft.dropdown.Option("Quanto você conhece sobre a Lei Maria da Penha:"),
                ],
            )
    tema5 = Dropdown(
            hint_text = "A sociedade e a violência doméstica e familiar",
            width = 600,
            border = "underline",
            text_size= 15,
            options=[
                ft.dropdown.Option("De forma geral, você considera o Brasil um país:"),
                ft.dropdown.Option("O que você acha que a sociedade pode fazer para diminuir ou evitar a violência \n doméstica e familiar contra a mulher?"),
                ft.dropdown.Option("Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma \n mulher em seu ambiente familiar?"),
                ft.dropdown.Option("Se você presenciasse um ato de agressão contra uma mulher, você denunciaria:")
                ],
            )

    #Botões (Vamo testar pôr como uma variável pra ver se rola o style)

    botao_pagina_inicial = Container( 
                ft.FilledTonalButton(
                    "Voltar para a Página Inicial",
                    style = ft.ButtonStyle(
                        color = "black",
                        bgcolor = "black"),
                        icon = "arrow_left", icon_color = "#5d5179",
                        width = 245, height = 40,
                        on_click = lambda e: e.page.go("/pg_inicial")
                    )
                )
    #####ESSES AQUUI TBM PRECISAM Ó######
    botao_busca1 = Container(
        ft.FilledButton(
        text="Mostrar dados", on_click=abrir_janela
            ),
        alignment = alignment.center,
        padding = 5,
        )
    botao_busca2 = Container(
        ft.FilledButton(
        text="Mostrar dados", on_click=abrir_janela
            ),
        alignment = alignment.center,
        padding = 5,
        )
    botao_busca3 = Container(
        ft.FilledButton(
        text="Mostrar dados", on_click=abrir_janela
            ),
        alignment = alignment.center,
        padding = 5,
        )
    botao_busca4 = Container(
        ft.FilledButton(
        text="Mostrar dados", on_click=abrir_janela
            ),
        alignment = alignment.center,
        padding = 5,
        )
    botao_busca5 = Container(
        ft.FilledButton(
        text="Mostrar dados", on_click=abrir_janela,
            ),
        alignment = alignment.center,
        padding = 5,
        )


    return View(
        "/pg_Tema", 
        bgcolor= "#663d79",
        controls = [
            botao_pagina_inicial,
            bottom_Dados,
            Column(
                controls = [                    
                    ft.ResponsiveRow(
                        alignment ="center",
                        controls = [
                            #Dropdowns (as msms config de container que tavam antes, só puxar os tema/drop que fica igual)
                            Container( #Tema 1
                                tema1,
                                col = {"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl":12},
                                alignment = alignment.top_center,
                                padding = 20
                            ),

                            #Boões de busca. Abaixo dos seus respectivos temas
                            botao_busca1,
                        
                            Container( #Tema 2
                                tema2,
                                col = {"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl":12},
                                alignment = alignment.top_center,
                                padding = 20,
                            ),
                            
                            botao_busca2,

                            Container( #Tema 3
                                tema3,
                                col = {"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl":12},
                                alignment = alignment.top_center,
                                padding = 20
                            ),
                            
                            botao_busca3,

                            Container( #Tema 4
                                tema4,
                                col = {"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl":12},
                                alignment = alignment.top_center,
                                padding = 20,
                            ),
                            
                            botao_busca4,

                            Container( #Tema 5
                                tema5,
                                col = {"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl":12},
                                alignment = alignment.top_center,
                                padding = 20,
                            ),

                            botao_busca5
                        ]                                     
                    ),
                ]
            )
        ]
    )
