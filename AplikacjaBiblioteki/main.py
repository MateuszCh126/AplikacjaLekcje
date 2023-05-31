import flet as ft
from flet import *
import sqlite3
import hashlib

# lączenie z baza danych
global conn
conn = sqlite3.connect('Biblioteka.db', check_same_thread=False)

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
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # logowanie tego typu
    def zaloguj_page():
        page.clean()
        page.update()
        Zaloguj = ft.Text(value="Zaloguj sie1", color="grey", text_align="CENTER", font_family='ARIAL')
        txt_Nazwa = ft.TextField(label="Nazwa: ", text_align="left", width=300, autofocus=True)
        txt_Hasło = ft.TextField(label="Hasło: ", text_align="left", autofocus=True, password=True,width=300)

        page.add(Zaloguj, txt_Nazwa, txt_Hasło)

        def button_clicked_login(e):
            page.clean()
            page.update()
            page.add(Zaloguj, txt_Nazwa, txt_Hasło)
            page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked_login, ))
            page.add(ft.ElevatedButton(text="Zarejestruj się", on_click=page_rejestracja, ))
            if not txt_Nazwa.value:
                txt_Nazwa.error_text = "Please enter your name"
                page.update()
            else:
                name = txt_Nazwa.value
                page.clean()
            if not txt_Hasło.value:
                txt_Hasło.error_text = "Please enter your name"
                page.update()
            else:
                password = txt_Hasło.value
                page.clean()

            def hash_password(password):

                return hashlib.sha256(password.encode('utf-8')).hexdigest()

            hashed_password = hash_password(password)

            cursor = conn.cursor()
            cursor.execute(f"SELECT imie , haslo FROM uzytkownicy WHERE imie ='{name}' AND haslo ='{hashed_password}'")
            result = cursor.fetchone()

            if result:
                cursor.execute(f"SELECT czy_admin FROM uzytkownicy WHERE czy_admin='1' AND imie ='{name}'")
                result2 = cursor.fetchone()
                print(result2)
                print("cos")
                if result2 == (1,):
                    page.add(ft.Text("Użytkownik jest administratorem.!"))
                    page.add(ft.Text("Zalogowano!"))
                else:
                    main_page(e)
            else:
                pass

        def page_rejestracja(e):
            page.clean()
            page.update()
            Zarejestruj = ft.Text(value="Zaloguj sie1", color="grey", text_align="CENTER", font_family='ARIAL')
            txt_Login = ft.TextField(label="Nazwa: ", text_align="left", width=300, autofocus=True)
            txt_Haslo = ft.TextField(label="Hasło: ", text_align="left", autofocus=True, password=True)
            txt_Haslo2 = ft.TextField(label="Powtórz hasło: ", text_align="left", autofocus=True, password=True)
            page.add(Zarejestruj, txt_Login, txt_Haslo, txt_Haslo2)

            def page_rejestracja1(e):
                if not txt_Login.value:
                    txt_Login.error_text = "Please enter your name"
                    page.update()
                else:
                    Login = txt_Login.value
                    page.clean()
                if not txt_Haslo.value:
                    txt_Haslo.error_text = "Please enter your password"
                    page.update()
                else:
                    Haslo = txt_Haslo.value
                    page.clean()
                if not txt_Haslo2.value:
                    txt_Haslo2.error_text = "Please enter your password again"
                    page.update()
                else:
                    Haslo2 = txt_Haslo2.value
                    page.clean()

                if Haslo == Haslo2:
                    hashed_password = hash_password(Haslo)
                    cursor = conn.cursor()
                    cursor.execute(f"INSERT INTO uzytkownicy (imie, haslo) VALUES ('{Login}', '{hashed_password}')")
                    conn.commit()
                    page.add(ft.Text("Zarejestrowano! Proszę się zalogować"))
                    page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked_login, ))


                else:
                    page.add(ft.Text("Hasła nie są takie same!"))

            page.add(ft.ElevatedButton(text="Zarejestruj się", on_click=page_rejestracja1, ))
            page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked_login, ))

        page.add(ft.ElevatedButton(text="Zaloguj się", on_click=button_clicked_login, ))
        page.add(ft.ElevatedButton(text="Zarejestruj się", on_click=page_rejestracja, ))

    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    zaloguj_page()
    test = ft.TextField()
    page.add(test)
    def main_page(e):
        page.clean()

        def route_change(route):
            page.views.clear()
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Bibiloteka"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Moje Konto", on_click=lambda _: page.go("/Konto")),
                        ft.Row(wrap=True, scroll="always", expand=True),
                    ],
                )
            )
            if page.route == "/Konto":
                
                page.views.append(
                    ft.View(
                        "/Konto",
                        [
                            ft.AppBar(title=ft.Text("Konto"), bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.ElevatedButton("Biblioteka", on_click=lambda _: page.go("/")),
                            ft.Text('Hejka'),
                        ],
                    )
                )
            page.update()

        def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)
ft.app(target=main)