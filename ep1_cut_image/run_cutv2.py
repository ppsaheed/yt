import cv2
import numpy as np

# Load the image
image = cv2.imread('og.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blurred, 30, 150)

# Perform a dilation and erosion to close gaps in between object edges
dilated = cv2.dilate(edges, None, iterations=2)
eroded = cv2.erode(dilated, None, iterations=1)

# Find contours in the eroded image
contours, hierarchy = cv2.findContours(eroded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours
for i, contour in enumerate(contours):
    # Compute the bounding box for the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Extract the individual notebook
    notebook = image[y:y+h, x:x+w]

    # Save the individual notebook
    cv2.imwrite(f'notebook_{i+1}.jpg', notebook)
