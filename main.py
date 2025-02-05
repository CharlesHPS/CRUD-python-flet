import flet as ft
from controles.cabecalho import Cabecalho
from telas.rota import router
from useaction_table import create_table


def main(page: ft.Page):
    #Criar as tabelas do banco de dados
    create_table()

    page.scroll = "auto"
    page.theme_mode = "dark"
    page.appbar = Cabecalho(page) 
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body    
    )
    page.go('/inicio')

ft.app(target=main, assets_dir="assets")