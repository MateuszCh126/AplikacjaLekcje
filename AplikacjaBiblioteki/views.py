import flet as ft
from flet import *
from Pages.Login import Login1
from Pages.register import Register1
from Pages.main import Main
def views_handler(page):
    return{
        '/':View(
            route='/',
            controls=[
                    Container(
                        Login1(page),
                        
                    )
                    ]
        ),
        '/Register':View(
            route='/Register',
            controls=[
                    Container(
                        Register1(page)
                    )
                    ]
        ),
        '/Main':View(
            route='/Main',
            controls=[ 
                Container(
                    Main(page)
                )
            ]
        )
    }