import PySimpleGUI as sg

layout = [[sg.Text('A toggle button example')],
          [sg.Button('On', size=(3,1), button_color=('white', 'green'), key='_B_'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

down = True

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == '_B_':
        down = not down
        window.Element('_B_').Update(('Off','On')[down], button_color=(('white', ('red', 'green')[down])))

window.Close()