import cv2

path= "img/img.jpg"
image= cv2.imread(path)

cv2.imshow("Original Image", image)
cv2.waitKey(0)

#Gaussian Blur
gaussian= cv2.GaussianBlur(image,(7, 7), 0)
cv2.imshow("Gaussian Image", gaussian)
cv2.waitKey(0)

#Median Blur
median= cv2.medianBlur(image, 5)
cv2.imshow("Median Image", median)
cv2.waitKey(0)
