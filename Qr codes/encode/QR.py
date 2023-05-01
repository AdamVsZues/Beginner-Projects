import qrcode

data = "https://www.youtube.com/@JoeButter42"

img = qrcode.make(data)

img.save('C:/Users/Tyant/Desktop/Projects/My Qr codes/TheBestChannel.png')
