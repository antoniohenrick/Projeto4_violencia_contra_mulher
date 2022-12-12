import flet as ft
from flet import (Text, Page, Row, Container, margin, Column, LinearGradient, column, Alignment, alignment, View, BottomSheet)

def pagina():

    '''
    Função de criação de página específica (view)

    '''
    pagina.scroll="always"
    return View (
        "/pg_inicial",
        bgcolor= "#663d79",
        controls = [
        
            ft.ResponsiveRow(
                alignment ="center",
                controls = [
                    Container( #Texto principal, título
                        col = {"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl":12},
                        alignment = alignment.top_center,
                        padding = 20,
                        content = Text(
                        "Pesquisa Violência doméstica e familiar \n contra a mulher - 2021",
                        size = 45,
                        weight = "w500",
                        text_align= "center"
                        )
                    ),

                    Container( #Subtítulo
                        col = {"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl":12},
                        alignment = alignment.top_center,
                        padding = 20,
                        content = Text(
                        "Plataforma interativa para visualização, análise e download dos resultados das pesquisas de opinião \n sobre violência contra a mulher realizadas pelo DataSenado, contendo dados de 2005 a 2021",
                        size = 20,
                        weight = "w400",
                        text_align= "center"
                        )
                    ),

                    Container( #Botão 
                                content=Text("Por Tema", size = 20, weight = "w400"),
                                margin=50,
                                padding=10,
                                gradient= LinearGradient(
                                    begin = alignment.top_right,
                                    end = alignment.bottom_left,
                                    colors = ["#745BA3","#571F4E"],
                                    ),
                                alignment=ft.alignment.center,
                                width=150,
                                height=150,
                                border_radius=10,
                                ink = True,
                                on_click = lambda e: e.page.go("/pg_Tema")
                            )
                ]
            ),
                
            
        ]
    )
    