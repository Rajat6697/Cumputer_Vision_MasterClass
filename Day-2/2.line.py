import cv2

window_name= "Image"
path= "img/img.jpg"

image= cv2.imread(path)

# Start point and end point for the line
start_point= (10, 20)

# End point
end_point= (50, 80)

color= (0, 255, 0) # blue line(RGB format)
thickness= 9

image= cv2.line(image, start_point, end_point, color, thickness)

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()