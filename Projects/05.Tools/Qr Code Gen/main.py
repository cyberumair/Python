# pip install qrcode qrcode[pil]

import qrcode as qr
img = qr.make('https://umairshakoor.vercel.app')
img.save('main.png')
