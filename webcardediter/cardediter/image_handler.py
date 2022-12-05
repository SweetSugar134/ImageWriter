from PIL import Image, ImageDraw, ImageFont
import math

import io
from webcardediter.settings import BASE_DIR


def resizer(image):
    print(type(image))
    im = Image.open(image)
    w, h = im.size
    height_difference = h / 800
    width_difference = w / 1000
    if height_difference > width_difference:
        h /= height_difference
        w /= height_difference
    else:
        w /= width_difference
        h /= width_difference
    im_resized = im.resize((math.floor(w), math.floor(h)))
    img_byte_arr = io.BytesIO()
    im_resized.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    print('image resizes!!!')
    return img_byte_arr


def drawer(image_bytes, text, pos, font_size, color='#ffffff'):
    font_path = BASE_DIR / 'cardediter' / 'static' / 'ArialRegular.ttf'
    im = Image.open(image_bytes)
    font = ImageFont.truetype(str(font_path), font_size)
    canvas = ImageDraw.Draw(im)
    print(font_size, text, pos)
    text = text.replace('\r\n', '\n')
    canvas.multiline_text(pos, font=font, text=text, fill=color)
    img_byte_arr = io.BytesIO()
    im.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    im.close()
    return img_byte_arr
