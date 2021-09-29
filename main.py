import PySimpleGUI as sg
from gui import *
from wordcloud import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Event Loop to process "events"
    font = ('Helvetica', 16)
    last_window = None
    image_preview = sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/image_placeholder.png')
    curr_window = main_window(font=font, image=image_preview)
    while True:
        event, values = curr_window.read()
        print(event, values)
        if event == 'go_to_colormaps':
            last_window = curr_window
            curr_window = colormap_window()
        elif event == 'transform':
            wc = transform()
        elif event in (sg.WIN_CLOSED, 'Cancel') and last_window is not None:
            curr_window = last_window
            last_window = None
        elif event in (sg.WIN_CLOSED, 'Cancel'):
            break

    curr_window.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
