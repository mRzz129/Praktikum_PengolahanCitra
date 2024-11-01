import numpy as np
import matplotlib.pyplot as plt
import imageio as img

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            
            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)

            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

image = img.imread('C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\Praktikum_MirzaYusuf\\Gambar\\Tiger.jpg')
scale = 0.5

imgZoom = zoomMinus(image, scale)
img.imwrite("C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\Praktikum_MirzaYusuf\\Gambar\\Tiger_zoomed_down.jpg", imgZoom)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(imgZoom)
plt.title("Zoomed-Out Image")

plt.show()
