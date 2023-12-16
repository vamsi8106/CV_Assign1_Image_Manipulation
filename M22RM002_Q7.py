# -*- coding: utf-8 -*-
"""M22RM002_Q7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_5PTVJVVv6ZamkWhtgCZI6uIiaaZjrge
"""

import sys                      
import cv2                     
import numpy as np
from collections import Counter
from google.colab.patches import cv2_imshow 



class BackgroundColorDetector():
    def __init__(self,img):
        self.img = img
        self.manual_count = {}
        self.w, self.h, self.channels = self.img.shape
        self.total_pixels = self.w*self.h

    def count_function(self):
        for y in range(0, self.h):
            for x in range(0, self.w):
                RGB = (self.img[x, y, 2], self.img[x, y, 1], self.img[x, y, 0])
                if RGB in self.manual_count:
                    self.manual_count[RGB] += 1
                else:
                    self.manual_count[RGB] = 1

    def average_colour(self):
        red = 0
        green = 0
        blue = 0
        sample = 10
        for top in range(0, sample):
            red += self.number_counter[top][0][0]
            green += self.number_counter[top][0][1]
            blue += self.number_counter[top][0][2]

        average_red = red / sample
        average_green = green / sample
        average_blue = blue / sample
        self.backgroundcolor1(average_red,average_green,average_blue)
        
    def backgroundcolor1(self,average_red,average_green,average_blue):
        if(average_red<190 and average_green<190 and average_blue<190):
            print("Background is dark and text is bright")
       

    def twenty_most_common(self):
        self.count_function()
        self.number_counter = Counter(self.manual_count).most_common(20)
    def backgroundcolor2(self,x):
         if (x[0]>200 and x[1]>200 and x[2]>200):
                print("Background is bright and text is dark")
        
    def detect(self):
        self.twenty_most_common()
        self.percentage_of_first = (
            float(self.number_counter[0][1])/self.total_pixels)
        if self.percentage_of_first > 0.5:
            self.backgroundcolor2(self.number_counter[0][0])  
        else:
            self.average_colour()


if __name__ == "__main__":
    img=cv2.imread("black_on_white.png")
    cv2_imshow(img)
    BackgroundColor = BackgroundColorDetector(img)
    
    BackgroundColor.detect()

