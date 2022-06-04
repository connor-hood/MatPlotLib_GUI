import PySimpleGUI as sg
import matplotlib.pyplot as plt


line_data = [0.1, 0.2, 0.5, 0.7]
pie_data = [.37, .31, .18, .11]


def draw_line():
    plt.title("Test with MatPlotLib in PySimpleGui")
    plt.text(0.535, 0.703, "Line Graph Version")
    plt.plot(line_data)
    plt.show(block=False)

def draw_pie():
    plt.title("Test with MatPlotLib in PySimpleGui")
    plt.text(-0.781, 1.077, "Pie Graph")
    plt.pie(pie_data, autopct='%d%%')
    plt.axis('equal')
    plt.show()

layout = [[sg.Button('Plot'), sg.Button('Pie'), sg.Cancel(), sg.Button('Popup')]]

window = sg.Window('Have some Matplotlib...', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Plot':
        draw_line()
    elif event == 'Pie':
        draw_pie()
    elif event == 'Popup':
        sg.popup('Yes, your application is still running')
window.close()
