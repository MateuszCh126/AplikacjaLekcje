import flet as ft
from flet import *
import sqlite3
import hashlib

# lączenie z baza danych
global conn
conn = sqlite3.connect('Uzytkownicy.db', check_same_thread=False)

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


# strona wyswietlana
def main(page: ft.Page):
    page.title = "logowanie"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # logowanie tego typu

    Zaloguj = ft.Text(value="Zaloguj sie1", color="grey", text_align="CENTER", font_family='ARIAL')
    txt_Nazwa = ft.TextField(label="Nazwa: ", text_align="left", width=300, autofocus=True)
    txt_Hasło = ft.TextField(label="Hasło: ", text_align="left", autofocus=True, password=True)

    page.add(Zaloguj, txt_Nazwa, txt_Hasło)

    def button_clicked_login(e):
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

        cursor = conn.cursor()
        cursor.execute(f"SELECT imie , haslo FROM uzytkownicy WHERE imie ='{name}' AND haslo ='{password}'")
        result = cursor.fetchone()

        if result:

            page.add(ft.Text("Zalogowano!1"))
            Nazwa, Hasło = result
            if cursor.execute("SELECT czy_admin FROM uzytkownicy WHERE czy_admin=1", ):

                page.add(ft.Text("Użytkownik jest administratorem.!"))
                page.add(ft.Text("Zalogowano!"))
            else:

                page.add(ft.Text("Użytkownik NIE jest administratorem.!"))
                page.add(ft.Text("Zalogowano! ALE NIE ADMIN"))
        else:

            page.add(ft.Text("NIE Zalogowano! ZLE DANE"))




    def page_rejestracja(e):
        page.clean()
        page.update()
        Zarejestruj = ft.Text(value="Zaloguj sie1", color="grey", text_align="CENTER", font_family='ARIAL')
        txt_Login = ft.TextField(label="Nazwa: ", text_align="left", width=300, autofocus=True)
        txt_Haslo = ft.TextField(label="Hasło: ", text_align="left", autofocus=True, password=True)
        txt_Haslo2 = ft.TextField(label="Powtórz hasło: ", text_align="left", autofocus=True, password=True)
        page.add(Zarejestruj, txt_Login, txt_Haslo, txt_Haslo2)


        def button_clicked_rejestracja(e):
            if not txt_Login.value:
                txt_Login.error_text = "Please enter your name"
                page.update()
            else:
                Login = txt_Login.value
            if not txt_Haslo.value:
                txt_Haslo.error_text = "Please enter your password"
                page.update()
            else:
                Haslo = txt_Haslo.value
            if not txt_Haslo2.value:
                txt_Haslo2.error_text = "Please enter your password again"
                page.update()
            else:
                Haslo2 = txt_Haslo2.value

            if Haslo == Haslo2:
                cursor = conn.cursor()
                cursor.execute(f"INSERT INTO uzytkownicy (imie, haslo) VALUES ('{Login}', '{Haslo}')")
                conn.commit()
                page.add(ft.Text("Zarejestrowano!"))
            else:
                page.add(ft.Text("Hasła nie są takie same!"))

        page.add(ft.ElevatedButton(text="Zarejestruj się", on_click=button_clicked_rejestracja, ))

    page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked_login, ))
    page.add(ft.ElevatedButton(text="Zarejestruj się", on_click=page_rejestracja, ))

# zabezpieczenie hasla bo to wiesz pro ludzie robia TO DO REJESTRACJI BTW
def hash_paassword(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


ft.app(target=main)