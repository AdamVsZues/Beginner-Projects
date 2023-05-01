import qrcode

#link
data = ""

img = qrcode.make(data)

#where to save
img.save('C:/Users/Tyant/Desktop/Projects/My Qr codes/placeholder.png')
