import flet as ft
from flet import *
from Rejestracja import Logowanie
from logowanie import Zobaczymy

def views_handler(page):
    return {
        "/login":View(
            route="/login",
            controls=[
                Logowanie(page)
            ]
        ),
        "/zobacz":View(
            route="/zobacz",
            controls=[
                Zobaczymy(page)
            ]
        )
    }
