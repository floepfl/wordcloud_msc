import PySimpleGUI as sg
from wordcloud_transform import transform
from data.images import *

def main_window(font, image):
    sg.theme('DarkAmber')   # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    text_size = (20, 1)
    button_size = (15, 1)
    layout = [[sg.Column([[sg.Text('Input image: ', font=font, size=text_size),
                           sg.Input(key='_INPUT_IMAGE_', default_text='.png or .jpg/jpeg', font=font),
                           sg.FilesBrowse(font=font, size=(10,1))],
                [sg.Text('Words:', font=font, size=text_size),
                 sg.Input(key='_INPUT_WORDS_', default_text='.numbers, .xlsx or .csv', font=font),
                 sg.FilesBrowse(font=font, size=(10,1))],
                [sg.Text('Colormap:', font=font, size=text_size),
                 sg.InputText(font=font, default_text='None', key='_INPUT_COLORMAP_'),
                 sg.Button('See colormaps', key='colormaps', font=font)],
                [sg.Button('Settings', key='settings', size=(15,2), font=font),
                 sg.Button('Transform', key='transform', size=(15,2), font=font)]]),
               image]]

    #TODO scale, preview size, transparent_background, repeat

    # layout = [[sg.Column([[sg.Text('Input image: ', font=font)], [sg.Text('Horizontal/Vertical ratio', font=font)]]),
    #                        sg.Column([[sg.Text('Horizontal/Vertical ratio', font=font)], [sg.Slider(range=(0,100))]])]]
    return sg.Window('Window Title', layout)

def settings_window(font, font_names_for_preview, base64_font_dict, default_font):
    sg.theme('DarkAmber')  # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    text_size = (20, 1)
    button_size = (15, 1)
    layout = [[sg.Column([[sg.Text('Maximum number of words:', font=font, size=text_size),
                           sg.Slider(range=(0, 50000), default_value=200, size=(20, 15), orientation='horizontal',
                                     font=font, key='_SLIDER_MAX_WORDS_')],
                          [sg.Text('Horizontal/Vertical ratio [%]:', font=font, size=text_size),
                           sg.Slider(range=(0, 100), default_value=90, size=(20, 15), orientation='horizontal',
                                     font=font, key='_SLIDER_H/V_RATIO_')],
                          [sg.Text('Relative scaling [%]:', font=font, size=text_size),
                           sg.Slider(range=(0, 100), default_value=50, size=(20, 15), orientation='horizontal',
                                     font=font, key='_SLIDER_RELATIVE_SCALING_')],
                          [sg.Text('Scale:', font=font, size=text_size),
                           sg.Slider(range=(0, 10), default_value=1, size=(20, 15), orientation='horizontal',
                                     font=font, key='_SLIDER_SCALE_')],
                          [sg.Text("Canvas' width: ", font=font, size=(20, 1)),
                           sg.Input(key='_INPUT_CANVAS_WIDTH_', default_text='400', font=font, size=(10, 1)),
                           sg.Text("Canvas' height: ", font=font, size=(15, 1)),
                           sg.Input(key='_INPUT_CANVAS_HEIGHT_', default_text='200', font=font, size=(10, 1))],
                          # [sg.Text('Scale:', font=font, size=text_size),
                          #  sg.Radio('My first Radio!', "RADIO1", default=True),
                          #    sg.Radio('My second radio!', "RADIO1")],
                          [sg.Text('Contour width:', font=font, size=text_size),
                           sg.Slider(range=(0, 100), default_value=0, size=(20, 15),
                                     orientation='horizontal', font=font, key='_SLIDER_CONTOUR_WIDTH_')],
                          [sg.Text('Minimum font size:', font=font, size=text_size),
                           sg.Slider(range=(0, 500), default_value=4, size=(20, 15), orientation='horizontal',
                                     font=font, key='_SLIDER_MIN_FONT_')],
                          [sg.Text('Maximum font size:', font=font, size=text_size),
                           sg.Slider(range=(0, 500), default_value=160, size=(20, 15), orientation='horizontal',
                                     font=font, key='_SLIDER_MAX_FONT_')],
                          [sg.Button('Reset to default settings', key='_RESET_', size=button_size, font=font),
                           sg.Button('Save settings', key='_SAVE_SETTINGS_', size=button_size, font=font)]]),
                           sg.Column([[sg.Image(key='_PREVIEW_IMAGE_', source=base64_font_dict[default_font])],
                           [sg.Listbox(font_names_for_preview, size=(30, 20),
                                       default_values=default_font, font=font,
                                       change_submits=True, key='_FONT_LIST_')]])]]
    return sg.Window('Window Title', layout)


def colormap_window():
    sg.theme('DarkAmber')  # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [[sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/cyclic_and_uniform_sequential.png'),
               sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/sequential_2.png'),
               sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/qualitative.png')],
              [sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/sequential_1.png'),
               sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/diverging.png'),
               sg.Image(r'/Users/civiliste/PycharmProjects/wordcloud_app/data/misc.png')],]
    return sg.Window('Window Title', layout)

def loading(loading_gif):
    layout = [[sg.Image(loading_gif, key='_LOADING_GIF_')]]
    return sg.Window('', layout)

def fixed_loading(loading_image):
    layout = [[sg.Image(loading_image, key='_LOADING_IMAGE_')]]
    return sg.Window('', layout)