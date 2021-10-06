import base64

images = ['/Users/civiliste/PycharmProjects/wordcloud_app/data/cyclic_and_uniform_sequential.png',
'/Users/civiliste/PycharmProjects/wordcloud_app/data/sequential_2.png',
'/Users/civiliste/PycharmProjects/wordcloud_app/data/qualitative.png',
'/Users/civiliste/PycharmProjects/wordcloud_app/data/sequential_1.png',
'/Users/civiliste/PycharmProjects/wordcloud_app/data/diverging.png',
'/Users/civiliste/PycharmProjects/wordcloud_app/data/misc.png',
'/Users/civiliste/PycharmProjects/wordcloud_app/data/image_placeholder.png']

b64_image_dict = {}
for image_path in images:
    with open(image_path, "rb") as font_file_bin:
        image_name = image_path.split('/')[-1].split('.')[0]
        b64_image_dict[image_name] = base64.b64encode(font_file_bin.read())

# Save to file
with open('base64_images.py', 'w') as f:
    print('b64_image_dict = ', end='', file=f)
    print(b64_image_dict, file=f)



