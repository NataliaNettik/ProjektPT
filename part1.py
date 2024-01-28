# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:16:46 2024

@author: natal
"""

# Funkcja usuwająca zaznaczone zadanie z listy
def usun_zadanie():
 selected_index = listbox_zadania.curselection() # Pobranie indeksu zaznaczonego zadania
 if selected_index:
 listbox_zadania.delete(selected_index) # Usunięcie zaznaczonego zadania z listy
 aktualizuj_pasek_postepu() # Aktualizacja paska postępu po usunięciu zadania