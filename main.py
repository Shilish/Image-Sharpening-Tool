import cv2

#Reading the image
in_img = cv2.imread('original.jpg')

#Gauusian blur for image subtraction
g_blur = cv2.GaussianBlur(in_img, (9,9), 0)

#Using addweighted()
intensity1 = cv2.addWeighted(in_img,1.5, g_blur, -0.5, -10)
intensity2 = cv2.addWeighted(in_img,2.5, g_blur, -1.5, -20)
intensity3 = cv2.addWeighted(in_img,3.5, g_blur, -2.5, -30)

#Resizing the images
img_re3 = cv2.resize(intensity3, (0,0), fx=0.9, fy=0.9)
img_re2 = cv2.resize(intensity2, (0,0), fx=0.9, fy=0.9)
img_re1 = cv2.resize(intensity1, (0,0), fx=0.9, fy=0.9)
img_re0 = cv2.resize(in_img, (0,0), fx=0.9, fy=0.9)

#Outputting the images
cv2.imshow('Intensity Level 2', img_re3)
cv2.imshow('Intensity Level 3', img_re2)
cv2.imshow('Intensity Level 1', img_re1)
cv2.imshow('original', img_re0)

#Saving the images
cv2.imwrite('intensity1.jpg', intensity1)
cv2.imwrite('intensity2.jpg', intensity2)
cv2.imwrite('intensity3.jpg', intensity3)

cv2.waitKey(0)