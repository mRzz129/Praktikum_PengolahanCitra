import imageio.v3 as ing
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):
    
    imgTranslasi = np.roll(image, shift=shiftY, axis=0)
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)
    
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0
    elif shiftY < 0:
        imgTranslasi[:shiftY, :] = 0
    if shiftX > 0:
        imgTranslasi[:shiftX, :] = 0
    elif shiftX < 0:
        imgTranslasi[:shiftX, :] = 0
        
    return imgTranslasi

image = plt.imread("C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\Praktikum_MirzaYusuf\\Gambar\\Tiger.jpg")

imgResult = Translasi(image, shiftX=50, shiftY=-300)

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.imshow(image)
plt.imshow(imgResult)
plt.show()