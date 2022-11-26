import cv2 as cv
import numpy as np
events = [i for i in dir(cv) if "EVENT" in i]
#print(events) #all events in cv2 library
# to execute something when mouse click event takes place
def click_event(event,a,b,flags,param): #whenever a mouse click happens the five arguments are stored in the mouse click event
    if event==cv.EVENT_LBUTTONDOWN:
        #Here whenever a click is made at a certain x,y then those coordinates are displayed at that x,y
        #for blue green and red channels
        blue=img[a,b,0]
        green=img[a,b,1]
        red=img[a,b,2]
        print(a,",",b)
        my_text=str(a) + "," + str(b)
        cv.putText(img,my_text,(a,b),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,cv.LINE_AA)
        cv.imshow("image",img)

img=np.zeros((512,512,3),np.uint8) # creating a image using numpy method
cv.imshow("image",img)
cv.setMouseCallback("image",click_event)
key=cv.waitKey(0)
if key==ord("q"):
    cv.destroyAllWindows()
    



