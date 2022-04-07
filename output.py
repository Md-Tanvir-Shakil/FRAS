from tkinter import *
from PIL import ImageTk, Image
import Recognize

# Create an instance of Tkinter Frame
win = Tk()
win.title("NITER")

# Set the geometry of Tkinter Frame
win.geometry("780x450")

bg = PhotoImage(file = "GUI.png")
  
# Create Canvas
canvas1 = Canvas( win, width = 780,
                 height = 450)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
#Define the working of the button
def my_command():
    Recognize.recognize_attendence()
click_btn = PhotoImage(file = 'NITER.png')

#Let us create a label for button event
img_label = Label(image = click_btn)

#Let us create a dummy button and pass the image
button = Button(win, image = click_btn, command = my_command,
   borderwidth = 0)
button.pack(pady = 30)

button_canvas = canvas1.create_window( 260, 100, 
                                       anchor = "nw",
                                       window = button)


win.mainloop()