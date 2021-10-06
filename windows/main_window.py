import PySimpleGUI as sg
from PySimpleGUI import BUTTON_TYPE_SAVEAS_FILE, ThisRow
from .window import Window
from .settings_window import SettingsWindow
from wordcloud_transform import *
from fonts_wrangling.base64_images import base64_images_dict


class MainWindow(Window):

    def __init__(self, font, font_names_for_preview, base64_font_dict, default_font):
        super(MainWindow, self).__init__()
        self.subwindows['settings'] = SettingsWindow(font, font_names_for_preview, base64_font_dict, default_font)
        self.font = font
        self.default_image_preview = sg.Image(base64_images_dict['image_placeholder'], key='_IMAGE_PREVIEW_')

    def layout(self):
        sg.theme('DarkAmber')  # Add a little color to your windows
        text_size = (20, 1)
        button_size = (12, 2)
        layout = [[sg.Column([[sg.Text('Input image: ', font=self.font, size=text_size),
                               sg.Input(key='_INPUT_IMAGE_', default_text='Choose .png file', font=self.font),
                               sg.FilesBrowse(font=self.font, size=(10, 1))],
                              [sg.Text('Words:', font=self.font, size=text_size),
                               sg.Input(key='_INPUT_WORDS_',enable_events=True, default_text='Choose .csv file', font=self.font),
                               sg.FilesBrowse(font=self.font,enable_events=True, size=(10, 1))],
                              [sg.Text('', font=self.font,
                                       key='_OUTPUT_IMAGE_SIZE', visible=False)],
                              [sg.Button('Settings', key='_BUTTON_SETTINGS_', size=button_size, font=self.font),
                               sg.Button('Exit', key='_BUTTON_EXIT_', size=button_size, font=self.font),
                               sg.Button('Transform', key='_BUTTON_TRANSFORM_', size=button_size, font=self.font),
                               sg.Input(key='_TEXT_SAVE_IMAGE_', enable_events=True, default_text='.csv',
                                        font=self.font, visible=False),
                               sg.Button('Save image', enable_events=True, target=(ThisRow, -1), key='_BUTTON_SAVE_IMAGE_', size=button_size, font=self.font,
                                             button_type=BUTTON_TYPE_SAVEAS_FILE, visible=False, file_types=('.png'),
                                         default_extension='.png')]]),
                   self.default_image_preview]]

        # TODO scale, preview size, transparent_background, repeat
        # layout = [[sg.Column([[sg.Text('Input image: ', font=font)], [sg.Text('Horizontal/Vertical ratio', font=font)]]),
        #                        sg.Column([[sg.Text('Horizontal/Vertical ratio', font=font)], [sg.Slider(range=(0,100))]])]]
        self.window = sg.Window('', layout)

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
                self.wordcloud_image, preview_wordcloud_image_str, output_image_size =\
                    transform(**all_transform_kwargs)
                self.window['_IMAGE_PREVIEW_'].update(source=preview_wordcloud_image_str)
                self.window['_BUTTON_SAVE_IMAGE_'].update(visible=True)
                self.window['_OUTPUT_IMAGE_SIZE'].update(value=f'Transformed image size: {output_image_size[0]}x{output_image_size[1]} '
                                                               f'(width x height in pixels)', visible=True)
            elif event == '_TEXT_SAVE_IMAGE_':
                self.wordcloud_image.save(values['_TEXT_SAVE_IMAGE_'], 'PNG')
            elif event in (sg.WIN_CLOSED, 'Cancel', '_BUTTON_EXIT_'):
                self.window.close()
                break




