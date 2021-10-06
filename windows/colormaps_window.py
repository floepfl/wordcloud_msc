import PySimpleGUI as sg
from .window import Window


class ColormapsWindow(Window):

    def __init__(self, font, button_size):
        super(ColormapsWindow, self).__init__()
        self.font = font
        self.button_size = button_size


    def layout(self):
        sg.theme('DarkAmber')  # Add a little color to your windows
        # All the stuff inside your window. This is the PSG magic code compactor...
        layout = [
            [sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/cyclic_and_uniform_sequential.png'),
             sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/sequential_2.png'),
             sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/qualitative.png')],
            [sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/sequential_1.png'),
             sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/diverging.png'),
             sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/misc.png') ],
        [sg.Button('Back', key='_BUTTON_BACK_', font=self.font, size=self.button_size)]]
        self.window = sg.Window('', layout)

    def run(self):
        self.layout()
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Cancel', '_BUTTON_BACK_'):
                self.window.close()
                break
