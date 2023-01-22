from customtkinter import *
import Backend

set_default_color_theme("green")
root = CTk()
root.title("LCS")

CTkLabel(root, text="Ciąg 1").grid(row=0)
CTkLabel(root, text="Ciąg 2").grid(row=1)

e1 = CTkEntry(root, width=1000)
e2 = CTkEntry(root, width=1000)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


def open_txt(e):
    text_file = filedialog.askopenfile(initialdir="C:/gui/", title='Otwórz plik tekstowy',
                                       filetypes=(("Text Files", "*.txt"), ('All files', '*.*'), ('All files', '*.fasta')))
    file = open(text_file.name, "r")
    stuff = file.read()
    e.insert(END, stuff)
    text_file.close()


open_button1 = CTkButton(root, text="Otwórz plik", command=lambda: open_txt(e1))
open_button2 = CTkButton(root, text="Otwórz plik", command=lambda: open_txt(e2))
open_button1.grid(row=0, column=2)
open_button2.grid(row=1, column=2)


def click_run():
    try:
        LCS = Backend.LCS(e1.get(), e2.get())
        for seq in range(len(LCS)):
            output = CTkTextbox(root)
            output.insert(INSERT, f"Najdluższy wspólny podciąg:\n {LCS[seq]}\n")
            output.tag_add("start", "2.1", f"2.{len(LCS[seq])+1}")
            for i in range(2):
                if i == 0:
                    output.insert(END, f"Ciąg 1:\n {e1.get()}\n")
                else:
                    output.insert(END, f"Ciąg 2:\n {e2.get()}\n")
                output.grid(row=3+seq,column=1)

                coordinates = Backend.find_coordinates(e1.get(), e2.get())
                for cord in coordinates[seq][i]:
                    output.tag_add("start", f"{2*i+4}.{cord+1}")
                output.tag_config("start", foreground="red")
    except:
        CTkLabel(root, text="Nieprawidłowe dane").grid(row=3, column=1)


# --------------------------------------
run_button = CTkButton(root, text='Znajdź najdłuższy wspólny podciąg', command=click_run).grid(row=2, column=1)

root.mainloop()
