try:
    import qrcode
except:
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    install("qrcode")

list_of_codes = []

file = open("C:/Users/jacob/OneDrive/Documents/Python/QR Code Generator/input.txt", 'r')
lines = file.readlines()
file.close()

for x in lines:
    list_of_codes.append(x)

# print(list_of_codes)

num = 1

for x in range(len(list_of_codes)):
    img = qrcode.make(f'https://store.pokemongolive.com/offer-redemption?passcode={list_of_codes[x]}')
    filename = f'C:/Users/jacob/OneDrive/Documents/Python/QR Code Generator/output/00{num}.png' 
    img.save(filename)
    type(img)
    num += 1

print('Yay!')