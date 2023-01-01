import time
from PIL import Image,ImageGrab
import pytesseract

# time.sleep(1)
# ImageGrab.grab().save('screen.jpg')
# img = Image.open('screen.jpg')
# icrop = img.crop((270, 280, 830, 410)).save('crop.jpg')

# time.sleep(1)

path_tesseract = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path_tesseract

image = Image.open('friend.png')

txt = pytesseract.image_to_string(image, lang='eng')

print(txt)