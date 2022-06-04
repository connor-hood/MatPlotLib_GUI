import PySimpleGUI as sg
import matplotlib.pyplot as plt


def draw_line():
    plt.title("Test with MatPlotLib in PySimpleGui")
    plt.text(0, 0.6, "Line Graph Version")
    plt.plot([0.1, 0.2, 0.5, 0.7])
    plt.show(block=False)

layout = [[sg.Button('Plot'), sg.Cancel(), sg.Button('Popup')]]

window = sg.Window('Have some Matplotlib....', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Plot':
        draw_line()
    elif event == 'Popup':
        sg.popup('Yes, your application is still running')
window.close()
