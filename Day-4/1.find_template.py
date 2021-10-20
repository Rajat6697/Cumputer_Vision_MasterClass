# Import the necessary modules
import argparse
import cv2

# Construct the arguement parser and  parse the arguements
ap= argparse.ArgumentParser()
ap.add_argument("-i","--image", type= str, required=True, help= "path to input image where we'll apply template matching")
ap.add_argument("-t", "--template", type= str, required=True, help="path to template image")
args= vars(ap.parse_args())

#load the input image and template image from disk, then display them on our screen
print("[info] loading screen")
path_image= "img/img.jpg"
path_template= "img/template.jpg"
image= cv2.imread(args["image"])
template= cv2.imread(args["template"])
cv2.imshow("Image", image)
cv2.imshow("Template", template)

#Convert both the image and template to grayscale
imageGray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray= cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#Perform template matching
print("[info] performing template matching")
result= cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVAL, maxVAL, minLOC, maxLOC)= cv2.minMaxLoc(result)

#Determine the starting and ending point of the bounding box
(startX, startY)= maxLOC
endX= startX + template.shape[1]
endY= startY + template.shape[0]
#draw the bounding box on the image
cv2.rectangle(image, (startX, startY), (endX, endY), (255,0, 0), 3)

#Show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)