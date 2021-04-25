import numpy as np
import cv2
import matplotlib.pyplot as plt

img_raw = cv2.imread('image.jpg')
type(img_raw)
numpy.ndarray

img_raw.shape
(1300, 1950, 3)
plt.imshow(img_raw)
img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
