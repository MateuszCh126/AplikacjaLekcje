from flet import *
import sqlite3
import flet as ft
import hashlib
bg='#cdb4db'
bg2='#ffc8dd'
bg3='#ffafcc'
bg4='#bde0fe'
bg5='#a2d2ff'
class Main(UserControl):
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
        glowna=Container(
            width=1080,
            height=1080,
            bgcolor=bg,
        )
        return glowna