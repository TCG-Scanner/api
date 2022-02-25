from os import getenv
from PIL import Image
from pytesseract import pytesseract
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

image_path = "test.jpg"

img = Image.open(image_path)

if (tesseract_path := getenv("TESSERACT_PATH")) is not None:
    pytesseract.tesseract_cmd = tesseract_path

test = pytesseract.image_to_string(img)
print(test)
