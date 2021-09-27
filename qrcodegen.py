import qrcode
import image
qr=qrcode.QRCode(
    version=4, # 15 refers to the version of the qr code ,  higher the no bigger the code image and complicated picture
    box_size=4, #size of the b0x where qr code will be displayed
    border=5 #it is the white part of image -- border in all 4 sides with white color
)

data="https://www.linkedin.com/in/nikhil-prasad-09716218a/" #any website address

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(back_color="cyan")
img.save("test.png")
