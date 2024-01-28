# Importowanie modułów z modułu tkinter, potrzebnych do budowy interfejsu użytkownika
from tkinter import *
from tkinter import messagebox

# Funkcja dodająca nowe zadanie do listy
def dodaj_zadanie():
    zadanie = entry_zadanie.get()  # Pobranie tekstu wprowadzonego w polu do wprowadzania zadań
    if zadanie.strip() != "":  # Sprawdzenie, czy wprowadzony tekst nie jest pusty po usunięciu białych znaków
        listbox_zadania.insert(END, zadanie)  # Wstawienie nowego zadania na koniec listy
        entry_zadanie.delete(0, "end")  # Wyczyszczenie pola do wprowadzania zadań
        aktualizuj_pasek_postepu()  # Aktualizacja paska postępu po dodaniu zadania
    else:
        messagebox.showwarning("Ostrzeżenie", "Proszę wprowadzić jakieś zadanie.")  # Wyświetlenie ostrzeżenia, gdy wprowadzony tekst jest pusty
