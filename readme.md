## QR Code Scanner - Python Project

This project is a simple QR code scanner written in Python using OpenCV and the pyzbar library. It allows you to scan QR codes from either an image file or directly from your webcam.

**Features:**

* Decodes QR codes from images or webcam feed.
* Displays the decoded data and type of QR code.
* Highlights the detected QR code in the image with a green polygon.

**Credits:**

* Inspiration and code structure based on the work of Mrinank Bhowmick ([https://github.com/Mrinank-Bhowmick/python-beginner-projects/blob/main/projects/QRCode%20Scanner/main.py](https://github.com/Mrinank-Bhowmick/python-beginner-projects/blob/main/projects/QRCode%20Scanner/main.py)) 

**How to Use:**

1. **Install dependencies:**

   ```bash
   pip install opencv-python pyzbar
   ```

2. **Run the script:**

   ```bash
   python qr_code_scanner.py
   ```

3. **Choose an option:**

   The script will prompt you to choose between scanning a QR code from an image (option 1) or your webcam (option 2).

4. **Scan via Image:**

   * Enter the file path of the image containing the QR code when prompted.

5. **Scan via Webcam:**

   * The script will access your webcam and display the live feed.
   * Press the "q" key to stop the webcam capture.

**Note:**

* This script uses grayscale images for faster processing.
* Ensure the image path is correct for scanning from an image.

This project provides a basic implementation of a QR code scanner. You can further enhance it by adding features like saving scanned data, handling different barcode formats, or improving error handling.
