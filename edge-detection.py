# use canny edge detection to find edges in noise_lena.png image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the noisy image
image = cv2.imread('noisy_lena.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Apply Gaussian blur to reduce noise and improve edge detection
image_blur = cv2.GaussianBlur(image_gray, (5, 5), 1.5)

# Apply Canny edge detection
edges = cv2.Canny(image_blur, 80, 200)

# Display original and edge-detected images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_blur, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')

#Display the edge-detected image
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detected Image')
plt.axis('off')
plt.show()
