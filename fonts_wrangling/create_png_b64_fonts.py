from fontpreview import FontPreview
import base64
from io import BytesIO
import sys, os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import numpy as np

def ttf_to_base64png(font_file_path, preview_text):
    fp = FontPreview(font_file_path)
    fp.font_text = preview_text
    fp.bg_color = (253, 194, 45)
    fp.dimension = (800, 200)
    fp.fg_color = (51, 153, 193)
    fp.set_text_position('center')
    fp.draw()

    # Uncomment to draw
    # imshow(np.asarray(fp.image))
    # plt.show()

    buffered = BytesIO()
    fp.image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue())


if __name__ == '__main__':
    all_font_dir = sys.argv[1] # Extract font directory location
    preview_text = sys.argv[2]
    print(f'Path is: {all_font_dir}')

    # Create dict
    base64_font_dict = {}
    for font_dir in os.listdir(all_font_dir):
        if font_dir[0] != '.':
            font_dir_path = os.path.join(all_font_dir, font_dir)
            for font_file in os.listdir(font_dir_path):
                font_file_name = '.'.join(font_file.split('.')[:-1])
                font_file_path = os.path.join(font_dir_path, font_file)
                base64_font_dict[font_file_name] = ttf_to_base64png(font_file_path, preview_text)

    # Save to file
        with open('png_base64_fonts.py', 'w') as f:
            print('base64_font_dict = ', end='', file=f)
            print(base64_font_dict, file=f)