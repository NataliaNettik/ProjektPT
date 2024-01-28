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
 # Funkcja usuwająca zaznaczone zadanie z listy
def usun_zadanie():
    selected_index = listbox_zadania.curselection()  # Pobranie indeksu zaznaczonego zadania
    if selected_index:
        listbox_zadania.delete(selected_index)  # Usunięcie zaznaczonego zadania z listy
        aktualizuj_pasek_postepu()  # Aktualizacja paska postępu po usunięciu zadania
        
# Funkcja zmieniająca kolor tła zaznaczonego zadania na bardzo jasnoniebieski
def w_trakcie_zadanie():
    selected_index = listbox_zadania.curselection()
    if selected_index:
        listbox_zadania.itemconfig(selected_index, {'bg': '#a6e2ff'})
        aktualizuj_pasek_postepu()
        
# Funkcja zmieniająca kolor tła zaznaczonego zadania
def wykonaj_zadanie():
    selected_index = listbox_zadania.curselection()  # Pobranie indeksu zaznaczonego zadania
    if selected_index:
        current_bg = listbox_zadania.itemcget(selected_index, "bg")  # Pobranie aktualnego koloru tła zadania
        new_bg = '#61a0ff' if current_bg != '#61a0ff' else ''  # Zmiana koloru tła na niebieski, jeśli niebieski nie był wcześniej ustawiony, w przeciwnym razie usunięcie koloru
        listbox_zadania.itemconfig(selected_index, {'bg': new_bg})  # Ustawienie nowego koloru tła zadania
        aktualizuj_pasek_postepu()  # Aktualizacja paska postępu po zmianie koloru zadania

# Funkcja aktualizująca pasek postępu w zależności od liczby zadań
def aktualizuj_pasek_postepu():
    all_tasks = listbox_zadania.size()  # Pobranie liczby wszystkich zadań
    blue_tasks = len([i for i in range(all_tasks) if listbox_zadania.itemcget(i, "bg") == '#61a0ff'])  # Pobranie liczby zadań z niebieskim tłem
    total_width = pasek_postepu.winfo_width()  # Pobranie szerokości paska postępu

    if all_tasks > 0:
        blue_width = int((blue_tasks / all_tasks) * total_width)  # Obliczenie szerokości niebieskiego obszaru paska postępu
        white_width = total_width - blue_width  # Obliczenie szerokości białego obszaru paska postępu
    else:
        blue_width = 0
        white_width = total_width

    pasek_postepu.coords(pasek_niebieski, 0, 0, blue_width, 20)  # Ustawienie współrzędnych niebieskiego obszaru paska postępu
    pasek_postepu.coords(pasek_bialy, blue_width, 0, total_width, 20)  # Ustawienie współrzędnych białego obszaru paska postępu

# Pokazuj gwiazdkę gdy pasek jest całkowicie niebieski, ukryj w przeciwnym razie
if blue_width == total_width:
    canvas_gwiazdka.place(relx=0.87, rely=0.878, anchor='se')
else:
    canvas_gwiazdka.place_forget()

# Utworzenie głównego okna
root = Tk()
root.geometry('650x500+500+200')  # Ustawienie rozmiaru i położenia głównego okna
root.title('Lista Zadań')  # Ustawienie tytułu głównego okna
root.config(bg='#034078')  # Ustawienie koloru tła głównego okna
root.resizable(width=False, height=False)  # Zablokowanie możliwości zmiany rozmiaru głównego okna

# Napis nad głównym obszarem z zadaniami
label_lista_zadan = Label(root, text='L I S T A   Z A D A Ń', font=('Helvetica', 16, 'bold'), bg='#034078', fg='white')
label_lista_zadan.pack()

# Ramka dla listy zadań
frame_zadania = Frame(root)
frame_zadania.pack(pady=10)

# Listbox z zadaniami
listbox_zadania = Listbox(
    frame_zadania,
    width=25,
    height=8,
    font=('Helvetica', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
listbox_zadania.pack(side=LEFT, fill=BOTH)

# Pasek przewijania dla listy zadań
scrollbar_zadania = Scrollbar(frame_zadania)
scrollbar_zadania.pack(side=RIGHT, fill=Y)

listbox_zadania.config(yscrollcommand=scrollbar_zadania.set)
scrollbar_zadania.config(command=listbox_zadania.yview)

# Pole do wprowadzania nowych zadań
entry_zadanie = Entry(
    root,
    font=('Helvetica', 20)
)
entry_zadanie.pack(pady=20)

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

button_w_trakcie = Button(
    frame_przyciski,
    text='W trakcie',
    command=w_trakcie_zadanie,
    padx=10,
    pady=5,
    font=('Helvetica', 14),
    bg='#a6e2ff', 
    fg='black'
)
button_w_trakcie.pack(side=LEFT)

# Utwórz Canvas dla gwiazdki
canvas_gwiazdka = Canvas(root, width=20, height=20, bg='#034078', highlightthickness=0)
canvas_gwiazdka.create_text(10, 10, text='★', font=('Helvetica', 12, 'bold'), fill='#FFD700')

# Pasek postępu
pasek_postepu = Canvas(root, width=435 - 10, height=20, bg='#ffffff', highlightthickness=1, highlightbackground='black')
pasek_postepu.pack(pady=(0, 10))

# Paski kolorów
pasek_bialy = pasek_postepu.create_rectangle(0, 0, 0, 20, fill='#ffffff', width=0)
pasek_niebieski = pasek_postepu.create_rectangle(0, 0, 0, 20, fill='#61a0ff', width=0)
