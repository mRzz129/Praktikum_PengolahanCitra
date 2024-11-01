import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    
    height, width = image.shape[:2]
    max_dim = int(np.sqrt(height**2 + width**2))
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)

    for y in range(height):
        for x in range(width):
            newY = int(cos_deg * y - sin_deg * x)
            newX = int(sin_deg * y + cos_deg * x)
            
            shiftedY = newY + max_dim // 2
            shiftedX = newX + max_dim // 2
            
            if 0 <= shiftedX < max_dim and 0 <= shiftedY < max_dim:
                outputImage[shiftedY, shiftedX] = image[y, x]
                
    return outputImage  

image = img.imread('C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\Praktikum_MirzaYusuf\\Gambar\\Tiger.jpg')

rotated_image = rotateImage(image, 45)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Rotated Image (Pivot at Top-Left)")

plt.show()
