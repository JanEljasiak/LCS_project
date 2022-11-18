import PySimpleGUI as sg  # pip install pysimplegui


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
        sg.popup_error("Not yet implemented")
window.close()
"""



"""