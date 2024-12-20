import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=5)
url=input("Enter the URL: ")
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill_color='black',back_color='white')
img.save('qrcode.png')
img.show()
