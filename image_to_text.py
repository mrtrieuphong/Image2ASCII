import PIL.Image

ASCCI_CHARS = ["@", "#", "$", "%", "?", "*", "'", ";", ":", ",", "."]
new_width = 0

def resize_image(image):
    global new_width
    width, height = image.size
    ratio = height / width / 1.65
    if width >= height:
        new_width = 500
        new_height = int(new_width * ratio / 1.8)
        print('TH1 - ' + str(new_width) + ' - ' + str(new_height))
    else:
        new_height = 150
        new_width = int(new_height / ratio + 120 / ratio)
        print('TH2 - ' + str(new_width) + ' - ' + str(new_height))
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCCI_CHARS[pixel // 25] for pixel in pixels])
    return characters


def saveAsText(image_path):
    global new_width
    try:
        image = PIL.Image.open(image_path)
        new_image_data = pixels_to_ascii(grayify(resize_image(image)))
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))
        return ascii_image

    except:
        return "Error when converting"
