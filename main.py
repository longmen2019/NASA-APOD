"""Creating a black and white style image to avoid confusion
Grayscale images are simpler and faster to process"""

import cv2  # OpenCV library for image processing.
import numpy as np
from pyzbar.pyzbar import decode  # Function from the pyzbar library to decode barcodes and QR codes


# image = cv2.imread('images (1).png')  # Reads the image from the specified file path and loads it into a NumPy array

def decoder(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converts the loaded image from BGR color space to grayscale
    barcode = decode(
        gray_img)  # Uses the decode function from pyzbar to detect and decode any barcodes or QR codes in the grayscale image

    # Algorithm to scan the obtained image

    for obj in barcode:
        points = obj.polygon  # Retrieves the polygon points that outline the detected barcode
        (x, y, w,
         h) = obj.rect  # Retrieves the rectangle coordinates (x, y, width, height) that bound the detected barcode
        pts = np.array(points, np.int32)  # Converts the polygon points to a NumPy array of type int32
        pts = pts.reshape(
            (-1, 1, 2))  # Reshapes the points array to a format suitable for drawing the polygon with OpenCV functions.

        cv2.polylines(image, [pts], True, (0, 255, 0),
                      3)  # Draws the polygon on the original image in green color with a thickness of 3 pixels.

        barcodeData = obj.data.decode(
            "utf-8")  # Decodes the barcode data from the object and converts it to a UTF-8 string
        barcodeType = obj.type  # Extracts the barcode type from the object
        string = "Data" + str(barcodeData) + "| Type " + str(
            barcodeType)  # Creates a string containing the decoded data and barcode type
        cv2.putText(image, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0),
                    2)  # This line displays the string information (data and type) on the image at the top-left corner of the bounding rectangle ((x, y)) using a specific font and color.
        # print("Barcode: " + barcodeData + " | Type: " + barcodeType)


def main():
    """The code prompts the user to choose between two options: Scan via image and Scan via WebCam"""
    choice = int(input("1. Scan via image\n2. Scan via WebCam\n Choice: "))
    if choice == 2:
        """Accessing webcam for images"""
        cap = cv2.VideoCapture(
            0)  # The code captures video frames from the webcam using cv2.VideoCapture(0). (0 refers to the default webcam)
        while True:  # It enters a loop that continuously captures frames and calls the decoder function on each frame to process and decode any barcodes present
            ret, image = cap.read()
            decoder(image)
            cv2.imshow("Image",
                       image)  # The processed frames with highlighted barcodes and decoded data are displayed using cv2.imshow
            code = cv2.waitKey(10)
            if code == ord("q"):  # The code waits for a key press (q in this case) to terminate the webcam capture
                break
        cap.release()  # After the loop exists, this line releases the webcam resource
        cv2.destroyAllWindows()  # This closes any open windows used by OpenCV, like the "Image" window.

    else:
        # Scanning the qrcode in locally available image
        img_path = input(
            "Enter Image Path: ")  # This line prompts the user to enter the file path of the image containing the QR code
        img = cv2.imread(
            img_path)  # This line uses the cv2.imread function from OpenCV to load the image specified by the img_path into a NumPy array named img
        detector = cv2.QRCodeDetector()  # This line creates an instance of the QRCodeDetector class from OpenCV, which is used to detect and decode QR codes.

        """data, bbox, straight_qrcode = detector.detectAndDecode(img) This line calls the detectAndDecode method of the 
        detector object, passing the loaded image img as input. This method detects and decodes QR codes within the image.
        data: This variable stores the decoded data extracted from the QR code.
        bbox: This variable stores the bounding box coordinates of the detected QR code.
        straight_qrcode: This variable stores the straightened QR code image."""

        data, bbox, straight_qrcode = detector.detectAndDecode(img)  # etects and decodes QR codes within the image

        print("QRCode Encode Data: ", data)


if __name__ == "__main__":
    main()
