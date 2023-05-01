from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Tyant/Desktop/Projects/My Qr codes/python25projects.png')

results = decode(img)

print(results)