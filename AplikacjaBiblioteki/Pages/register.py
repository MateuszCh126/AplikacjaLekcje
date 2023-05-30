from flet import *
import flet as ft
class Register1(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page=page

    def build(self):
        return Column(
            controls=[
                Container( 
                    height=400,width=500,
                    bgcolor='Blue',
                    content=Column(
                        controls=[
                            Text('hejka zarejestruj'),
                            ElevatedButton("Logowanie", on_click=lambda _: self.page.go('/')),
                        ]
                    )
                )
            ]
            
        )
    def main(page: ft.Page):
        pass