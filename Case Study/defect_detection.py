# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:26:20 2024

@author: Sean_Lin
"""

import cv2 as cv
import numpy as np

src = cv.imread("ce_02.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 图像二值化
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
binary = cv.morphologyEx(binary, cv.MORPH_OPEN, se)
cv.imshow("binary", binary)

# 轮廓提取
contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
height, width = src.shape[:2]
for c in range(len(contours)):
    x, y, w, h = cv.boundingRect(contours[c])
    area = cv.contourArea(contours[c])
    if h > (height//2):
        continue
    if area < 150:
        continue
    cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0)
    cv.drawContours(src, contours, c, (0, 255, 0), 2, 8)

cv.imshow("result", src)
cv.imwrite("D:/binary2.png", src)

cv.waitKey(0)
cv.destroyAllWindows()