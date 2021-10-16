import cv2
path= "img/img.jpg"

image= cv2.imread(path)
window_name= "Image"

image= cv2.copyMakeBorder(image, 5, 10, 15, 20, cv2.BORDER_REFLECT, None, value=1)
cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()