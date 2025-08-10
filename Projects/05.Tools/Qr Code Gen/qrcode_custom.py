import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://umairshakoor.vercel.app')
qr.make(fit=True)

img = qr.make_image(fill_color="yellow", back_color="black")
img.save('qrcode_custom.png')
