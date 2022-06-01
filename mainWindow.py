import PySimpleGUI as sg
import Dijkstra as dk

sg.theme("Dark Amber")
user_input_column = [
    [sg.FileBrowse(button_text="Wybierz plik z grafem", size=(35, None),
                   file_types=(("Text files", "*.txt"),), k="graphBrowser", enable_events=True)],
    [sg.Button(button_text="Wylicz najkrótszą ścieżkę",
               size=(35, None), k="findSortestPath")],
    [sg.HorizontalSeparator(pad=(None, (10, 7)))],
    [sg.Text("Informacje o pliku:", size=(35, None), justification="center")],
    [sg.Multiline(size=(38, 3), auto_refresh=True,
                  tooltip="ścieżka do pliku", k="path")],
    [sg.Multiline(size=(38, 7), horizontal_scroll=True,
                  tooltip="zawartość pliku", k="content")],
]

user_output_column = [
    [sg.Multiline(size=(38, 3), auto_refresh=True,
                  tooltip="wynik obliczeń", k="outputContent")],
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
        filePath = values["graphBrowser"]
        file = open(filePath, "r")
        fileContent = file.read()
        file.close
        window["content"].update(fileContent)
        window["path"].update(filePath)
    if event == "findSortestPath":
        try:
            graph = dk.convertToNumpyArray(values["content"])
            content = str(dk.Dijkstra(5, 2, graph))
            window["outputContent"].update(content)
        except:
            window["outputContent"].update("")
window.close()
