import qrcode

features=qrcode.QRCode(version=1,box_size=40,border=5)

features.add_data("https://www.youtube.com/results?search_query=seethala+ruchulu")
features.make(fit=True)

myqr = features.make_image(fill_color="black",back_color="white")
myqr.save("myqr8.png")