#add salt noise to girl image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

# Load girl.jpg image
image = cv2.imread('lena.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Add salt and pepper noise
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size
    num_salt = np.ceil(salt_prob * total_pixels)
    num_pepper = np.ceil(pepper_prob * total_pixels)

    # Add salt noise (white pixels)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 255

    # Add pepper noise (black pixels)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 0

    return noisy_image

#test the function
salt_prob = 0.02
pepper_prob = 0.02
noisy_image = add_salt_and_pepper_noise(image, salt_prob, pepper_prob)

# Display original and noisy images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)

plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(noisy_image)
plt.title('Noisy Image')

plt.axis('off')
plt.show()

# Save the noisy image
cv2.imwrite('noisy_lena.png', cv2.cvtColor(noisy_image, cv2.COLOR_RGB2BGR)) 

