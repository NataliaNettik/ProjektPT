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

# Funkcja zmieniająca kolor tła zaznaczonego zadania na bardzo jasnoniebieski
def w_trakcie_zadanie():
    selected_index = listbox_zadania.curselection()
    if selected_index:
        listbox_zadania.itemconfig(selected_index, {'bg': '#a6e2ff'})
        aktualizuj_pasek_postepu()

# Napis nad głównym obszarem z zadaniami
label_lista_zadan = Label(root, text='L I S T A   Z A D A Ń', font=('Helvetica', 16, 'bold'), bg='#034078', fg='white')
label_lista_zadan.pack()

# Ramka dla listy zadań
frame_zadania = Frame(root)
frame_zadania.pack(pady=10)

# Ramka przycisków
frame_przyciski = Frame(root, bg='#61a0ff')
frame_przyciski.pack(pady=10)

# Przyciski
button_dodaj = Button(
    frame_przyciski,
    text='Dodaj Zadanie',
    command=dodaj_zadanie,
    padx=10,
    pady=5,
    font=('Helvetica', 14),
    bg='#4CAF50',
    fg='black'
)
button_dodaj.pack(side=LEFT)

button_usun = Button(
    frame_przyciski,
    text='Usuń Zadanie',
    command=usun_zadanie,
    padx=10,
    pady=5,
    font=('Helvetica', 14),
    bg='#FF5733',
    fg='black'
)
button_usun.pack(side=LEFT)

button_wykonane = Button(
    frame_przyciski,
    text='Wykonane',
    command=wykonaj_zadanie,
    padx=10,
    pady=5,
    font=('Helvetica', 14),
    bg='#3498DB',
    fg='black'
)
button_wykonane.pack(side=LEFT)
