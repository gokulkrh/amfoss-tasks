from PIL import Image
from pytesseract import image_to_string

img = Image.open(input('path of captcha image: '))
t = image_to_string(img)
print(eval(t))