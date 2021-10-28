from pyzbar.pyzbar import decode
from PIL import Image
import sys

path_the_same_as_python_script = sys.path[0]

img = Image.open(path_the_same_as_python_script + '/myQRcode.png')
result = decode(img)
print(result)