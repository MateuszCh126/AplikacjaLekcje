import flet as ft
from flet import *
import sqlite3
import hashlib
#lączenie z baza danych
conn = sqlite3.connect('Uzytkownicy.db')

# utworzenie tabeli uzytkownicy
conn.execute("""
    CREATE TABLE IF NOT EXISTS uzytkownicy (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie TEXT NOT NULL,
        haslo TEXT NOT NULL,
        czy_admin INTEGER NOT NULL DEFAULT 0
    );
""")

# zapisanie zmian w bazie danych
conn.commit()

#strona wyswietlana 
def main(page: ft.Page):
    page.title = "logowanie"
    page.vertical_alignment = ft.MainAxisAlignment.START
    #logowanie tego typu
    def create_tuple():
        global Zaloguj
        Zaloguj = ft.Ref[Text]()
        global Nazwa
        Nazwa = ft.Ref[TextField]()
        global Hasło
        Hasło = ft.Ref[TextField]()
        return Zaloguj,Nazwa,Hasło
    Zaloguj,Nazwa,Hasło = create_tuple()
    page.add(
    ft.Column(controls=[
        ft.Text(ref=Zaloguj, value="Zaloguj sie", color="grey",text_align="CENTER",font_family='ARIAL'),
        ft.TextField(ref=Nazwa, label="Nazwa: ",text_align="left",width=300, autofocus=True),
        ft.TextField(ref=Hasło, label="Hasło: ",text_align="left", autofocus=True)
    ],alignment=ft.MainAxisAlignment.START))
    def button_clicked(e):
        page.add(ft.Text("Zalogowano!"))
        page.route = "index.py"
        page.update()

    page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked,))
#zabezpieczenie hasla bo to wiesz pro ludzie robia
def hash_password(password): 
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
    hashed_password = hash_password(Hasło)
ft.app(target=main)
conn.close()  