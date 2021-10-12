import cv2
path= "img/img.jpg"

image= cv2.imread(path)
window_name= "Image"

font= cv2.FONT_HERSHEY_COMPLEX
org= (50, 50)
fontScale= 2
color= (255, 0, 0)
thickness= 2
text= "Computer Vision"

image= cv2.putText(image, text, org, font, fontScale, color, thickness)

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()