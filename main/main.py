import flet as ft
from flet import *
import sqlite3
import hashlib
#lączenie z baza danych
global conn 
conn= sqlite3.connect('Uzytkownicy.db',check_same_thread=False)

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
        ft.TextField(ref=Hasło, label="Hasło: ",text_align="left",width=300 ,autofocus=True,password=True)
    ],alignment=ft.MainAxisAlignment.START))
    

    def button_clicked(e):
        conn= sqlite3.connect('Uzytkownicy.db',check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT imie , haslo FROM uzytkownicy WHERE imie ='{Nazwaa}' AND haslo ='{Hasłoo}'")
        result= cursor.fetchone()
        print(result)
        print(cursor)
        if result is not None :
            page.add(ft.Text("Zalogowano!1"))
            Nazwa, Hasło = result
            if cursor.execute("SELECT czy_admin FROM uzytkownicy WHERE czy_admin=1",):
                print('hej0')
                page.add(ft.Text("Użytkownik jest administratorem.!"))
                page.add(ft.Text("Zalogowano!"))
                
            else:
                print('hej1')
                page.add(ft.Text("Użytkownik NIE jest administratorem.!"))
                page.add(ft.Text("Zalogowano! ALE NIE ADMIN"))
                
        else:
            print('hej2')
            page.add(ft.Text("NIE Zalogowano! ZLE DANE")) 
    page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked,))

#zabezpieczenie hasla bo to wiesz pro ludzie robia TO DO REJESTRACJI BTW
# def hash_password(password): 
#     return hashlib.sha256(password.encode('utf-8')).hexdigest()

ft.app(target=main)
 