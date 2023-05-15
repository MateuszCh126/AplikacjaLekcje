import flet as ft
from flet import *

def main(page: ft.Page):
    page.title = "logowanie"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(
    ft.Column(controls=[
        ft.Text(value="Zaloguj sie", color="grey",text_align="CENTER",font_family='ARIAL'),
        ft.TextField(label="Nazwa: ",text_align="left",width=300),
        ft.TextField(label="Hasło: ",text_align="left")
    ],alignment=ft.MainAxisAlignment.START))
    def button_clicked(e):
        page.add(ft.Text("Zalogowano!"))
        page.route = "C:\Users\gamin\OneDrive\Dokumenty\GitHub\AplikacjaLekcje\main\index.py"
        page.update()

    page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked,))
ft.app(target=main)  