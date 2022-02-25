from PIL import Image
from pytesseract import pytesseract

image_path = "test.jpg"

img = Image.open(image_path)

#  pytesseract.tesseract_cmd = path

test = pytesseract.image_to_string(img)
print(test)
