import base64

with open("/Users/civiliste/PycharmProjects/wordcloud_app/data/image_placeholder.png", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
print(b64_string)