import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data("https://youtube.com/@ishashiva-0?si=1zDXcr5l1ROawpev")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("img1.png")