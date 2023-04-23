from tkinter import *
from  tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import cv2

window = Tk()

window.title("NIO Internship")
window.config(bg='#e1f1f7')
window.geometry("1280x720")

logo_img = ImageTk.PhotoImage(Image.open("nio.png"))
logo_label = Label(image=logo_img)
logo_label.grid(row=0, column=0, columnspan=3)

in_img = ''
### defining src img button
def src_img():
    info.delete(0, END)
    global in_img
    filepath = filedialog.askopenfilename()
    in_img = cv2.imread(''+filepath)
    in_imgre = cv2.resize(in_img, (0,0), fx=0.5, fy=0.5)
    cv2.imshow('Src Image', in_imgre)
    info.insert(0, "Image Loaded Successfully")
    #messagebox.showinfo("Success","Done :)")

### defining output button
def output_img():
    info.delete(0, END)
    #in_img = cv2.imread('3.jpg')
    g_blur = cv2.GaussianBlur(in_img, (9,9), 0)
    intensity1 = cv2.addWeighted(in_img,1.5, g_blur, -0.5, -10)
    intensity2 = cv2.addWeighted(in_img,2.5, g_blur, -1.5, -20)
    intensity3 = cv2.addWeighted(in_img,3.5, g_blur, -2.5, -30)
    # img_re3 = cv2.resize(intensity3, (0,0), fx=0.9, fy=0.9)
    # img_re2 = cv2.resize(intensity2, (0,0), fx=0.9, fy=0.9)
    # img_re1 = cv2.resize(intensity1, (0,0), fx=0.9, fy=0.9)
    # img_re0 = cv2.resize(in_img, (0,0), fx=0.9, fy=0.9)
    # cv2.imshow('Intensity Level 2', img_re3)
    # cv2.imshow('Intensity Level 3', img_re2)
    # cv2.imshow('Intensity Level 1', img_re1)
    # cv2.imshow('original', img_re0)
    cv2.imwrite('intensity1.jpg', intensity1)
    cv2.imwrite('intensity2.jpg', intensity2)
    cv2.imwrite('intensity3.jpg', intensity3)
    cv2.imwrite('blur.jpg',g_blur)
    cv2.waitKey(0)
    info.insert(0, "Image Saved Successfully")
    messagebox.showinfo("Success","Done :)")

### create text boxes
info = Entry(window, width=30)
info.place(x=500, y=200, width=400, height=50)
### creating output buttons
output_img_button = Button(window, text="Save Output", command=output_img)
output_img_button.place(x=800, y=300, width=100, height=50)
### button for selecting src img
src_img_button = Button(window, text="Select Image", command=src_img)
src_img_button.place(x=500, y=300, width=100, height=50)


window.mainloop()



###
## Make it so there are check boxes for the following:
# Save the images upscale & save
# Do noise reduction
# Do Contour detection maybe
# Do edge detection maybe