#CREATED BY IVOOF_

import pyqrcode as QRCODE
import time
import sys

print("Welcome to the QR CODES GENERATOR!")
text = input("Enter the TEXT to convert it to QR CODE:")

try:
    print("Generating QR CODE, Please be patient.")
    toolbar_width = 40
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))
    for i in range(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("]\n")
    qrcode_text = QRCODE.create(text)
    qrcode_text.png("QRCODE.PNG")
except:
    print("An error occurred, try entering another text.")
print("Finished converting the TEXT TO QR CODE, check the destination folder!")

#CREATED BY IVOOF_