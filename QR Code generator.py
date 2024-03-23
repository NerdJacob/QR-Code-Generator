import os # os import needed for realtive file path
try:
    import qrcode
except:
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    install("qrcode")
# ↑ import qrcode (generator) or, on fail install and import
dirname = os.path.dirname(__file__)

list_of_codes = []
inputfile = os.path.join(dirname, 'input.txt')
file = open(inputfile, 'r')
lines = file.readlines()
file.close()

for x in lines: # append each QR code from the input list to an array
    list_of_codes.append(x)

# print(list_of_codes)

num = 1

for x in range(len(list_of_codes)):
    img = qrcode.make(f'https://store.pokemongolive.com/offer-redemption?passcode={list_of_codes[x]}')
    filename = os.path.join(dirname, f'output/QR{num}.png')
    # filename = f'output/QR{num}.png' 
    img.save(filename)
    type(img)
    num += 1

print('Yay!')
