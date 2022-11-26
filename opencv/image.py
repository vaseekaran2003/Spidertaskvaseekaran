import cv2 as cv
img=cv.imread("Capture.PNG",1)
new_frame=cv.cvtColor(img,cv.COLOR_BAYER_BG2GRAY)

cv.imshow("image",new_frame)
key=cv.waitKey(0)

if key ==27:
    cv.destroyAllWindows()
elif key ==(ord("s")):
    cv.imwrite("some.PNG",img)
    cv.destroyAllWindows()
    


