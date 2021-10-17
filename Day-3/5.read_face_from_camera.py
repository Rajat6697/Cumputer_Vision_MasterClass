from imutils.video import VideoStream
import argparse
import imutils
import time
import os
import cv2
#Construct the arguement parser and parse the arguements
ap= argparse.ArgumentParser()
ap.add_argument("-c", "--cascades", type=str, default="cascades", help= "Path to input directory containing haar cascades")
args= vars(ap.parse_args())

#initialize a dictionary that maps the name of the haar cascades
#their filenames
detectorPaths= {
    "face": "haarcascade_frontalface_default.xml",
    "eyes": "haarcascade_eye.xml",
    "smile": "haarcascade_smile.xml",
}


# Initialize a dictionary to store our haar cascade detectors
print("[Info] loading haar cascades")
detectors= {}

#Loop Over our detector paths
for (name, path) in detectorPaths.items():
    path= os.path.sep.join([args["cascades"], path])
    detectors[name]= cv2.CascadeClassifier(path)

#Initialize the video stream and allow the camera sensor
print("[Info] strting the camera")
vs= VideoStream(src=0).start()
time.sleep(2.0)

# Loop over the frames from the video stream
while True:
    frame= vs.read()
    frame= imutils.resize(frame, width=500)
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Perform face detection
    faceReacts= detectors["face"].detectMultiScale(gray, scaleFactor= 1.05, minNeighbors= 5, minSize= (15, 15), flags= cv2.CASCADE_SCALE_IMAGE)
    #Loop over the face bounding boxes
    for (fX, fY, fW, fH) in faceReacts:
        #Extract the face ROI
        faceROI= gray[fY:fY+fH, fX:fX+fW]
        #apply eye detection to the face ROI
        eyeReacts= detectors["eyes"].detectMultiScale(faceROI, scaleFactor= 1.1, minNeighbors= 5, minsize= (15, 15), flags= cv2.CASCADE_SCALE_IMAGE)
        # apply smile detection to the face ROI
        smileReacts= detectors["smile"].detectMultiScale(faceROI, scaleFactor= 1.1, minNeighbors= 5, minsize= (15, 15))
        for (eX, eY, eW, eH) in eyeReacts:
            ptA= (fX + eX, fY + eY)
            ptB= (fX + eX + eW, fY + eY + eH)
            cv2.rectangle(frame, ptA, ptB, (0, 0, 255), 10 )
        cv2.rectangle(frame, (fX, fY), (fX+fW, fY+fH), (0, 0, 255), 2 )
    
    cv2.imshow("Frame", frame)
    key= cv2.waitKey(1) & 0xFF
    #if the q key was pressed , break from the loop
    if key== ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()







