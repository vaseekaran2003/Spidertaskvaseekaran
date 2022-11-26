import numpy as np
import cv2 as cv
import datetime
cap = cv.VideoCapture(0)
'''cap.set(cv.CAP_PROP_FRAME_WIDTH,300)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,300)'''


print(cap.get(cv.CAP_PROP_FRAME_WIDTH),cap.get(cv.CAP_PROP_FRAME_HEIGHT))


'''Better store every variable in every cv functions,use cap.get(cv.cap_prop_width) for getting the width of the frame
use cap.set(cv.cap_prop_width,new_size_u_want_to_provide)
cap.get() for properties of the video capture
cap.set() is for modifying
cap.get() returns the properties in integer format
for eg if we need to print the width of the frame in the top left corner of the frame,then use string=str(cap.get()) then pass the string to 
the cv.puttext() fucntion
text= "width:" + str(cap.get())

for displaying date and time import datetime module


'''




if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.get(cv.CAP_PROP_FRAME_WIDTH)
    text="width :"+ str(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) + "height:"+ str(cap.get(cv.CAP_PROP_FRAME_WIDTH))

    date_and_time=str(datetime.datetime.now())

    frame=cv.putText(frame,text,(0,255),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),3,cv.LINE_AA)
    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    

    # Display the resulting frame
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()