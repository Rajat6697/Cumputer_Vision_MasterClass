import cv2
import matplotlib.pyplot  as plt

img= cv2.imread("baby.jpg")

face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade= cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade= cv2.CascadeClassifier("haarcascade_smile.xml")

# Create a function to detect face
def adjusted_detect_face(img):
    face_img= img.copy()
    face_rect= face_cascade.detectMultiScale(face_img, scaleFactor= 1.2, minNeighbors= 5)
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y), (x+w, y+h), (255, 255, 255), 10)
    return face_img 



# Detecting the face
face= adjusted_detect_face(img)
plt.imshow(face)
# Saving the image
window_name= "Face"
cv2.imwrite('baby_face.jpg', face)
cv2.imshow(window_name, face)


# Create a function to detect eyes
def detect_eyes(img):
    eye_img= img.copy()
    eye_rect= eye_cascade.detectMultiScale(eye_img, scaleFactor= 1.2, minNeighbors= 5)
    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y), (x+w, y+h), (255, 255, 255), 10)
    return eye_img

# Detecting eyes
eyes= detect_eyes(img)
plt.imshow(eyes)
window_name_eyes= "Eyes Image"
cv2.imwrite("baby_eyes.jpg", eyes)
cv2.imshow(window_name_eyes, eyes)


eyes_face= adjusted_detect_face(img)
eyes_face= detect_eyes(eyes_face)
plt.show(eyes_face)
window_name= "Face+eyes.jpg"
cv2.imwrite("face+eyes.jpg", eyes_face)
cv2.imshow(window_name, eyes_face)