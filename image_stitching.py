import streamlit as st
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

st.title('Image Stitching')
st.subheader('Please Upload your Image')

image_paths = ['1.jpg', '2.jpg']

imgs = []
for i in range(len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))

# Show original images
cv2.imshow('1', imgs[0])
cv2.imshow('2', imgs[1])

# Resize the images
img1 = cv2.resize(imgs[0], (700, 550))
img2 = cv2.resize(imgs[1], (700, 550))

stitcher = cv2.Stitcher.create()
status, stitched_image = stitcher.stitch([img1, img2])

if status == cv2.Stitcher_OK:
    print('Your Panorama is ready!!!')
    cv2.imshow('Final Result', stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    stitched_image_rgb = cv2.cvtColor(stitched_image, cv2.COLOR_BGR2RGB)
    plt.imshow(stitched_image_rgb)
    plt.axis('on')
    plt.show()
else:
    print("Stitching ain't successful")
