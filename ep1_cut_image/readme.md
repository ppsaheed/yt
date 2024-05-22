## count the squares
Based on the image description, there are 12 squares in the image. Each square contains a different design of a notebook. The squares are likely representing different models of notebooks in a catalog. Each square includes the model number, pricing information, and size details of the notebook. Hope this helps! 😊

## write a program cut the 12 squre and save as to individual

Sure, I can help you with that. Here's a Python program using OpenCV to cut out squares from an image. This is a simple example and might need to be adjusted based on the actual image and the location of the squares.

Please install the necessary libraries by running:

```
pip install opencv-python numpy
```

Here's the Python code:
```
import cv2
import numpy as np

# Load the image
image = cv2.imread('notebooks.jpg')

# Define the coordinates of the squares
squares = [
    # (top left x, top left y, width, height)
    (x, y, w, h) for x, y, w, h in [
        # Add the coordinates of the 12 squares here
        # For example: (10, 10, 200, 200)
    ]
]

# Loop over the squares
for i, (x, y, w, h) in enumerate(squares):
    # Cut out the square
    square = image[y:y+h, x:x+w]

    # Save the square
    cv2.imwrite(f'square_{i+1}.jpg', square)
```

In this code, you need to replace 'notebooks.jpg' with the path to your image. Also, you need to replace the list of coordinates with the actual coordinates of the squares in your image. The coordinates are in the format (x, y, width, height), where (x, y) is the top-left corner of the square.
Please note that this is a simple example and might not work perfectly for your specific image. You might need to adjust the coordinates or use image processing techniques to automatically detect and cut out the squares. If you need further assistance, feel free to ask! 😊
