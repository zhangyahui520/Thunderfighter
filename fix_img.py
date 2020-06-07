#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : fix_img.py
    Author      : Charles zhang
    Created date: 2020/6/7 14:48
    Description :
       
"""
import cv2

img =cv2.imread('./img/spaceship1.jpg')
cv2.imshow('img', img)

img1 = cv2.resize(img, (int(img.shape[0]*0.2), int(img.shape[1]*0.2)))
cv2.imshow('img1', img1)

cv2.imwrite('./img/spaceship1_mini.png', img1)

cv2.waitKey(0)