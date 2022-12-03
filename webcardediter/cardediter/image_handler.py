from PIL import Image


def resizer(image):
    im = Image.open(image)
    h, w = im.size
    (width, height) = (im.width // 2, im.height // 2)
    im_resized = im.resize((width, height))
    return im_resized.getdata()

    # print(type(image.read()))
    # print(Image.frombytes())
