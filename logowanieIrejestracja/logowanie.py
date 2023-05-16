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
def main(page: Page):
    page.title = "logowan32131ie"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #logowanie tego typu
    
    Zaloguj=ft.Text(value="Zaloguj sie1", color="grey",text_align="CENTER",font_family='ARIAL')
    txt_Nazwa=ft.TextField(label="Nazwa: ",text_align="left",width=300, autofocus=True)
    txt_Hasło=ft.TextField(label="Hasło: ",text_align="left", autofocus=True,password=True)
    print('stadasdsfafsafa')
    page.add(Zaloguj,txt_Nazwa,txt_Hasło)
    def button_clicked(e):
        if not txt_Nazwa.value:
            txt_Nazwa.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_Nazwa.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))
        if not txt_Hasło.value:
            txt_Hasło.error_text = "Please enter your name"
            page.update()
        else:
            password = txt_Hasło.value
            page.clean()
            page.add(ft.Text(f"Hello, {password}!"))
        def hash_password(password): 

            return hashlib.sha256(password.encode('utf-8')).hexdigest()

        hashed_password = hash_password(password)
        
        cursor = conn.cursor()
        cursor.execute(f"SELECT imie , haslo FROM uzytkownicy WHERE imie ='{name}' AND haslo ='{hashed_password}'")
        result= cursor.fetchone()
        
        if result:
            page.add(ft.Text("Zalogowano!1"))
            Nazwa, Hasło = result
            if cursor.execute("SELECT czy_admin FROM uzytkownicy WHERE czy_admin=1",):
                page.add(ft.Text("Użytkownik jest administratorem.!"))
                page.add(ft.Text("Zalogowano!"))
            else:
                page.add(ft.Text("Użytkownik NIE jest administratorem.!"))
                page.add(ft.Text("Zalogowano! ALE NIE ADMIN"))
        else:
            page.add(ft.Text("NIE Zalogowano! ZLE DANE"))

    page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked,))
#zabezpieczenie hasla bo to wiesz pro ludzie robia TO DO REJESTRACJI BTW

ft.app(target=main)
 