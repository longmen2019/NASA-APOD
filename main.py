"""Creating a black and white style image to avoid confusion
Grayscale images are simpler and faster to process"""

import cv2 #OpenCV library for image processing.
import numpy as np
from pyzbar.pyzbar import decode # Function from the pyzbar library to decode barcodes and QR codes

image = cv2.imread('images (1).png') #Reads the image from the specified file path and loads it into a NumPy array

if image is None:
    print("Error: Could not load image") #Checks if the image was successfully loaded. If not, it prints an error message
else:
    gray_imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Converts the loaded image from BGR color space to grayscale
print(gray_imag)
barcode = decode(gray_imag) #Uses the decode function from pyzbar to detect and decode any barcodes or QR codes in the grayscale image
print(" ")
print("barcode:", barcode)

# Algorithm to scan the obtained image

for obj in barcode:
    points = obj.polygon #Retrieves the polygon points that outline the detected barcode
    print(points)
    (x,y,w,h) = obj.rect #Retrieves the rectangle coordinates (x, y, width, height) that bound the detected barcode
    pts = np.array(points, np.int32) #Converts the polygon points to a NumPy array of type int32
    pts = pts.reshape((-1,1,2)) #Reshapes the array to the required format for drawing.

    cv2.polylines(image, [pts], True, (0,255,0), 3) #Draws the polygon on the original image in green color with a thickness of 3 pixels.
