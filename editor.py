'''
    ----- Env -----
    conda create -n PhEditor -c conda-forge -c simpleitk -c bioconda graphicsmagick opencv numpy matplotlib scikit-image scipy pillow mahotas simpleitk pysimplegui
'''

import PySimpleGUI as sg

x = []


sg.theme('DarkTeal11') #colour

# Inside the window

layout = [  [sg.Text('Have fun!')],
            [ sg.Text('Enter anything you want'), sg.InputText() ],
            [ sg.Button('Add'), sg.Button('Leave') ]   ]

# Create the Window
window = sg.Window("Cookie's fun window", layout, size=(500, 250))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Leave': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

    x.append(values[0])


window.close()


print('======================')
print(x)