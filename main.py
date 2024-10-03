import cv2
from matplotlib import pyplot as pl
import imutils

face_recognizer = cv2.CascadeClassifier("face.xml")
img = cv2.imread("images/download.jpg")
img = cv2.resize(img, (1280, 920))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = face_recognizer.detectMultiScale(gray, 3, 1)


areas = []
numb_of_face = 0
for (x, y, w, h) in face:
    areas.append(w*h)
areas_1 = sorted(areas)
for i in range (0, len(areas)):
    if(areas[i] == areas_1[-1]):
        max_face = i


img = cv2.rectangle(img, (face[max_face][0], face[max_face][1]), (face[max_face][0] + face[max_face][2], face[max_face][1] + face[max_face][3]), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)