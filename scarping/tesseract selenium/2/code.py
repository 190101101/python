from PIL import Image,ImageGrab
import pytesseract

c_path = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = c_path

image = Image.open('friend.png')

text = pytesseract.image_to_string(image, lang='eng')

print(text)