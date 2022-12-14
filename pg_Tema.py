import flet as ft
from flet import (Text, Page,Row, Container, Column, LinearGradient, Icon, Dropdown, 
ButtonStyle, icons, animation, column, Alignment,alignment, RadialGradient, View, BottomSheet)

#data
from analises2005 import *
from analises2007 import *
from analises2009 import *
from analises2011 import *
#from analises2013 import *
#from analises2015 import *
from analises2017 import *
#from analises2019 import *
#from analises2021 import *


from anos import*

from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("svg")  #impede da janela de abrir

def pagina():

    fig, ax = plt.subplots()   
    
    
    def download(e):   

        '''
        Função para baixar a imagem do gráfico
        '''                               
        plt.savefig('grafico.png', bbox_inches='tight')

    #Botões
    botao_pagina_inicial = Container( 
                ft.FilledButton(
                    "Voltar para a Página Inicial",
                        icon = "arrow_left", icon_color = "#5d5179",
                        width = 245, height = 40,
                        on_click = lambda e: e.page.go("/pg_inicial")
                    )
                ) 

    #BottomSheets
    ### TEMA 1###
    #01
    def t1p01(e):
        '''
        Função para abrir o bottom sheet
        '''
        bs_t1p01.open = True
        grafico = dados2005_p1.grafico() #2005
        #grafico = grafico2007_P3(dado2007_P3()) #2007
        #grafico = grafico2009_P01(dado2009_P01()) #2009
        #grafico = dados2011_p04.grafico() #2011
        bs_t1p01.update()

    
    bs_t1p01 = ft.BottomSheet(            
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa01_01(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #02
    def t1p02(e):
        bs_t1p02.open = True
        grafico = dados2011_p06.grafico() #2011
        bs_t1p02.update()


    bs_t1p02 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa01_02(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #03
    def t1p03(e):
        bs_t1p03.open = True
        grafico = grafico2007_P4(dado2007_P4()) #2007
        #grafico = grafico2009_P02(dado2009_P02()) #2009
        #grafico = dados2011_p05.grafico() #2011
        bs_t1p03.update()


    bs_t1p03 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa01_03(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #04
    def t1p04(e):
        bs_t1p04.open = True
        grafico = dados2011_p09.grafico() #2011        
        bs_t1p04.update()


    bs_t1p04 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa01_04(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)


    ### TEMA 2###

    #01
    def t2p01(e):
        bs_t2p01.open = True
        grafico = dados2005_p12.grafico() #2005
        #grafico = grafico2007_P14(dado2007_P14()) #2007 
        #grafico = dados2011_p20.grafico() #2011        
        bs_t2p01.update()

    bs_t2p01 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_01(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #02
    def t2p02(e):
        bs_t2p02.open = True
        grafico = dados2005_p15.grafico() #2005
        #grafico = grafico2007_P15(dado2007_P15()) #2007
        #grafico = grafico2009_P25(dado2009_P25()) #2009
        #grafico = dados2011_p31.grafico() #2011 
        bs_t2p02.update()

    bs_t2p02 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_02(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #03
    def t2p03(e):
        bs_t2p03.open = True
        grafico = grafico2007_P11(dado2007_P11()) #2007
        #grafico = grafico2009_P19(dado2009_P19()) #2009
        #grafico = dados2011_p24.grafico() #2011 
        bs_t2p03.update()

    bs_t2p03 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_03(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #04
    def t2p04(e):
        bs_t2p04.open = True
        grafico = grafico2009_P13(dado2009_P13()) #2009
        #grafico = dados2011_p18.grafico() #2011 
        bs_t2p04.update()

    bs_t2p04 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_04(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #05
    def t2p05(e):
        bs_t2p05.open = True
        bs_t2p05.update()

    bs_t2p05 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_05(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #06
    def t2p06(e):
        bs_t2p06.open = True
        grafico = dados2005_p16.grafico() #2005
        #grafico = grafico2007_P10(dado2007_P10()) #2007
        #grafico = grafico2009_P18(dado2009_P18()) #2009
        #grafico = dados2011_p23.grafico() #2011 
        bs_t2p06.update()

    bs_t2p06 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_06(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #07
    def t2p07(e):
        bs_t2p07.open = True
        grafico = grafico = grafico2005_P17(dado2005_P17()) #2005
        #grafico = grafico2007_P13(dado2007_P13()) #2007
        #grafico = grafico2009_P22(dado2009_P22()) #2009
        #grafico = grafico2011_P27(dado2011_P27()) #2011 
        bs_t2p07.update()

    bs_t2p07 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_07(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #08
    def t2p08(e):
        bs_t2p08.open = True
        grafico = grafico2007_P8(dado2007_P8()) #2007
        #grafico = grafico2009_P16( dado2009_P16) #2009
        #grafico = dados2011_p21.grafico() #2011 
        bs_t2p08.update()

    bs_t2p08 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_08(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #09
    def t2p09(e):
        bs_t2p09.open = True
        grafico = grafico2007_P12(dado2007_P12()) #2007
        #grafico = grafico2009_P21(dado2009_P21()) #2009
        #grafico = dados2011_p26.grafico() #2011 
        bs_t2p09.update()

    bs_t2p09 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_09(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #10
    def t2p10(e):
        bs_t2p10.open = True
        grafico = grafico2005_P11(dado2005_P11()) #2005
        #grafico =  grafico2007_P9(dado2007_P9()) #2007
        #grafico =  grafico2009_P17(dado2009_P17()) #2009
        #grafico =  grafico2011_P22(dado2011_P22()) #2011 
        bs_t2p10.update()

    bs_t2p10 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa02_10(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    ### TEMA 3###

    #01
    def t3p01(e):
        bs_t3p01.open = True
        grafico = dados2005_p18.grafico() #2005
        #grafico = grafico2007_P14(dado2007_P14()) #2007
        #grafico = grafico2009_P24(dado2009_P24()) #2009
        #grafico =  grafico2009_P29(dado2009_P17()) #2011
        bs_t3p01.update()

    bs_t3p01 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa03_01(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)
        
    #02
    def t3p02(e):
        bs_t3p02.open = True
        grafico = dados2011_p07.grafico() #2011         
        bs_t3p02.update()

    bs_t3p02 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa03_02(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #03
    def t3p03(e):
        bs_t3p03.open = True
        bs_t3p03.update()

    bs_t3p03 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa03_03(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #04 
    def t3p04(e):
        bs_t3p04.open = True
        bs_t3p04.update()

    bs_t3p04 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa03_04(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)
        
    #05
    def t3p05(e):
        bs_t3p05.open = True
        grafico = dados2011_p32.grafico() #2011  
        bs_t3p05.update()

    bs_t3p05 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa03_05(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    ### TEMA 4###

    #01
    def t4p01(e):
        bs_t4p01.open = True
        grafico = dados2005_p4.grafico() #2005
        #grafico = grafico2007_P5(dado2007_P5())#2007
        #grafico = grafico2009_P07(dado2009_P07()) #2009
        #grafico = dados2011_p10.grafico() #2011 
        

        bs_t4p01.update()

    bs_t4p01 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa04_01(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #02
    def t4p02(e):
        bs_t4p02.open = True
        grafico = grafico2007_P17(dado2007_P17()) #2007
        #grafico = grafico2009_P27(dado2009_P27()) #2009
        bs_t4p02.update()

    bs_t4p02 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa04_02(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #03
    def t4p03(e):
        bs_t4p03.open = True
        grafico = grafico2009_P08(dado2009_P08()) #2009
        #grafico = dados2011_p11.grafico() #2011
        bs_t4p03.update()

    bs_t4p03 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa04_03(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #04
    def t4p04(e):
        bs_t4p04.open = True
        grafico = dados2011_p12.grafico() #2011
        bs_t4p04.update()

    bs_t4p04 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa04_04(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #05
    def t4p05(e):
        bs_t4p05.open = True
        bs_t4p05.update()

    bs_t4p05 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa04_05(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #06
    def t4p06(e):
        bs_t4p06.open = True
        bs_t4p06.update()

    bs_t4p06 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa04_06(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #07
    def t4p07(e):
        bs_t4p07.open = True
        bs_t4p07.update()

    bs_t4p07 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa04_07(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    ### TEMA 5###

    #01
    def t5p01(e):
        bs_t5p01.open = True
        bs_t5p01.update()

    bs_t5p01 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa05_01(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #02
    def t5p02(e):
        bs_t5p02.open = True
        grafico = grafico2007_P16(dado2007_P16()) #2007
        #grafico = grafico2009_P26(dado2009_P26()) #2009

        bs_t5p02.update()

    bs_t5p02 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa05_02(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #03
    def t5p03(e):
        bs_t5p03.open = True
        grafico = grafico2009_P11(dado2009_P11()) #2009
        #grafico = dados2011_p14.grafico() #2011
        bs_t5p03.update()

    bs_t5p03 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa05_03(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    #04
    def t5p04(e):
        bs_t5p04.open = True
        grafico = dados2011_p16.grafico() #2011
        bs_t5p04.update()

    bs_t5p04 = ft.BottomSheet(
            Row(
                alignment= "start",
                controls=[
                    Column(
                        width = 350,
                        controls = [ 
                            Container(dpa05_04(),margin=10,width=150),
                            Container(ft.FilledButton("Busca"), margin=10, alignment= alignment.top_left)
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 500,
                        controls = [
                            Container(
                                MatplotlibChart(fig, expand=True),
                                alignment = alignment.center,
                                margin = 40
                            )
                        ]
                    ),
                    Column(
                        width = 500,
                        height = 1000,
                        alignment = "end",
                        controls = [
                            Container(
                                ft.FilledButton(text = "Download", on_click=download),

                                margin=20
                            )
                        ]
                    )
                ]
            ),
            open=False)

    # Botões

    ### TEMA 1###

    btt1p01 = Container(
            ft.FilledButton(
            text="De forma geral, você acha que as mulheres são tratadas com respeito no Brasil?", on_click=t1p01
                ),
            alignment = alignment.center,
            padding = 5,
            )
            
    btt1p02 = Container(
            ft.FilledButton(
            text="Em sua opinião, nos últimos doze meses, como a violência doméstica e familiar se comportou?", on_click = t1p02
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt1p03 = Container(
            ft.FilledButton(
            text="Onde você acha que as mulheres são menos respeitadas?", on_click = t1p03
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt1p04 = Container(
            ft.FilledButton(
            text="O que leva uma mulher a não denunciar a agressão?", on_click = t1p04
                ),
            alignment = alignment.center,
            padding = 5,
            )


    ### TEMA 2###

    btt2p01 = Container(
            ft.FilledButton(
            text="Você já sofreu algum tipo de violência doméstica ou familiar provocada por um homem?", on_click=t2p01
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p02 = Container(
            ft.FilledButton(
            text="Qual era a sua idade quando você foi agredida pela primeira vez?", on_click=t2p02
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p03 = Container(
            ft.FilledButton(
            text="Você convive com o agressor?", on_click=t2p03
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p04 = Container(
            ft.FilledButton(
            text="Você conhece alguma mulher que já sofreu algum tipo de violência doméstica ou familiar?", on_click=t2p04
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p05 = Container(
            ft.FilledButton(
            text="E essa violência ocorreu nos últimos 12 meses?", on_click=t2p05
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p06 = Container(
            ft.FilledButton(
            text="Quem foi o agressor?", on_click=t2p06
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p07 = Container(
            ft.FilledButton(
            text="Qual foi sua atitude em relação à última agressão?", on_click=t2p07
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p08 = Container(
            ft.FilledButton(
            text="O que motivou a violência?", on_click=t2p08
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p09 = Container(
            ft.FilledButton(
            text="Com qual frequência você sofre violência?", on_click=t2p09
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt2p10 = Container(
            ft.FilledButton(
            text="Qual foi o tipo de violência sofrida?", on_click=t2p10
                ),
            alignment = alignment.center,
            padding = 5,
            )

    ### TEMA 3###

    btt3p01 = Container(
            ft.FilledButton(
            text="Como você avalia o atendimento recebido na delegacia?", on_click=t3p01
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt3p02 = Container(
            ft.FilledButton(
            text="Em sua opinião, as mulheres que sofrem agressão costumam denunciar o fato às autoridades?", on_click=t3p02
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt3p03 = Container(
            ft.FilledButton(
            text="Por causa dessa violência, você buscou algum tipo de assistência de saúde?", on_click=t3p03
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt3p04 = Container(
        ft.FilledButton(
        text="Quais dos serviços de proteção à mulher prestados você conhece?", on_click=t3p04
            ),
        alignment = alignment.center,
        padding = 5,
        )

    btt3p05 = Container(
            ft.FilledButton(
            text="Após quantas ocorrências você procurou ajuda?", on_click=t3p05
                ),
            alignment = alignment.center,
            padding = 5,
            )
        

    ### TEMA 4###

    btt4p01 = Container(
            ft.FilledButton(
            text="As leis brasileiras protegem as mulheres contra abusos e violências domésticas?", on_click=t4p01
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt4p02 = Container(
            ft.FilledButton(
            text="Você lembra de ter visto ou ouvido alguma campanha veiculada na mídia contra a violência às mulheres?", on_click=t4p02
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt4p03 = Container(
            ft.FilledButton(
            text= "Já ouviu falar da Lei Maria da Penha?", on_click=t4p03
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt4p04 = Container(
            ft.FilledButton(
            text="Depois da Lei Maria da Penha, qual a situação da proteção da mulher?", on_click=t4p04
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt4p05 = Container(
            ft.FilledButton(
            text="Na sua opinião, o agressor deve ou não deve ser processado mesmo contra a vontade da vítima?", on_click=t4p05
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt4p06 = Container(
            ft.FilledButton(
            text="Você acha que a Lei Maria da Penha protege as mulheres contra a violência doméstica e familiar?", on_click=t4p06
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt4p07 = Container(
            ft.FilledButton(
            text="Quanto você conhece sobre a Lei Maria da Penha?", on_click=t4p07
                ),
            alignment = alignment.center,
            padding = 5,
            )

    ### TEMA 5###

    btt5p01 = Container(
            ft.FilledButton(
            text="Quão machista você considera o Brasil?", on_click=t5p01
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt5p02 = Container(
            ft.FilledButton(
            text="O que você acha que a sociedade pode fazer para diminuir ou evitar a violência doméstica e familiar contra a mulher?", on_click=t5p02
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt5p03 = Container(
            ft.FilledButton(
            text="Em sua opinião, quem pode denunciar um ato de agressão física cometido contra uma mulher em seu ambiente familiar?", on_click=t5p03
                ),
            alignment = alignment.center,
            padding = 5,
            )

    btt5p04 = Container(
            ft.FilledButton(
            text="Se você presenciasse um ato de agressão contra uma mulher, você denunciaria?", on_click=t5p04
                ),
            alignment = alignment.center,
            padding = 5,
            )

    ##### BOTÕES POR PERGUNTA###### 
    


    return View(
        "/pg_Tema", 
        scroll= ft.ScrollMode.AUTO,
        bgcolor= "#663d79",
        controls = [
            botao_pagina_inicial,
            
            Column(
                controls = [                    
                    ft.ResponsiveRow(
                        alignment ="center",
                        controls = [
                            Container( #Texto principal, título
                                #alignment = alignment.top_center,
                                content = Text(
                                "Percepção geral sobre violência contra as mulheres",
                                size = 16,
                                weight = "w500",
                                text_align= "center"
                                )
                            ),
                            btt1p01,
                            btt1p02,
                            btt1p03,
                            btt1p04,
                            Container( 
                                alignment = alignment.top_center,
                                content = Text(
                                "A violência vivida/testemunhada",
                                size = 16,
                                weight = "w500",
                                text_align= "center"
                                )
                            ),
                            btt2p01,
                            btt2p02,
                            btt2p03,
                            btt2p04,
                            btt2p05,
                            btt2p06,
                            btt2p07,
                            btt2p08,
                            btt2p09,
                            btt2p10,
                            Container( 
                                alignment = alignment.top_center,
                                content = Text(
                                "Atendimento e rede de apoio/denúncia",
                                size = 16,
                                weight = "w500",
                                text_align= "center"
                                )
                            ),        
                            btt3p01,
                            btt3p02,
                            btt3p03,
                            btt3p04,
                            btt3p05,
                            Container( 
                                alignment = alignment.top_center,
                                content = Text(
                                "Conhecimento e eficácia das leis (reconhecimento de ações/leis)",
                                size = 16,
                                weight = "w500",
                                text_align= "center"
                                )
                            ), 
                            btt4p01,
                            btt4p02,
                            btt4p03,
                            btt4p04,
                            btt4p05,
                            btt4p06,
                            btt4p07,
                            Container( 
                                alignment = alignment.top_center,
                                content = Text(
                                "A sociedade e a violência doméstica e familiar",
                                size = 16,
                                weight = "w500",
                                text_align= "center"
                                )
                            ),
                            btt5p01,
                            btt5p02,
                            btt5p03,
                            btt5p04,

                            #bottomsheets
                            bs_t1p01,
                            bs_t1p02,
                            bs_t1p03,
                            bs_t1p04,

                            bs_t2p01,
                            bs_t2p02,
                            bs_t2p03,
                            bs_t2p04,
                            bs_t2p05,
                            bs_t2p06,
                            bs_t2p07,
                            bs_t2p08,
                            bs_t2p09,
                            bs_t2p10,

                            bs_t3p01,
                            bs_t3p02,
                            bs_t3p03,
                            bs_t3p04,
                            bs_t3p05,

                            bs_t4p01,
                            bs_t4p02,
                            bs_t4p03,
                            bs_t4p04,
                            bs_t4p05,
                            bs_t4p06,
                            bs_t4p07,

                            bs_t5p01,
                            bs_t5p02,
                            bs_t5p03,
                            bs_t5p04
                       ]
                    )
                 ]   )                
        ]                                     
    )
