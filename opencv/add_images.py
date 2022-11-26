import cv2 as cv
img1=cv.imread("Capture.PNG",1)
img2=cv.imread("Default.jpg",1)
img2=cv.resize(img2,(512,512))
img1=cv.resize(img1,(512,512))

final_img=cv.add(img1,img2)

cv.imshow("image",final_img)
key=cv.waitKey(0)
if key==ord("q"):
    cv.destroyAllWindows()
