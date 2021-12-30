from PIL import Image, ImageDraw, ImageFont
import os
import sys


def saveAsImage(image_path, new_height):
    chars = " .'`^\",:;I1!i><-+_-?][}{1)(|\/tfjrxnuvczXYUCLQ0OZmwqpbdkhao*#MW&8%B@$"
    fixed_height = new_height
    char_width = 9
    char_height = 9
    image = Image.open(image_path)
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), Image.NEAREST)
    WIDTH, HEIGHT = image.size
    image = image.resize((
        int(WIDTH / char_width),
        int(HEIGHT / char_height)
    ), Image.NEAREST)
    width, height = image.size
    image = image.load()
    ascii_image = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    font = ImageFont.truetype("arial.ttf", 14)
    drawImage = ImageDraw.Draw(ascii_image)

    def getChar(value):
        return chars[int(value * (len(chars) / 256))]

    try:
        for i in range(height):
            for j in range(width):
                r, g, b = image[j, i]
                k = int((r + g + b) / 3)
                drawImage.text(
                    (j * char_width, i * char_height),
                    getChar(k),
                    font=font,
                    fill=(r, g, b)
                )
    except:
        print('')
    return ascii_image
