**# QR Code Scanner**

This project provides a Python script for scanning QR codes from either a webcam stream or a local image file. It utilizes OpenCV (cv2) for image processing and the pyzbar library for robust QR code decoding.

**## Functionality**

* **Webcam Scanning:** Capture QR codes in real-time using your webcam.
* **Image Scanning:** Decode QR codes from locally stored images.
* **Data Display:** Visually highlight the detected QR code with a bounding box and display the decoded data on the image.

**## Usage**

1. **Install Dependencies:**
   ```bash
   pip install opencv-python pyzbar
   ```

2. **Run the Script:**
   ```bash
   python qr_code_scanner.py
   ```

3. **Select Input Method:**
   - Choose 1 to scan using your webcam.
   - Choose 2 to scan a local image.

**## Webcam Scanning (Choice 1):**

   - The script will access your webcam and start displaying the video feed.
   - Focus the camera on a QR code to decode its information.
   - Press the "q" key on your keyboard to quit the live scanning.

**## Image Scanning (Choice 2):**

   - Enter the path to the image file containing the QR code when prompted.
   - The script will decode the QR code and display the decoded data in the terminal.

**## Script Breakdown:**

**1. Imports:**

   - `cv2`: OpenCV library for image processing and computer vision.
   - `numpy`: NumPy library for scientific computing.
   - `from pyzbar.pyzbar import decode`: Imports the QR code decoding function from the pyzbar library.

**2. `decoder` Function:**

   - Takes an image as input.
   - Converts the image to grayscale to facilitate QR code detection.
   - Uses `decode` from pyzbar to extract QR code information from the grayscale image.
   - Iterates through the decoded objects (if any):
      - Draws a green bounding box around the detected QR code.
      - Displays the decoded data (content and type) on the image using `cv2.putText`.
      - Prints the decoded data to the console.

**3. User Choice:**

   - Prompts the user to choose between webcam or image scanning.

**4. Webcam Scanning:**

   - Creates a `VideoCapture` object to access the webcam.
   - Enters a loop to capture continuous frames:
      - Reads a frame from the webcam.
      - Calls the `decoder` function to process the frame.
      - Displays the processed frame.
      - Waits for a key press for 10 milliseconds.
      - Quits the loop if the user presses "q".

**5. Image Scanning:**

   - Prompts the user for the image path.
   - Reads the image using `cv2.imread`.
   - Creates a `QRCodeDetector` object from OpenCV (alternative approach).
   - Calls the `detectAndDecode` method to attempt QR code detection and decoding:
      - If the QR code is detected, prints the decoded data.
   - (Optional) You can display the processed image with the bounding box and decoded data using OpenCV techniques.

**## Additional Notes**

- This script provides a basic implementation of QR code scanning.
- Error handling and user input validation can be further enhanced.
- Consider utilizing libraries like Pillow (PIL Fork) for advanced image processing and manipulation.
- Explore more advanced QR code decoding features offered by libraries like pyzbar.

