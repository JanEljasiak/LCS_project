from customtkinter import *
import Backend

set_default_color_theme("green")
root = CTk()
root.title("LCS")

CTkLabel(root, text="Ciąg 1").grid(row=0)
CTkLabel(root, text="Ciąg 2").grid(row=1)

e1 = CTkEntry(root, width=500)
e2 = CTkEntry(root, width=500)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def open_txt(e):
    text_file = filedialog.askopenfile(initialdir="C:/gui/", title='Otwórz plik tekstowy',
                                       filetypes=(("Text Files", "*.txt"), ('All files', '*.*')))
    file = open(text_file.name, "r")
    stuff = file.read()
    e.insert(END, stuff)
    text_file.close()


open_button1 = CTkButton(root, text="Otwórz plik", command=lambda: open_txt(e1))
open_button2 = CTkButton(root, text="Otwórz plik", command=lambda: open_txt(e2))
open_button1.grid(row=0, column=2)
open_button2.grid(row=1, column=2)


def click_run():
    CTkLabel(root, text=" " * 50).grid(row=3, column=1)
    try:
        CTkLabel(root, text=Backend.LCS(e1.get(), e2.get())).grid(row=3, column=1)
    except:
        CTkLabel(root, text="Nieprawidłowe dane").grid(row=3, column=1)


run_button = CTkButton(root, text='Znajdź najdłuższy wspólny podciąg', command=click_run).grid(row=2, column=1)

root.mainloop()
