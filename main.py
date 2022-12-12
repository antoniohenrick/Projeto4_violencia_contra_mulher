import flet as ft
from flet import Page

from paginas.pg_inicial import pagina as v1
from paginas.pg_Tema import pagina as v2


def main(page: Page):

    '''
    Função básica de criação flet

    '''
    #Permitir o scroll da página
    page.scroll = "always" #não tá funcionando

    #Título da janela
    page.title = "Projeto 4" 


    pg_inicial = v1()
    pg_Tema = v2()

    #routing
    def route_change(route):

        '''
        Função de criação da página para visualização (Views), para navegação

        '''

        #criação de rotas, a partir do nome da view
        page.views.clear()
        if page.route == "/pg_Tema":
            page.views.append(pg_Tema)
        if page.route == "/pg_inicial":
            page.views.append(pg_inicial)
        
        page.update()

    #remove top view
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    #call the rout functions
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    #views   
    page.views.append(pg_Tema)
    page.views.append(pg_inicial)
    page.update()


ft.app(target=main)