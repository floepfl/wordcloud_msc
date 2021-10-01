import base64
import os
import sys

if __name__ == '__main__':
    all_font_dir = sys.argv[1] # Extract font directory location

    # Create dict
    b64_font_dict = {}
    print(f'Path is: {all_font_dir}')
    for font_dir in os.listdir(all_font_dir):
        if font_dir[0] != '.':
            font_dir_path = os.path.join(all_font_dir, font_dir)
            for font_file in os.listdir(font_dir_path):
                    font_file_name = '.'.join(font_file.split('.')[:-1])
                    font_file_path = os.path.join(font_dir_path, font_file)
                    with open(font_file_path, "rb") as font_file_bin:
                        b64_font_dict[font_file_name] = base64.b64encode(font_file_bin.read())

    # Save to file
    with open('base64_fonts.py', 'w') as f:
        print('b64_font_dict = ', file=f)
        print(b64_font_dict, file=f)

