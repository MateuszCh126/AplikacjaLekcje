from flet import *
import sqlite3
import flet as ft
import hashlib

bg='#cdb4db'
bg2='#ffc8dd'
bg3='#ffafcc'
bg4='#bde0fe'
bg5='#a2d2ff'
class Register1(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page=page
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
    def build(self):
        Pola_logowania = Column(

            )
        txt_Nazwa = ft.Ref[ft.TextField]()
        txt_Hasło = ft.Ref[ft.TextField]()
        txt_Hasło2 = ft.Ref[ft.TextField]()
        def page_rejestracja1(e):

            if not txt_Nazwa.current.value:
                    txt_Nazwa.current.error_text = "Wpisz Imie"
                    self.page.update()
            else:
                    Login = txt_Nazwa.current.value
                    self.page.clean()
            if not txt_Hasło.current.value:
                    txt_Hasło.current.error_text = "Podaj Hasło"
                    self.page.update()
            else:
                    Haslo = txt_Hasło.current.value
                    self.page.clean()
            if not txt_Hasło2.current.value:
                    txt_Hasło2.current.error_text = "Powtórz Hasło"
                    self.page.update()
            else:
                    Haslo2 = txt_Hasło2.current.value
                    self.page.clean()

            if Haslo == Haslo2:
                    hashed_password = hash_password(Haslo)
                    cursor = conn.cursor()
                    cursor.execute(f"INSERT INTO uzytkownicy (imie, haslo) VALUES ('{Login}', '{hashed_password}')")
                    conn.commit()
                    self.page.go('/')

            else:
                txt_Hasło2.current.error_text = "Please enter your password again"
        def hash_password(password):
            return hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        Pola_logowania.controls.append(
            Container(
                border_radius=20,
                bgcolor=bg2,
                width='50vw',height='50vw',
                padding=55,
                    content=Column(
                        alignment=ft.alignment.center,
                        controls=[
                            TextField(ref=txt_Nazwa,label="Nazwa: ", text_align="left", width=300, autofocus=True),
                            TextField(ref=txt_Hasło,label="Hasło: ", text_align="left", autofocus=True, password=True,width=300),
                            TextField(ref=txt_Hasło2,label="Hasło: ", text_align="left", autofocus=True, password=True,width=300),                                            
                            ElevatedButton("Zarejestruj się",on_click=lambda e: page_rejestracja1(e), bgcolor=bg3,
                                color=bg5,
                                style=ft.ButtonStyle(
                                shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),},
                                side={ft.MaterialState.DEFAULT: ft.BorderSide(1, bg4),
                                ft.MaterialState.HOVERED: ft.BorderSide(2, bg4),},
                                ),
                            ), 
                            ElevatedButton("Logowanie",on_click=lambda _: self.page.go('/'),
                                bgcolor=bg3,
                                color=bg5,
                                style=ft.ButtonStyle(
                                shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),},
                                side={ft.MaterialState.DEFAULT: ft.BorderSide(1, bg4),
                                ft.MaterialState.HOVERED: ft.BorderSide(2, bg4),},
                                ),
                            ),
                            
                        ]
                    )
            )
        )
        rejestracja = Container(
            Column(
                    controls=[
                        Container(
                            height=self.page.height,width=self.page.width,
                            bgcolor=bg,
                            border_radius=35,
                            alignment=ft.alignment.center, 
                            content=Column(                         
                                controls=[
                                    Text('Zarejestruj sie',weight=600,size=60,color=bg5,text_align="right",),
                                    Pola_logowania,
                                ],
                                alignment=ft.alignment.center
                        )
                    )
                ]
            )
        )
        
        return rejestracja