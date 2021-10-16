import cv2

cap= cv2.VideoCapture('video.mp4')

if(cap.isOpened()==False):
    print("Error opening video.")

while(cap.isOpened()):
    ret, frame= cap.read()

    if ret== True:
        frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale Video',frame)
        
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()