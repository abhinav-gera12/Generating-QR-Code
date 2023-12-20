# importing qrcode from python library
# downloading the qrcode library while typing pip install qrcode in the terminal if you have created the virtual environment there unless it won't work.
# you can create any qrcode likewise any link of your website or youtube link, even you can create your google pay, paytm qr code.


import qrcode as qr

image = qr.make("https://github.com/abhinav-gera12")                   # image is a variable and .make is an attribute method that i am using from the qrcode library which generates the qr-code and get stored in the variable.

image.save("abhinav_github_profile.png")                               #saving the image with the extension of .png and you can see your qrcode in the followed directory.
