import qrcode

data = "https://github.com/robrach"

img = qrcode.make(data)

img.save('/home/robert/Six_Quick_Python_Projects/6 - QR coding/myqrcode_01.png')