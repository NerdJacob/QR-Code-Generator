try:
    import qrcode
except:
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    install("qrcode")

# ↓ Update with the directory path for the txt file with the list of codes 
source_location = " "
# ↓ Update with the directory path to place the QR files
destination_location = " "

list_of_codes = []
file = open(source_location, 'r')
lines = file.readlines()
file.close()

for x in lines:
    list_of_codes.append(x)

# print(list_of_codes)

num = 1

for x in range(len(list_of_codes)):
    img = qrcode.make(f'https://store.pokemongolive.com/offer-redemption?passcode={list_of_codes[x]}')
    filename = f'{destination_location}{num}.png' 
    img.save(filename)
    type(img)
    num += 1

print('Yay!')
