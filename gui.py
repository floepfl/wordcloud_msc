import PySimpleGUI as sg
from wordcloud_transform import transform
from data.images import *

def main_window(font, image):
    sg.theme('DarkAmber')   # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    text_size = (20, 1)
    button_size = (15, 1)
    layout = [[sg.Column([[sg.Text('Input image: ', font=font, size=text_size), sg.Input(key='_INPUT_IMAGE_', default_text='.png or .jpg/jpeg', font=font), sg.FilesBrowse(font=font, size=(10,1))],
                [sg.Text('Words:', font=font, size=text_size), sg.Input(key='_INPUT_WORDS_', default_text='.numbers, .xlsx or .csv', font=font), sg.FilesBrowse(font=font, size=(10,1))],
                [sg.Text('Horizontal/Vertical ratio [%]:', font=font, size=text_size), sg.Slider(range=(0,100), default_value=90, size=(20,15), orientation='horizontal', font=font)],
                [sg.Text('Contour width:', font=font, size=text_size), sg.Slider(range=(0,100), default_value=0, size=(20,15), orientation='horizontal', font=font)],
                [sg.Text('Minimum font size:', font=font, size=text_size), sg.Slider(range=(0,500), default_value=4, size=(20,15), orientation='horizontal', font=font)],
                [sg.Text('Maximum font size:', font=font, size=text_size), sg.Slider(range=(0,500), default_value=160, size=(20,15), orientation='horizontal', font=font)],
                [sg.Text('Colormap:', font=font, size=text_size), sg.InputText(font=font, default_text='enter name'), sg.Button('See colormaps', key='go_to_colormaps', font=font)],
                [sg.Button('Reset to default settings', key='_RESET_', size=button_size, font=font), sg.Button('Transform', key='transform', size=(15,2), font=font)]]),
               image]]

    #TODO scale

    # layout = [[sg.Column([[sg.Text('Input image: ', font=font)], [sg.Text('Horizontal/Vertical ratio', font=font)]]),
    #                        sg.Column([[sg.Text('Horizontal/Vertical ratio', font=font)], [sg.Slider(range=(0,100))]])]]
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