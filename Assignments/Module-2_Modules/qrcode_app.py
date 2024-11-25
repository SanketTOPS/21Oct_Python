import qrcode

#qr=qrcode.make("https://www.tops-int.com/")
#qr.save('tops.png')

qr=qrcode.make("Hello Students! This is secret msg!")
qr.save('secret.png')