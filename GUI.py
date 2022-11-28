import PySimpleGUI as sg  # pip install pysimplegui
from pathlib import Path

def is_valid_path(filepath):
    if filepath and Path(filepath).exists():
        return True
    sg.popup_error("Filepath is not correct")
    return False






layout = [
    [sg.Text("Input data: "), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("TextFiles", "*.txt"),("Fasta files","*.fasta")))],
    [sg.Text("Output folder: "), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Check degree of kinship")],
]

window = sg.Window("Kinshaap", layout)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Check degree of kinship":
        if is_valid_path(values["-IN-"]) and is_valid_path(values["-OUT-"]):
            sg.popup_error("Not yet implemented")
window.close()
"""



"""