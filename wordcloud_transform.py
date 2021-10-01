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

def pil_image_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")
    pil_image_str = base64.b64encode(buffered.getvalue())
    return pil_image_str

def transform(image_path, words_path, font_path, max_words, hv_ratio,
              relative_scaling, scale, canvas_width, canvas_height,
              contour_width, min_font_size, max_font_size, colormap):

    words_and_weights_df = pd.read_csv(words_path, sep=';')
    words_and_weights_dict = dict(zip(words_and_weights_df.iloc[:, 0],
                                      words_and_weights_df.iloc[:, 1]))
    image = Image.open(path.join(os.getcwd(), image_path))
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)
    coloring = np.array(Image.open(path.join(os.getcwd(), image_path)))


    wc = WordCloud(background_color=None, mode='RGBA', font_path=font_path, max_words=2000, mask=coloring,
                   stopwords=None, contour_width=contour_width, min_font_size=min_font_size,
                   max_font_size=max_font_size, random_state=42, relative_scaling=1)
    wc.generate_from_frequencies(words_and_weights_dict)
    image_colors = ImageColorGenerator(coloring)
    wc = wc.recolor(color_func=image_colors).to_image()
    preview_wc = wc.resize(size=(1024, 1024))
    wc_str = pil_image_to_base64(wc)
    preview_wc_str = pil_image_to_base64(preview_wc)
    return wc_str, preview_wc_str

    # # show
    # fig, ax = plt.subplots(1, 1)
    # fig.set_figheight(200)
    # fig.set_figwidth(200)
    # ax.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    # ax.set_axis_off()
    # plt.show()