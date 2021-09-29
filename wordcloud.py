import pandas as pd
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.stats import pareto


def transform(image_path, weights, contour_width):
    image = Image.open(path.join(os.getcwd(), 'data/#0e.png'))
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)
    coloring = np.array(Image.open(path.join(os.getcwd(), 'data/colored_silhouettes.jpg')))
    wc = WordCloud(background_color="white", max_words=2000, mask=coloring,
                   stopwords=None, contour_width=0, max_font_size=40, random_state=42, relative_scaling=1)
    wc.generate_from_frequencies(weights)
    image_colors = ImageColorGenerator(coloring)
    wc = wc.recolor(color_func=image_colors)
    return wc
    # # show
    # fig, ax = plt.subplots(1, 1)
    # fig.set_figheight(200)
    # fig.set_figwidth(200)
    # ax.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    # ax.set_axis_off()
    # plt.show()