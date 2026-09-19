#name Husnain Nadeem
#reg no 23-ntu-cs-1038
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
# Load the image
image = plt.imread('image.jpg')
# Display the image
for i in range(1, 4):
    plt.subplot(1, 3, i)
    plt.imshow(image)
    plt.axis('off')

plt.show()