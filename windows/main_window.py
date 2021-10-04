import PySimpleGUI as sg
from .window import Window
from .settings_window import SettingsWindow
from wordcloud_transform import *


class MainWindow(Window):

    def __init__(self, font, font_names_for_preview, base64_font_dict, default_font):
        super(MainWindow, self).__init__()
        self.subwindows['settings'] = SettingsWindow(font, font_names_for_preview, base64_font_dict, default_font)
        self.font = font
        self.default_image_preview = sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/image_placeholder.png', key='_IMAGE_PREVIEW_')

    def layout(self):
        sg.theme('DarkAmber')  # Add a little color to your windows
        text_size = (20, 1)
        button_size = (15, 1)
        layout = [[sg.Column([[sg.Text('Input image: ', font=self.font, size=text_size),
                               sg.Input(key='_INPUT_IMAGE_', default_text='.png or .jpg/jpeg', font=self.font),
                               sg.FilesBrowse(font=self.font, size=(10, 1))],
                              [sg.Text('Words:', font=self.font, size=text_size),
                               sg.Input(key='_INPUT_WORDS_', default_text='.numbers, .xlsx or .csv', font=self.font),
                               sg.FilesBrowse(font=self.font, size=(10, 1))],
                              [sg.Button('Settings', key='_BUTTON_SETTINGS_', size=(15, 2), font=self.font),
                               sg.Button('Transform', key='_BUTTON_TRANSFORM_', size=(15, 2), font=self.font)]]),
                   self.default_image_preview]]

        # TODO scale, preview size, transparent_background, repeat
        # layout = [[sg.Column([[sg.Text('Input image: ', font=font)], [sg.Text('Horizontal/Vertical ratio', font=font)]]),
        #                        sg.Column([[sg.Text('Horizontal/Vertical ratio', font=font)], [sg.Slider(range=(0,100))]])]]
        self.window = sg.Window('Window Title', layout)

    def run(self):
        self.layout()
        while True:
            event, values = self.window.read()
            print(event, values)
            if event == '_BUTTON_SETTINGS_':
                self.window.hide()
                self.subwindows['settings'].run()
                self.window.un_hide()
            elif event == '_BUTTON_TRANSFORM_':
                # loading_window = fixed_loading(loading_image)
                # curr_window.close()
                # _ = loading_window.read()
                transform_kwargs = {'image_path': values['_INPUT_IMAGE_'],
                                    'words_path': values['_INPUT_WORDS_']}

                all_transform_kwargs = {**transform_kwargs, **self.subwindows['settings'].transform_kwargs} #TODO add proper recursive strategy
                wordcloud_image_str, preview_wordcloud_image_str = transform(**all_transform_kwargs)
                self.window['_IMAGE_PREVIEW_'].update(source=preview_wordcloud_image_str)
            elif event in (sg.WIN_CLOSED, 'Cancel'):
                self.window.close()
                break




