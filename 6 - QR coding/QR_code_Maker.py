import qrcode
import sys

path_the_same_as_python_script = sys.path[0]

data = "https://github.com/robrach"     # It will be coded in QR code.
img = qrcode.make(data)
img.save(path_the_same_as_python_script + '/myQRcode.png')