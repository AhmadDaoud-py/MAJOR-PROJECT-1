import cv2
img = cv2.imread('pic.jpg')
facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

ret,frame=img
faces=facedetect.detectMultiScale(frame,1.3, 5)
for x,y,w,h in faces:
	cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
	cv2.imshow("WindowFrame", frame)
    # if cv2.waitKey(20) & 0xFF ==ord('d'):
    #     break
img.release()
cv2.destroyAllWindows()