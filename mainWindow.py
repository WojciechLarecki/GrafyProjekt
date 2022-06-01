import PySimpleGUI as sg

sg.theme("Dark Amber")
user_input_column = [
    [sg.FileBrowse(button_text="Wybierz plik z grafem", size=(35, None),
                   file_types=("Text files", "*.txt"), k="graphBrowser", enable_events=True)],
    [sg.Button(button_text="Wylicz najkrótszą ścieżkę", size=(35, None))],
    [sg.HorizontalSeparator(pad=(None, (10, 7)))],
    [sg.Text("Informacje o pliku:", size=(35, None), justification="center")],
    [sg.Multiline(size=(38, 3), auto_refresh=True,
                  tooltip="ścieżka do pliku", k="path")],
    [sg.Multiline(size=(38, 7), horizontal_scroll=True,
                  tooltip="ścieżka do pliku", k="content")],
]

user_output_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

layout = [
    [
        sg.Column(user_input_column),
        sg.VSeperator(),
        sg.Column(user_output_column),
    ]
]

window = sg.Window("PathFinder", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "graphBrowser":
        # folder = values["-FOLDER-"]
        # try:
        #     file_list = os.listdir(folder)
        # except:
        #     file_list = []
        filePath = values["graphBrowser"]
        file = open(filePath, "r")
        fileContent = file.read()
        file.close
        window["content"].update(fileContent)
        window["path"].update(filePath)
window.close()
