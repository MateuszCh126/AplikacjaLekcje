import flet as ft
from flet import *
import sqlite3
import hashlib
#lączenie z baza danych
global conn 
conn= sqlite3.connect('Uzytkownicy.db')

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
    
    Zaloguj=ft.Text(value="Zaloguj sie1", color="grey",text_align="CENTER",font_family='ARIAL')
    Nazwa=ft.TextField(label="Nazwa: ",text_align="left",width=300, autofocus=True)
    Hasło=ft.TextField(label="Hasło: ",text_align="left", autofocus=True,password=True)
    print('hej')
    page.add(Zaloguj,Nazwa,Hasło)
    def button_clicked(e):
        cursor = conn.cursor()
        cursor.execute("SELECT imie , haslo FROM uzytkownicy WHERE imie ='{Nazwa}' AND haslo ='{Hasło}'")
        result= cursor.fetchone()
        print('hej')
        if result:
            print('hej')
            page.add(ft.Text("Zalogowano!1"))
            Nazwa, Hasło = result
            page.add(result)
            if cursor.execute("SELECT czy_admin FROM uzytkownicy WHERE czy_admin=1",):
                print('hej')
                page.add(ft.Text("Użytkownik jest administratorem.!"))
                page.add(ft.Text("Zalogowano!"))
            else:
                print('hej')
                page.add(ft.Text("Użytkownik NIE jest administratorem.!"))
                page.add(ft.Text("Zalogowano! ALE NIE ADMIN"))
        else:
            print('hej')
            page.add(ft.Text("NIE Zalogowano! ZLE DANE"))

    page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked,))
#zabezpieczenie hasla bo to wiesz pro ludzie robia TO DO REJESTRACJI BTW
def hash_password(password): 
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

ft.app(target=main)
conn.close()  