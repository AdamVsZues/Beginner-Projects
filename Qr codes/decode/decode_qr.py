from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Tyant/Desktop/Projects/My Qr codes/placeholder.png')

results = decode(img)

print(results)