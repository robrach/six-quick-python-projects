from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/home/robert/Six_Quick_Python_Projects/6 - QR coding/myqrcode_01.png')

result = decode(img)

print(result)