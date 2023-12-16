# -*- coding: utf-8 -*-
"""M22RM002_Q9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LXqsx8DDb9RORXaXlM8yy_Oa4stjpkJy
"""

import numpy as np
import cv2 
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow 


img = cv2.imread("victoria_memorial_1.jpg")
hist = cv2.calcHist([img], [0], None, [10], [0, 256])
plt.title("Original Image")
plt.plot(hist)
plt.show()

import numpy as np
import cv2 
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow


img = cv2.imread("victoria_memorial_1.jpg")
hist = cv2.calcHist([img], [0], None, [10], [0, 256])
plt.title("Original Image histogram")
plt.plot(hist)
plt.show()
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img_gray)
res = np.hstack((img_gray,equ)) #stacking images side-by-side

hist1 = cv2.calcHist([equ], [0], None, [10], [0, 256])
plt.plot(hist1)
plt.title("Equalization image histogram")
plt.show()

img=cv2.resize(img,(600,400))
equ=cv2.resize(equ,(600,400))
cv2_imshow(img)
cv2_imshow(equ)
