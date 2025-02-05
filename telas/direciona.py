from typing import Callable, Any
import flet as ft




class Direciona:
    def __init__(self,):

        self.direc = {}
        self.body = ft.Container()

    def set_route(self, stub: str, view: Callable):
        self.direc[stub] = view
    
    def set_routes(self, route_dictionary: dict):
        """Sets multiple direc at once. Ex: {"/": IndexView }"""
        self.direc.update(route_dictionary)

    def route_change(self, route):
        _page = route.route.split("?")[0]

        self.body.content = self.direc[_page](self)
        self.body.update()