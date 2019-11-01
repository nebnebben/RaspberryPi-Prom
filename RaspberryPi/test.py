from constants import *
from bmultfunction import *
from bdetectfunction import *
from tkinter import *
from PIL import Image, ImageTk

camroach = 0
microach = 0
automatic = False
PWMLightOn = True
servoMotorOn = True

root = Tk()

def sys(event):
   global automatic
   if automatic == True:
       automatic = False
       sys_label.config(text="Manual")
   else:
       automatic = True
       sys_label.config(text="Automatic")


def PWM(event):
   global PWMLightOn
   if PWMLightOn == True:
       PWMLightOn = False
       PWM_label.config(text="Off")
   else:
       PWMLightOn = True
       PWM_label.config(text="On")


def Servo(event):
   global servoMotorOn
   if servoMotorOn == True:
       servoMotorOn = False
       Servo_label.config(text="Off")
   else:
       servoMotorOn = True
       Servo_label.config(text="On")

def takepic(event):
	if bugdetectmult == False:
		global camroach
		camroach, picarray = bdetect(camroach)
		img = PIL.Image.fromarray(picarray)
		tkimage = ImageTk.PhotoImage(img)
		global tkimage
		tklabel = Label(root, image = tkimage)
		global tklabel
		tklabel.grid(row=3,column=0,columnspan=5)
		cam_label.config(text=camroach)
	else:
		global camroach
		camroach, picarray = mdetect(camroach)
		img = PIL.Image.fromarray(picarray)
		tkimage = ImageTk.PhotoImage(img)
		global tkimage
		tklabel = Label(root, image = tkimage)
		global tklabel
		tklabel.grid(row=3,column=0,columnspan=5)
		cam_label.config(text=camroach)
		

def start(event):
	print("Start")	

sys_button = Button(root, text="System State")
sys_button.bind("<Button-1>", sys)
# sys_button.pack()

PWM_button = Button(root, text="PWM Light")
PWM_button.bind("<Button-1>", PWM)
# PWM_button.pack()

Servo_button = Button(root, text="Servo Motor")
Servo_button.bind("<Button-1>", Servo)
# Servo_button.pack()

takepic_button = Button(root, text="Take Picture")
takepic_button.bind("<Button-1>", takepic)

start_button = Button(root, text="Automatic Start")
start_button.bind("<Button-1>", start)

if automatic == True:
   sys_label = Label(root, text="Automatic")
else:
   sys_label = Label(root, text="Manual")

if PWMLightOn == True:
   PWM_label = Label(root, text="On")
else:
   PWM_label = Label(root, text="Off")

if servoMotorOn == True:
   Servo_label = Label(root, text="On")
else:
   Servo_label = Label(root, text="Off")

camheading_label = Label(root, text = "No. of Roaches w. mic")
micheading_label = Label(root, text = "No. of Roaches w. cam")


cam_label = Label(root, text=camroach)
mic_label = Label(root, text=microach)


camheading_label.grid(row=0,column=3)
micheading_label.grid(row=0,column=4)

cam_label.grid(row=1, column=4)
mic_label.grid(row=1, column=3)


sys_button.grid(row=0, column=0)
sys_label.grid(row=1, column=0)

PWM_button.grid(row=0, column=1)
PWM_label.grid(row=1, column=1)

Servo_button.grid(row=0, column=2)
Servo_label.grid(row=1, column=2)

takepic_button.grid(row=0,column=6)

start_button.grid(row=0,column=7)


root.mainloop()

if bugdetectmult == True:
	mdetect()
else:
	bdetect()


