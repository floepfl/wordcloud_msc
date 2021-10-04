#!/usr/bin/env python
#https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Font_Previewer.py
import sys
import PySimpleGUI as sg
from tkinter import font
from fonts_wrangling.base64_fonts import b64_font_dict
from fonts_wrangling.png_base64_fonts import base64_font_dict
import base64
import tkinter
import tkinter as tk
import pyglet
import os
root = tkinter.Tk()
font_names = list(base64_font_dict.keys())
font_names.sort()
root.destroy()

'''
    Showing fonts in PSG / tk
'''

sg.theme('Black')

layout = [[sg.Image(key='_PREVIEW_IMAGE_',)],
          [sg.Listbox(font_names, size=(30, 20), change_submits=True, key='_FONT_LIST_')]]

window = sg.Window('My new window', layout)

while True:     # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    preview_image_elem = window['_PREVIEW_IMAGE_']
    print(event, values)
    if values['_FONT_LIST_'] is not None and len(values['_FONT_LIST_']) >= 1:
        # font_filename = f"{values['-list-'][0]}.ttf"
        # print(font_filename)
        # if not os.path.isdir('/tmp/font_previewer'):
        #     os.mkdir('/tmp/font_previewer')
        # with open(f"/tmp/font_previewer/{font_filename}", "wb") as font_file:
        #     print(type(base64.b64decode(b64_font_dict[values['-list-'][0]])))
        #     print(type(base64.b64decode(b64_font_dict[values['-list-'][0]])[0]))
        #     #print(base64.b64decode(b64_font_dict[values['-list-'][0]]), file=font_file)
        #     font_file.write(base64.b64decode(b64_font_dict[values['-list-'][0]]))
        #
        # pyglet.font.add_file(os.path.join('/tmp/font_previewer', font_filename))  # Your TTF file name here
        # root = tk.Tk()
        # print(pyglet.font.load('fdsf'))
        # MyLabel = tk.Label(root, text="test", font=(values['-list-'][0], 25))
        # MyLabel.pack()
        # root.mainloop()
        # text_elem.update(font=values['-list-'][0])

        preview_image_elem.update(source=base64_font_dict[values['_FONT_LIST_'][0]])
window.close()