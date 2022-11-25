import PySimpleGUI as sg  # pip install pysimplegui


layout = [
    [sg.Text("Input data: "), sg.Input(key="-IN-"), sg.FileBrowse()],
    [sg.Text("Output data: "), sg.Input(key="-OUT-"), sg.FileBrowse()],
    [sg.Exit(), sg.Button("Do sth")],
]

window = sg.Window("123", layout)

