import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def mirrorImage(image):
    height, width = image.shape[:2]

    mirrored_image = np.zeros_like(image)

    for y in range(height):
        for x in range(width):
            mirrored_image[height - y - 1, width - x - 1] = image[y, x]
    
    return mirrored_image

image = img.imread('C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\Praktikum_MirzaYusuf\\Gambar\\Tiger.jpg')

mirrored_image = mirrorImage(image)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(mirrored_image)
plt.title("Mirrored Image (Vertical & Horizontal)")

plt.show()
