#1.
from tkinter import  *
root=Tk()

root.mainloop()
#2. Implementation of Size of GUI window
from tkinter import *
root = Tk()
root.geometry("400x200")#Width 400 and height 200; format should be ("width x height")
root.mainloop()
#2a. Restrict the size of GUI window using maxsize() and minsize()
from tkinter import *
root =Tk()
root.geometry("400x200")#It's the base size
root.minsize(100,50)#It sets the minimum size of the window; format(width,height)
root.maxsize(800,600)#It sets the maximum size of the window; format(width,height)
root.mainloop()
#3 Implementation of Label
from tkinter import *
root=Tk()
root.geometry("600x500")
root.minsize(300,200)
root.maxsize(800,700)
add_text=Label(text="My Name is Abisekh")
add_text.pack()#Packing The Data to Display it on The Window otherwise it will not be printed on the window
root.mainloop()
#4. Implementation of image in the GUI window
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("2560x1440")
image=Image.open(r"C:\Users\abise\OneDrive\Pictures\R.jpg")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo)
photo_label.pack()
root.mainloop()
#4a. Implementation of image in the GUI window
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("1200x900")
text=Label(text="Image Gallery")
text.pack()
image1=Image.open(r"C:\Users\abise\OneDrive\Pictures\R.jpg")
photo1=ImageTk.PhotoImage(image1)
photo_label1=Label(image=photo1)
photo_label1.pack()
image2=Image.open(r"C:\Users\abise\OneDrive\Pictures\block diagram.jpg")
photo2=ImageTk.PhotoImage(image2)
photo_label2=Label(image=photo2)
photo_label2.pack()
image3=Image.open(r"C:\Users\abise\OneDrive\Pictures\equivalent_flow_graph.jpg")
photo3=ImageTk.PhotoImage(image3)
photo_label3=Label(image=photo3)
photo_label3.pack()
root.mainloop()
#5. Implementation of Label in the GUI window
from tkinter import *
root=Tk()
root.title("It's A GUI Window")
root.mainloop()
#6. Implementauion Of Different Operations of Label
from tkinter import *
root=Tk()
root.geometry("800x400")
root.title("GUI Window")
text=Label(text='''
        The robot's hardware architecture involves the integration of sensors, actuators, 
        \nand a custom microcontroller circuit. In lieu of Arduino, 
        \na different microcontroller is employed to control the robot's movements and decision-making processes. 
        \nThe chosen microcontroller is selected based on its computational capabilities, input/output options, and power efficiency.
        \nSensors, such as ultrasonic or infrared distance sensors, are strategically placed on the robot to detect obstacles in its path. 
        \nThese sensors provide real-time data to the microcontroller, enabling the robot to make decisions about its movements. 
        \nThe decision-making algorithm is designed to analyse sensor data and determine the appropriate actions for obstacle avoidance.
        \nActuators, such as motors or servos, are used to drive the wheels or control other locomotion mechanisms. 
        \nThe microcontroller regulates the actuator outputs based on the obstacle detection algorithm, 
        \nensuring that the robot manoeuvres around obstacles effectively.
        ''',bg="light blue",fg="brown",font="arial 10 bold",padx=100,pady=30,borderwidth=10,relief=SUNKEN)
text.pack(side=TOP,anchor="center",fill=X,padx=100,pady=140)
root.mainloop()
#7.
from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("GUI Window")
text=Label(text="READY",fg="white",background="dark blue",font=("Agency FB",12,"bold"))
text.pack(side=BOTTOM,fill=X)
root.mainloop()
#8a.
from tkinter import *
root=Tk()
root.geometry("800x600")
l=Label(text="Abisekh")
l.pack(side=LEFT)
l=Label(text="Abisekh")
l.pack(side=LEFT)

root.mainloop()
#8b.
from tkinter import *
root=Tk()
root.geometry("800x600")
l=Label(text="Abisekh")
l.pack(anchor="w")
l1=Label(text="Abisekh")
l1.pack(anchor="w")
root.mainloop()
#8c.
from tkinter import *
root=Tk()
root.geometry("800x600")
l=Label(text="Abisekh")
l.pack(side=LEFT,anchor="w")
l1=Label(text="Abisekh")
l1.pack(side=LEFT,anchor="w")
root.mainloop()

#9. Implementation of Frame in GUI Window
from tkinter import *
root=Tk()
root.geometry("800x600")
f1=Frame(root,bg="black",borderwidth=2)
f1.pack(side=LEFT)
text=Label(f1,text="Frame",bg="blue",fg="white")
text.pack()
root.mainloop()
#9a.
from tkinter import *
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="dark blue",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
text=Label(f1,text="Side bar",bg="orange",font="arial 12 bold",fg="dark blue",padx=10,pady=10)
text.pack()
f2=Frame(root,borderwidth=2,bg="dark blue",padx=10,pady=10,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
text2=Label(f2,text="Welcome to The GUI Window",bg="orange",font="arial 12 bold",fg="dark blue",padx=10,pady=10)
text2.pack()
root.mainloop()
#10. Implementation of Buttons in Gui
from tkinter import *
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="white",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
button=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white")
button.pack()
root.mainloop()
#10a.
from tkinter import *
def button():
        print("It's A Button")
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="white",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
button=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=button)
button.pack()
root.mainloop()
from tkinter import *
import Atm
root=Tk()
root.geometry("800x600")
f1=Frame(root,borderwidth=2,bg="white",padx=10,pady=10,relief=SUNKEN)
f1.pack(side=TOP,fill=X)
button=Button(f1,text="Click Here",font="arial 12 bold",padx=10,pady=10,bg="blue",fg="white",command=Atm.ATM)
button.pack()
root.mainloop()
