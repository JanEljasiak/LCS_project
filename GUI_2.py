from tkinter import *
import Backend

root = Tk()

Label(root, text="Input 1").grid(row=0)
Label(root, text="Input 2").grid(row=1)

e1 = Entry(root, width=100)
e2 = Entry(root, width=100)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def click_run():
    Label(root, text=Backend.LCS(e1.get(), e2.get())).grid(row=3, column=1)


run_button = Button(root, text='RUN', command=click_run).grid(row=2, column=0)

Label(root, text="OUTPUT").grid(row=3, column=0)

root.mainloop()
