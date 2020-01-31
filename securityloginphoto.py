import cv2
import os
cap=cv2.VideoCapture(0)
ret ,photo=cap.read()
cv2.imwrite("/root/Desktop/alert.png",photo)
cap.release()
os.system("ansible-playbook /root/Desktop/ans")
