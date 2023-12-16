# -*- coding: utf-8 -*-
"""M22RM002_Q5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IobMJ0eFrHFaJ1GYDgnNvVusTIoZKZjh
"""

#a)Resize all images to 256 × 256. Convert it to gray.

import numpy as np
import cv2
from google.colab.patches import cv2_imshow 


img1=cv2.imread("victoria_memorial_1.jpg")
img1=cv2.resize(img1,(256,256))
gray_image_1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img2=cv2.imread("victoria_memorial_2.jpg")
img2=cv2.resize(img2,(256,256))
gray_image_2= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img3=cv2.imread("victoria_memorial_3.jpg")
img3=cv2.resize(img3,(256,256))
gray_image_3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=([15, 15]))
plt.subplot(131),plt.imshow(img1, cmap = 'gray')
plt.title('Input Image 1'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(gray_image_1,cmap = 'gray')
plt.title('Gray image 1'), plt.xticks([]), plt.yticks([])
plt.show()

plt.figure(figsize=([20, 20]))
plt.subplot(141),plt.imshow(img2, cmap = 'gray')
plt.title('Input Image 2'), plt.xticks([]), plt.yticks([])
plt.subplot(142),plt.imshow(gray_image_2,cmap = 'gray')
plt.title('Gray image 2'), plt.xticks([]), plt.yticks([])
plt.show()


plt.figure(figsize=([20, 20]))
plt.subplot(143),plt.imshow(img3, cmap = 'gray')
plt.title('Input Image 3'), plt.xticks([]), plt.yticks([])
plt.subplot(144),plt.imshow(gray_image_3,cmap = 'gray')
plt.title('Gray image 3'), plt.xticks([]), plt.yticks([])
plt.show()

#b)Show the average of all three images.
import glob
import numpy as np
import cv2
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

img1=cv2.imread("victoria_memorial_1.jpg")
img1=cv2.resize(img1,(256,256))

img2=cv2.imread("victoria_memorial_2.jpg")
img2=cv2.resize(img2,(256,256))


img3=cv2.imread("victoria_memorial_3.jpg")
img3=cv2.resize(img3,(256,256))

images=[img1,img2,img3]

image_data = []
for img in images:
    image_data.append(img)

avg_image = image_data[0]
for i in range(len(image_data)):
    if i == 0:
        pass
    else:
        alpha=beta=0.5
        avg_image = cv2.addWeighted(image_data[i], alpha, avg_image, beta, 0)


plt.figure(figsize=([20, 20]))
plt.subplot(131),plt.imshow(avg_image, cmap = 'gray')
plt.title('Average image')

#c)Subtract Image 1 with Image 2.


import cv2
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

img1=cv2.imread("victoria_memorial_1.jpg")
img1=cv2.resize(img1,(256,256))

img2=cv2.imread("victoria_memorial_2.jpg") 
img2=cv2.resize(img2,(256,256))

subtract = cv2.subtract(img1, img2)



plt.figure(figsize=([20, 20]))
plt.subplot(131),plt.imshow(img1, cmap = 'gray')
plt.title('Input Image 1'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img2, cmap = 'gray')
plt.title('Input Image 2'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(subtract)
plt.title('subtract image'), plt.xticks([]), plt.yticks([])
plt.show()

#d)5% noise
import numpy as np
import random
import cv2
import math
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
img=cv2.imread("victoria_memorial_2.jpg")
noise_img = sp_noise(img,0.05)
img=cv2.resize(img,(500,400))
noise_img=cv2.resize(noise_img,(500,400))

plt.figure(figsize=([30, 30]))
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image '), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(noise_img, cmap = 'gray')
plt.title('Noise Image'), plt.xticks([]), plt.yticks([])

#e)5% noise and removal
import numpy as np
import random
import cv2
import math
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
img=cv2.imread("victoria_memorial_2.jpg")
noise_img = sp_noise(img,0.05)


img_median = cv2.medianBlur(noise_img,3) 


plt.figure(figsize=([30, 30]))
plt.subplot(131),plt.imshow(noise_img, cmap = 'gray')
plt.title('Noise Image '), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_median, cmap = 'gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])

#convolution
import cv2
import numpy as np

img1=cv2.imread("victoria_memorial_1.jpg")
 

image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
 
# Apply identity kernel
kernel1 = np.array([[-1, -1, -1],
                    [0, 0, 0],
                    [1, 1, 1]])
 
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

plt.figure(figsize=([30, 30]))
plt.subplot(131),plt.imshow(image, cmap = 'gray')
plt.title('Input  Image '), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(identity, cmap = 'gray')
plt.title('Convolved Image'), plt.xticks([]), plt.yticks([])

