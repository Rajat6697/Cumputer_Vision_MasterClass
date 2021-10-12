import cv2


path= "img/img.jpg"
image= cv2.imread(path)
cv2.waitKey(0)

gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny Edges
edged= cv2.Canny(gray, 30, 150)
cv2.waitKey(0)

contours, hierarchy= cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.waitKey()

print("Number of Contours found = " + str(len(contours)))

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()