from sre_parse import State
import PySimpleGUI as sg
import Dijkstra as dk
from graphDraw import delete_figure_agg, draw_figure, drawGraph

sg.theme("Dark Amber")
user_input_column = [
    [sg.FileBrowse(button_text="Wybierz plik z grafem", size=(35, None),
                   file_types=(("Text files", "*.txt"),), k="graphBrowser", enable_events=True)],
    [sg.Button(button_text="Wylicz najkrótszą ścieżkę", disabled=True,
               size=(35, None), k="findSortestPath")],
    [sg.Column([
        [
            sg.Text("Start:"),
            sg.Spin([], tooltip="wierczołek początkowy", key="start"),
            sg.Text("Koniec:"),
            sg.Spin([], tooltip="wierzchołek końcowy", key="end")]], justification="center")],
    [sg.HorizontalSeparator(pad=(None, (10, 7)))],
    [sg.Text("Informacje o pliku:", size=(35, None))],
    [sg.Multiline(size=(38, 3), auto_refresh=True,
                  tooltip="ścieżka do pliku",disabled=True, k="path")],
    [sg.Multiline(size=(38, 7), horizontal_scroll=True,
                  tooltip="zawartość pliku",disabled=True, k="content")],
]

user_output_column = [
    [sg.Text("Wynik obliczeń:", size=(35, None), justification="center")],
    [sg.Multiline(size=(100, 3), auto_refresh=True,
                  tooltip="wynik obliczeń",disabled=True, k="outputContent")],
    [sg.Canvas(size=(38, 15), key="-CANVAS-")]
]

layout = [
    [
        sg.Column(user_input_column,vertical_alignment='t'),
        sg.VSeperator(),
        sg.Column(user_output_column,element_justification='center'),
    ]
]

window = sg.Window("PathFinder", layout,element_justification='top', size=(1000,600))
graph = []


def get_file_content(filePath):
    file = open(filePath, "r")
    fileContent = file.read()
    file.close
    if (fileContent == None or fileContent == 0):
        raise Exception(
            "Plik tekstowy jest pusty lub niemożliwy do odczytania.")

    return fileContent


def set_spins(window, max):
    val = [i for i in range(1, max + 1)]
    window["start"].update(val[0], values=val)
    window["end"].update(val[0], values=val)


def reset_window(window):
    window["content"].update("")
    window["path"].update("")
    window["findSortestPath"].update(disabled=True)
    window["start"].update("", values=[])
    window["end"].update("", values=[])


def set_up_text(content):
    text = "Najkrótsza ścieżka:\n"
    text += "- przechodzi przez wierzchołki: " + \
            str(content[0]) + "\n"
    text += "- koszt: " + str(content[1])
    return text

figure_agg = None
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "graphBrowser":
        try:
            filePath = values["graphBrowser"]
            fileContent = get_file_content(filePath)
            graph = dk.convertToNumpyArray(fileContent)
            
            window["content"].update(fileContent)
            window["path"].update(filePath)
            set_spins(window, len(graph))
            window["findSortestPath"].update(disabled=False)
        except Exception as e:
            sg.popup(e)
            graph = []
            reset_window(window)
    if event == "findSortestPath":
        start = values["start"]
        end = values["end"]
        if start == end:
            sg.popup("Krawędzie początkowa i końcowa nie mogą być takie same.")
            continue
        if figure_agg:
            delete_figure_agg(figure_agg)
        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, drawGraph(graph))
        content = dk.Dijkstra(start, end, graph)
        text = set_up_text(content)
        window["outputContent"].update(text)
window.close()
