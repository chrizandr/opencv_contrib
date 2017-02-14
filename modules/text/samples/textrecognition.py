#!/usr/bin/python

import sys
import os

import cv2
import numpy as np
import pdb

print('\ntextrecognition.py')
print('       A demo script of OpenCV Tesseract API for text recognition')


if (len(sys.argv) < 2):
  print(' (ERROR) You must call this script with an argument (path_to_image_to_be_processed)\n')
  quit()

img = cv2.imread(str(sys.argv[1]))

# Initialize the OCR API Object
ocr = cv2.text.OCRTesseract_create()

min_confidence = 0
max_confidence = 100
# Integers between 0-100, represents the confidence level of the OCR prediction

# Possible to iterate over confidence values and check the best result
# Covering all confidences for the sample, may be changed based on image
results = list()    # Storing the results in case it is needed later
for confidence in range(min_confidence , max_confidence):
    result = ocr.run(img, confidence, cv2.text.OCR_LEVEL_WORD)
    result = result.strip()     # Removing leading and trailing whitespaces
    if len(result) != 0 :
        results.append( (result,confidence) )
        print('Prediction : ' + result + ' Confidence : ' + str(confidence))
