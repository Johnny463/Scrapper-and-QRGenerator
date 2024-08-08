import qrcode
from PIL import Image

def create_qrcode(url:str):
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # taking url or text
    # url = 'https://www.activeloop.com/'

    # adding URL or text to QRcode
    QRcode.add_data(url)

    # adding color to QR code
    QRimg = QRcode.make_image(
        back_color="white").convert('RGB')
    return QRimg

def qr_with_logo(logo_path: str, QRimg: Image.Image, output_image_name: str):
    logo = Image.open(logo_path)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize))

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code generated
    QRimg.save(output_image_name)
    return QRimg

QRimg = create_qrcode("https://mianelectronics.streamlit.app/")
output_image = qr_with_logo("logo.png", QRimg, "qr_with_logo.png")