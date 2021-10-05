import pandas as pd
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.stats import pareto
import base64
from io import BytesIO
from fonts_wrangling.base64_fonts import b64_font_dict

def pil_image_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")
    pil_image_str = base64.b64encode(buffered.getvalue())
    return pil_image_str

def create_ttf_file(font_name):
    dir_path = "/tmp/font_previewer/"
    path = os.path.join(dir_path, f"{font_name}.ttf")
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    with open(path, "wb") as font_file:
                # print(type(base64.b64decode(b64_font_dict[values['-list-'][0]])))
                # print(type(base64.b64decode(b64_font_dict[values['-list-'][0]])[0]))
                #print(base64.b64decode(b64_font_dict[values['-list-'][0]]), file=font_file)
                font_file.write(base64.b64decode(b64_font_dict[font_name]))
    return path

def transform(image_path, words_path, font_path, max_words, hv_ratio,
              relative_scaling, scale, canvas_width, canvas_height,
              contour_width, min_font_size, max_font_size, colormap):

    words_and_weights_df = pd.read_csv(words_path, sep=';')
    words_and_weights_dict = dict(zip(words_and_weights_df.iloc[:, 0],
                                      words_and_weights_df.iloc[:, 1]))
    image = Image.open(path.join(os.getcwd(), image_path)).convert('RGBA')
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)
    # coloring = np.array(Image.open(path.join(os.getcwd(), image_path)))
    coloring = np.array(new_image)

    font_path = create_ttf_file(font_path[0])
    if colormap != 'None':
        wc = WordCloud(background_color=None, mode='RGBA', font_path=font_path, max_words=max_words, mask=coloring,
                       stopwords=None, contour_width=contour_width, min_font_size=min_font_size, prefer_horizontal=hv_ratio / 100,
                       scale=scale, width=canvas_width, height=canvas_height, colormap=colormap,
                       max_font_size=max_font_size, random_state=42, relative_scaling=relative_scaling / 100)
        wc.generate_from_frequencies(words_and_weights_dict)
        wc = wc.to_image()
    else:
        wc = WordCloud(background_color=None, mode='RGBA', font_path=font_path, max_words=max_words, mask=coloring,
                       stopwords=None, contour_width=contour_width, min_font_size=min_font_size,
                       prefer_horizontal=hv_ratio / 100, repeat=True,
                       scale=scale, width=canvas_width, height=canvas_height,
                       max_font_size=max_font_size, random_state=42, relative_scaling=relative_scaling / 100)
        wc.generate_from_frequencies(words_and_weights_dict)
        image_colors = ImageColorGenerator(coloring)
        wc = wc.recolor(color_func=image_colors).to_image()
    output_image_size = wc.size
    preview_wc = wc.resize(size=(1024, 1024))
    preview_wc_str = pil_image_to_base64(preview_wc)
    return wc, preview_wc_str, output_image_size

    # # show
    # fig, ax = plt.subplots(1, 1)
    # fig.set_figheight(200)
    # fig.set_figwidth(200)
    # ax.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    # ax.set_axis_off()
    # plt.show()