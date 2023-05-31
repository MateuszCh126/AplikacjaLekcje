from flet import *
import sqlite3
import flet as ft
from io import BytesIO
from PIL import Image


bg='#cdb4db'
bg2='#ffc8dd'
bg3='#ffafcc'
bg4='#bde0fe'
bg5='#a2d2ff'
class Index1(UserControl):
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
        ksiazki = ft.GridView(
        height=400,
        width=400,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
         )
        cursor = conn.execute("SELECT id_ksiazki, tytul, autor, zdjecie FROM ksiazki")
        books = cursor.fetchall()

        for book in books:
            book_id, title, author, image_data = book
            image = Image.open(BytesIO(image_data))
            print(image_data)
            image = Image.open(BytesIO(image_data))
            image.save('test_image.png')
            book_panel = Container(
                content=Column(
                    [
                        ft.Image(image,fit=ft.ImageFit.CONTAIN,),
                        Text(title),
                        Text(author),
                        Row(
                            [
                                ElevatedButton("Kup", on_click=lambda: self.buy_book(book_id),
                                bgcolor=bg3,
                                color=bg5,
                                style=ft.ButtonStyle(
                                shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),},
                                side={ft.MaterialState.DEFAULT: ft.BorderSide(1, bg4),
                                ft.MaterialState.HOVERED: ft.BorderSide(2, bg4),},
                                ),
                            ),
                             ElevatedButton("Wypożycz", on_click=lambda: self.rent_book(book_id),
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
                        ),
                    ]
                )
            )
            ksiazki.controls.append(book_panel)



        glowna=Container(
            height=self.page.height,width=self.page.width,
            bgcolor=bg,
            content=Container(
                ksiazki,

            )
        )
        return glowna
    def buy_book(self, book_id):
    # Kod do obsługi zakupu książki
        pass

    def rent_book(self, book_id):
    # Kod do obsługi wypożyczenia książki
        pass