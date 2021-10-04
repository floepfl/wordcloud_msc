import PySimpleGUI as sg
from .window import Window
from .colormaps_window import ColormapsWindow


class SettingsWindow(Window):
    def __init__(self, font, font_names_for_preview, base64_font_dict, default_font):
        super(SettingsWindow, self).__init__()
        self.subwindows['colormaps'] = ColormapsWindow()
        self.font = font
        self.font_names_for_preview = font_names_for_preview
        self.base64_font_dict = base64_font_dict
        self.default_font = default_font
        self.values_before_hidden = None
        self.transform_kwargs = {'font_path': [self.default_font],
                'max_words': 2000,
                'hv_ratio': 90,
                'relative_scaling': 50,
                'scale': 1,
                'canvas_width': '400',
                'canvas_height': '200',
                'contour_width': 0,
                'min_font_size': 4,
                'max_font_size': 160,
                'colormap': 'None'}

        self.translation = {'font_path': '_FONT_LIST_',
                            'max_words': '_SLIDER_MAX_WORDS_',
                            'hv_ratio': '_SLIDER_H/V_RATIO_',
                            'relative_scaling': '_SLIDER_RELATIVE_SCALING_',
                            'scale': '_SLIDER_SCALE_',
                            'canvas_width': '_INPUT_CANVAS_WIDTH_',
                            'canvas_height': '_INPUT_CANVAS_HEIGHT_',
                            'contour_width': '_SLIDER_CONTOUR_WIDTH_',
                            'min_font_size': '_SLIDER_MIN_FONT_',
                            'max_font_size': '_SLIDER_MAX_FONT_',
                            'colormap': '_INPUT_COLORMAP_'}

    def layout(self):
        sg.theme('DarkAmber')  # Add a little color to your windows
        # All the stuff inside your window. This is the PSG magic code compactor...
        text_size = (20, 1)
        button_size = (15, 1)
        layout = [[sg.Column([[sg.Text('Maximum number of words:', font=self.font, size=text_size),
                               sg.Slider(range=(0, 50000), default_value=self.transform_kwargs['max_words'],
                                         size=(20, 15), orientation='horizontal',
                                         font=self.font, key='_SLIDER_MAX_WORDS_')],
                              [sg.Text('Horizontal/Vertical ratio [%]:', font=self.font, size=text_size),
                               sg.Slider(range=(0, 100), default_value=self.transform_kwargs['hv_ratio'],
                                         size=(20, 15), orientation='horizontal',
                                         font=self.font, key='_SLIDER_H/V_RATIO_')],
                              [sg.Text('Relative scaling [%]:', font=self.font, size=text_size),
                               sg.Slider(range=(0, 100), default_value=self.transform_kwargs['relative_scaling'],
                                         size=(20, 15), orientation='horizontal',
                                         font=self.font, key='_SLIDER_RELATIVE_SCALING_')],
                              [sg.Text('Scale:', font=self.font, size=text_size),
                               sg.Slider(range=(0, 10), default_value=self.transform_kwargs['scale'],
                                         size=(20, 15), orientation='horizontal',
                                         font=self.font, key='_SLIDER_SCALE_')],
                              [sg.Text("Canvas' width: ", font=self.font, size=(20, 1)),
                               sg.Input(key='_INPUT_CANVAS_WIDTH_', default_text=self.transform_kwargs['canvas_width'],
                                        font=self.font, size=(10, 1)),
                               sg.Text("Canvas' height: ", font=self.font, size=(15, 1)),
                               sg.Input(key='_INPUT_CANVAS_HEIGHT_', default_text=self.transform_kwargs['canvas_height'],
                                        font=self.font, size=(10, 1))],
                              # [sg.Text('Scale:', font=self.font, size=text_size),
                              #  sg.Radio('My first Radio!', "RADIO1", default=True),
                              #    sg.Radio('My second radio!', "RADIO1")],
                              [sg.Text('Contour width:', font=self.font, size=text_size),
                               sg.Slider(range=(0, 100), default_value=self.transform_kwargs['contour_width'], size=(20, 15),
                                         orientation='horizontal', font=self.font, key='_SLIDER_CONTOUR_WIDTH_')],
                              [sg.Text('Minimum font size:', font=self.font, size=text_size),
                               sg.Slider(range=(0, 500), default_value=self.transform_kwargs['min_font_size'], size=(20, 15),
                                         orientation='horizontal', font=self.font, key='_SLIDER_MIN_FONT_')],
                              [sg.Text('Maximum font size:', font=self.font, size=text_size),
                               sg.Slider(range=(0, 500), default_value=self.transform_kwargs['max_font_size'],
                                         size=(20, 15), orientation='horizontal',
                                         font=self.font, key='_SLIDER_MAX_FONT_')],
                              [sg.Text('Colormap:', font=self.font, size=text_size),
                               sg.InputText(font=self.font, default_text=self.transform_kwargs['colormap'],
                                            key='_INPUT_COLORMAP_'),
                               sg.Button('See colormaps', key='_BUTTON_COLORMAPS_', font=self.font)],
                              [sg.Button('Reset', key='_RESET_', size=button_size, font=self.font),
                               sg.Button('Exit', key='_EXIT_', size=button_size, font=self.font),
                               sg.Button('Exit & Save', key='_EXIT_SAVE_SETTINGS_', size=button_size, font=self.font)]]),
                   sg.Column([[sg.Image(key='_PREVIEW_IMAGE_', source=self.base64_font_dict[self.default_font])],
                              [sg.Listbox(self.font_names_for_preview, size=(30, 20),
                                          default_values=self.transform_kwargs['font_path'],
                                          font=self.font, change_submits=True, key='_FONT_LIST_')]])]]
        self.window = sg.Window('Window Title', layout)

    # def init_default_values(self):
    #     for k, v in self.transform_kwargs.items():
    #         k_trans = self.translation[k]
    #         print(k_trans)
    #         if k_trans == '_FONT_LIST_':
    #             print(self.window[k_trans])
    #             self.window[k_trans].update(scroll_to_index=self.font_names_for_preview.index(v))
    #         elif k_trans in ['_INPUT_CANVAS_WIDTH_', '_INPUT_CANVAS_HEIGHT_', '_BUTTON_COLORMAPS_',
    #                          '_SLIDER_MAX_WORDS_', '_SLIDER_H/V_RATIO_', '_SLIDER_RELATIVE_SCALING_',
    #                    '_SLIDER_SCALE_', '_SLIDER_MIN_FONT_', '_SLIDER_MAX_FONT_',]:
    #             self.window[k_trans].update(value=v)
    #         else:
    #             raise ValueError('Parameter default value not implemented')

    def run(self):
        self.layout()
        while True:
            if self.values_before_hidden:
                event, new_values = self.window.read()
                if new_values is not None:
                    values = new_values
                else:
                    values = self.values_before_hidden
                self.values_before_hidden = None
            else:
                event, values = self.window.read()
            print(values['_INPUT_COLORMAP_'])

            if event == '_BUTTON_COLORMAPS_':
                self.window.hide()
                self.values_before_hidden = values
                self.subwindows['colormaps'].run()
                self.window.un_hide()
            elif event == '_FONT_LIST_':
                preview_image_elem = self.window['_PREVIEW_IMAGE_']
                preview_image_elem.update(source=self.base64_font_dict[values['_FONT_LIST_'][0]])
            elif event == '_EXIT_SAVE_SETTINGS_':
                self.update_transform_kwargs(values)
                self.window.close()
                break
            elif event in (sg.WIN_CLOSED, 'Cancel') or event == '_EXIT_':
                self.window.close()
                break

    def update_transform_kwargs(self, values):
        selected_font = values['_FONT_LIST_'] if values['_FONT_LIST_'] else self.window['_FONT_LIST_'].DefaultValues[0]
        print(values['_INPUT_COLORMAP_'])
        self.transform_kwargs = {'font_path': selected_font,
                'max_words': int(values['_SLIDER_MAX_WORDS_']),
                'hv_ratio': values['_SLIDER_H/V_RATIO_'],
                'relative_scaling': values['_SLIDER_RELATIVE_SCALING_'],
                'scale': values['_SLIDER_SCALE_'],
                'canvas_width': values['_INPUT_CANVAS_WIDTH_'],
                'canvas_height': values['_INPUT_CANVAS_HEIGHT_'],
                'contour_width': values['_SLIDER_CONTOUR_WIDTH_'],
                'min_font_size': int(values['_SLIDER_MIN_FONT_']),
                'max_font_size': int(values['_SLIDER_MAX_FONT_']),
                'colormap': values['_INPUT_COLORMAP_']}

