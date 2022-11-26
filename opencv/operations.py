import cv2 as cv
def callback(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        coordinate=str(x)+","+str(y)
        print(x,y)
        cv.putText(img,coordinate,(x,y),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),1,cv.LINE_AA)
        cv.imshow("imgae",img)
img=cv.imread("Capture.PNG",1)
img2=cv.imread("Default.jpg",1)

print(img.shape)# no of rows coloumns and channels
print(img.size)# total pixels
print(img.dtype)# data type
region_of_interest=img[231:327 , 377:487]   #copy ur region of interest into a variable and change the area and equal it to the same variable
#img[66:37,184:163]=region_of_interest

b,g,r=cv.split(img)
img=cv.merge((b,g,r))
img_new=cv.add(img,img2)


cv.imshow("imgae",img)
cv.setMouseCallback("imgae",callback)
k=cv.waitKey(0)
if k==ord("q"): 
    cv.destroyAllWindows()