import flet as ft
from flet import *
import sqlite3
import hashlib
from Rejestracja import Logowanie
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
class Zobaczymy(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    #strona wyswietlana 
    def main(self,page: Page):
        page.title = "logowanie234"
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.add(ft.ElevatedButton(text="Zaloguj się", on_click= lambda : self.page.go('/login'),))
        #logowanie tego typu
        Zaloguj = ft.Text(value="Zaloguj sie43", color="grey", text_align="CENTER", font_family='ARIAL')
        txt_Nazwa = ft.TextField(label="Nazwa: ", text_align="left", width=300, autofocus=True)
        txt_Hasło = ft.TextField(label="Hasło: ", text_align="left", autofocus=True, password=True)
        
        
        # zabezpieczenie hasla bo to wiesz pro ludzie robia TO DO REJESTRACJI BTW
        def hash_password(password): 
            return hashlib.sha256(password.encode('utf-8')).hexdigest()

        def button_clicked(e):
            conn= sqlite3.connect('Uzytkownicy.db',check_same_thread=False)
            cursor = conn.cursor()
            hashed_password = hash_password(Hasło)
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

    ft.app(target=main)    



    
 