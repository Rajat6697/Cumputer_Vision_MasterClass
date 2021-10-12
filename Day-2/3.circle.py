import cv2

path= "img/img.jpg"
image= cv2.imread(path)
window_name= "Image"

center_coordinates= (120, 50)
radius= 10

color= (0, 255, 0)
thickness= 2
image= cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()