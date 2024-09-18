"""Creating a black and white style image to avoid confusion
Grayscale images are simpler and faster to process"""
import cv2

image = cv2.imread('pexels-mccutcheon-1209843.jpg')

if image is None:
    print("Error: Could not load image")
else:
    gray_imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_imag)
