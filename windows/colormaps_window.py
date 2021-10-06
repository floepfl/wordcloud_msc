import PySimpleGUI as sg
from .window import Window
from fonts_wrangling.base64_images import base64_images_dict


class ColormapsWindow(Window):

    def __init__(self, font, button_size):
        super(ColormapsWindow, self).__init__()
        self.font = font
        self.button_size = button_size


    def layout(self):
        sg.theme('DarkAmber')  # Add a little color to your windows
        # All the stuff inside your window. This is the PSG magic code compactor...
        layout = [
            [sg.Image(base64_images_dict['cyclic_and_uniform_sequential']),
             sg.Image(base64_images_dict['sequential_2']),
             sg.Image(base64_images_dict['qualitative'])],
            [sg.Image(base64_images_dict['sequential_1']),
             sg.Image(base64_images_dict['diverging']),
             sg.Image(base64_images_dict['misc']) ],
        [sg.Button('Back', key='_BUTTON_BACK_', font=self.font, size=self.button_size)]]
        self.window = sg.Window('', layout)

    def run(self):
        self.layout()
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Cancel', '_BUTTON_BACK_'):
                self.window.close()
                break
