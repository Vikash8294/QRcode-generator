import pyqrcode
from pyqrcode import QRCode 
img = "https://myupes-beta.upes.ac.in/oneportal/app/auth/login"
url = pyqrcode.create(img)
url.svg("D:\python project\qr.svg",scale=10)