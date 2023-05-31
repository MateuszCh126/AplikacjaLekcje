from flet import *
import sqlite3
import flet as ft
import hashlib

# lączenie z baza danych

bg='#cdb4db'
bg2='#ffc8dd'
bg3='#ffafcc'
bg4='#bde0fe'
bg5='#a2d2ff'

class Login1(UserControl):
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
            czy_admin BOOLEAN NOT NULL DEFAULT 0
        );
            """)

    # zapisanie zmian w bazie danych
    conn.commit()
    
    def build(self):
        self.page.window_full_screen=True
        Pola_logowania = Column(

        )
        txt_Nazwa = ft.Ref[ft.TextField]()
        txt_Hasło = ft.Ref[ft.TextField]()
        
        def button_clicked_login(e):
            if not txt_Nazwa.current.value:
                txt_Nazwa.current.error_text = "Podaj nazwe użytkownika"
                self.page.update()
            else:
                name = txt_Nazwa.current.value
                self.page.clean()
            if not txt_Hasło.current.value:
                txt_Hasło.current.error_text = "Podaj Hasło"
                self.page.update()
            else:
                password = txt_Hasło.current.value
                self.page.clean()
                hashed_password = hash_password(password)
                cursor = conn.cursor()
                cursor.execute(f"SELECT imie , haslo FROM uzytkownicy WHERE imie ='{name}' AND haslo ='{hashed_password}'")
                result = cursor.fetchone()
                if result:
                    cursor.execute(f"SELECT czy_admin FROM uzytkownicy WHERE imie ='{name}'")
                    result2 = str(cursor.fetchone())
                    print(result2)
                    if result2=='(1,)':
                        self.page.go('/Main')
                        print('poszlo dla admina')
                    elif result2=='(0,)':
                        self.page.go('/Main')
                        print("poszlo bez admian")
                else:
                    txt_Nazwa.current.error_text = "Złe dane"
                    pass
                self.page.update()
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
                            ElevatedButton("Zaloguj się",on_click=lambda e: button_clicked_login(e), bgcolor=bg3,
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

               
        logowanie = Container(
            Column(
                alignment=ft.alignment.center,
                    controls=[
                        Container(
                            height=self.page.height,width=self.page.width,
                            bgcolor=bg,
                            border_radius=35,
                            alignment=ft.alignment.center, 
                            content=Column(                         
                                controls=[
                                    Text('Zaloguj sie',weight=600,size=60,color=bg5,text_align="right",),
                                    Pola_logowania,
                                ],
                                alignment=ft.alignment.center
                        )
                    )
                ]
            )
        )
        self.page.vertical_alignment.CENTER
        return logowanie
    
