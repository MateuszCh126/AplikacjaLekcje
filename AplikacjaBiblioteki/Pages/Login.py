from flet import *
import sqlite3
import flet as ft
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
bg='#cdb4db'
bg2='#ffc8dd'
bg3='#ffafcc'
bg4='#bde0fe'
bg5='#a2d2ff'

class Login1(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page=page
    
    def build(self):
        Pola_logowania = Column(

        )
        txt_Nazwa = ft.TextField()
        txt_Hasło = ft.TextField()

        
        Pola_logowania.controls.append(
            Container(
                border_radius=20,
                bgcolor=bg2,
                width=300,height=300,
                padding=15,
                    content=Column(
                        alignment=ft.alignment.center,
                        controls=[
                            TextField(txt_Nazwa,label="Nazwa: ", text_align="left", width=300, autofocus=True),
                            TextField(txt_Hasło,label="Hasło: ", text_align="left", autofocus=True, password=True,width=300),                                            
                            ElevatedButton("Zaloguj się",on_click=button_clicked_login, bgcolor=bg3,
                                color=bg5,
                                style=ft.ButtonStyle(
                                shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),},
                                side={ft.MaterialState.DEFAULT: ft.BorderSide(1, bg4),
                                ft.MaterialState.HOVERED: ft.BorderSide(2, bg4),},
                                ),
                            ), 
                            ElevatedButton("Rejestracja",on_click=lambda _: self.page.go('/Register'),
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
        def button_clicked_login(e):
                if not txt_Nazwa.value or not txt_Hasło.value:
                    txt_Nazwa.error_text = "Podaj Nazwe"
                    txt_Hasło.error_text = "Podaj Hasło"
                    
                else:
                    name = txt_Nazwa.value
                    password=txt_Hasło.value
                    
                

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
                        self.page.go('/Register')
                    elif result2==(0,):
                        self.page.go('/Register')
                else:
                    pass
        logowanie = Container(
            Column(
                    controls=[
                        Container(
                            height=400,width=500,
                            bgcolor=bg,
                            border_radius=35,
                            alignment=ft.alignment.center, 
                            content=Column(                         
                                controls=[
                                    Text('Zaloguj sie',weight=600,size=30,color=bg5,text_align="center",),
                                    Pola_logowania,
                                ],
                                alignment=ft.alignment.center
                        )
                    )
                ]
            )
        )
        
        return logowanie
    def main(page: ft.Page):
        page.title("Logowanie")
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

            
        zaloguj_page()
