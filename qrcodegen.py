import qrcode
import image
qr=qrcode.QRCode(
    version=4, # 4 refers to the version of the qr code ,  higher the no bigger the code image and complicated picture
    box_size=4, #size of the box where qr code will be displayed
    border=5 # outline of image -- border in all 4 sides 
)

data="https://www.linkedin.com/in/nikhil-prasad-09716218a/" #any website address

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(back_color="cyan")
img.save("test.png")
