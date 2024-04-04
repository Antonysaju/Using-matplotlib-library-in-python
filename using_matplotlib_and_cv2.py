import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mping

image= cv2.imread("99.jpg")
plt.axis("off")
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()
