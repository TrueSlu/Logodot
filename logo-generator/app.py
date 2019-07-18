
from PIL import Image, ImageDraw, ImageFont, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, (255, 0, 0, 0))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    else:
        raise ValueError("cannot trim; image was empty")

def generate():
    font = ImageFont.truetype('./fonts/montserrat/Montserrat-Light.otf', size=600)
    #font = ImageFont.truetype('./fonts/metropolis/Metropolis-Bold.otf', size=600)
    (x, y) = (0, 0) # x = 22 for the I in Roboto Mono font
    color = '#C0C0C0' # white color
    dotcolor = '#8B008B'

    image = Image.new('RGBA', (10000, 10000), (255, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    message1 = 'Logodot'
    message2 = '.'

    draw.text((x, y), message1, fill=color, font=font)
    width = font.getsize(message1)[0]
    draw.text((width, y), message2, fill=dotcolor, font=font)

    image = trim(image)
    image.save('./logo.png')

generate()