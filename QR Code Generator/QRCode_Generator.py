import pyqrcode
from pyqrcode import QRCode

information = "My name is Shyam Makwana and is encoded in QRCode"

qrcode = pyqrcode.create(information)

qrcode.svg("qrcode.svg",scale=8)