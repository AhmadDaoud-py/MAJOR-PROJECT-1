import cv2
import os

#live camera object
video=cv2.VideoCapture(0)

#Object Detection Algorithm used to identify faces in an image or a real time video
facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count=0

perID=str(input("Enter Your Name: ")).lower()

path='images/'+perID

isExist = os.path.exists(path)

if isExist:
	print("Name Already Taken")
	perID=str(input("Enter Your Name Again: "))
else:
	os.makedirs(path)

while True:
	ret,frame=video.read()
	faces=facedetect.detectMultiScale(frame,1.3, 5)
	for x,y,w,h in faces:
		count=count+1
		name='./images/'+perID+'/'+ str(count) + '.jpg'
		print("Storing Image.........", name)
		cv2.imwrite(name, frame[y:y+h,x:x+w])
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
	cv2.imshow("WindowFrame", frame)
	# if cv2.waitKey(20) & 0xFF ==ord('d'):
    #      break
	cv2.waitKey(1)
	if count>500:
		break
video.release()
cv2.destroyAllWindows()