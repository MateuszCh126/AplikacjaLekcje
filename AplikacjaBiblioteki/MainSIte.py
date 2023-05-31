from flet import *
from views import views_handler
import flet as ft

from Pages.Login import Login1
print(type(Login1))
def main(page: Page):
    page.window_full_screen=True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )


    def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
            
    page.on_route_change = route_change
    page.go('/')
    page.on_view_pop = view_pop
    page.vertical_alignment.CENTER
ft.app(target=main)