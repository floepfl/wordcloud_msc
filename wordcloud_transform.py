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




def transform(image_path, words_path, contour_width, min_font_size, max_font_size):
    words_and_weights_df = pd.read_csv(words_path, sep=';')
    print(words_and_weights_df)
    words_and_weights_dict = dict(zip(words_and_weights_df.iloc[:, 0],
                                      words_and_weights_df.iloc[:, 1]))
    print(words_and_weights_dict)
    image = Image.open(path.join(os.getcwd(), image_path))
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)
    coloring = np.array(Image.open(path.join(os.getcwd(), image_path)))
    wc = WordCloud(background_color="white", max_words=2000, mask=coloring,
                   stopwords=None, contour_width=contour_width, min_font_size=min_font_size,
                   max_font_size=max_font_size, random_state=42, relative_scaling=1)
    wc.generate_from_frequencies(words_and_weights_dict)
    image_colors = ImageColorGenerator(coloring)
    wc = wc.recolor(color_func=image_colors).to_image()
    buffered = BytesIO()
    wc.save(buffered, format="PNG")
    wc_str = base64.b64encode(buffered.getvalue())
    return wc_str
    # # show
    # fig, ax = plt.subplots(1, 1)
    # fig.set_figheight(200)
    # fig.set_figwidth(200)
    # ax.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    # ax.set_axis_off()
    # plt.show()