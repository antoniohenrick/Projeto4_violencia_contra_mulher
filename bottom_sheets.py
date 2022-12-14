import flet as ft
from analises2017 import *
from anos import*
from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt
from flet import (Text, Row, Container, Column, Dropdown, ButtonStyle, Alignment,alignment, View, BottomSheet)

fig, ax = plt.subplots()

# nome das variáveis : (b)ottom(s)heet_(t)ema1(p)ergunta01 #

### TEMA 1###
#01
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#02
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#03
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#04
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)


### TEMA 2###

#01
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#02
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#03
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#04
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#05
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#06
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#07
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#08
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#09
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#10
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

### TEMA 3###

#01
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)
    
#02
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#03
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#04
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)
    
#05
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

### TEMA 4###

#01
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#02
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#03
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#04
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#05
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#06
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#07
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

### TEMA 5###

#01
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#02
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#03
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)

#04
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
                            ft.FilledButton(f"Download"),
                            #plt.savefig('imagem do grafico tal.png', bbox_inches='tight')
                            #plt.show()
                            margin=20
                        )
                    ]
                )
            ]
        ),
        open=False)


