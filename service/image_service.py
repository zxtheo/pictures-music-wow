#image_service

from PIL import Image
from data.image_data import ImageData

def get_image_data(image):
    try:
        im = Image.open("{}".format(image), 'r')
    except:
        im = Image.open("data/images/{}".format(image), 'r')

    pix_val = list(im.getdata())
    return ImageData(pix_val)
