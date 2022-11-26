import cv2 as cv
image=cv.imread("Capture.PNG",-1)

#for colour use bgr scale,
image=cv.line(image,(0,0),(255,255),(255,0,0),5) 
#use -1 in thickness to fill the rectangle
'''image_with_rectangle=cv.rectangle(image,(0,0),(255,255),(0,255,0),-1)
image_with_circle=cv.circle(image,(255,255),100,(255,0,0),-1)'''
image=cv.putText(image,"hi",(0,255),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),4,cv.LINE_AA)



cv.imshow("imagge",image)
key=cv.waitKey(0)
if key==ord("q"):
    cv.destroyAllWindows()