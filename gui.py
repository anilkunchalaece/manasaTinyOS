from Tkinter import *
#from ttk import *
import serial

ser = serial.Serial('/dev/ttyACM0',9600)

def updateVal():
	scaleValue.set(float(ser.readline()))
	root.after(10,updateVal)

def ledOn():
	ser.write('A')
	
def ledOff():
	ser.write('B')

def startLeds():
	ser.write('C')

def stopLeds():
	ser.write('D')
def changeLeds():
	ser.write('E')
def skipLeds():
	ser.write('F')
	
root = Tk()
root.title("Gui Demo By Kunchala Anil")
root["bg"] = "green"
root.geometry("600x400+300+300")

frameButton = Frame(root, width=300, height=300,bg="green")
frameScale = Frame(root,width = 300,height=300,bg="green")
frameLeds = Frame(root,width = 300,height=300,bg="green")
frameMyName = Frame(root,width = 300,height=300,bg="yellow")

buttonLedOn = Button(frameButton, text="LED ON!",bg="yellow",command = ledOn)
buttonLedOff = Button(frameButton,text="LED OFF!",bg="yellow",command = ledOff)
buttonLabel = Label(frameButton,text="Controls for On and Off the LED connected to 13")

scaleValue = Scale(frameScale,from_=0, to=1024,orient=HORIZONTAL,bg="yellow",length = 300,resolution=10)
scaleLabel = Label(frameScale,text="Analog Input From A0")
scaleValue.set(100)


buttonStartLeds = Button(frameLeds, text="Start Led's!",bg="yellow",command = startLeds)
buttonStopLeds = Button(frameLeds,text="Stop Led's!",bg="yellow",command = stopLeds)

buttonChangeLeds = Button(frameLeds, text="Change Led's!",bg="yellow",command = changeLeds)
buttonSkipLeds = Button(frameLeds,text="Skip Led's!",bg="yellow",command = skipLeds)
ledLabel = Label(frameLeds,text="LED's Connected to 4,5,6 Pins")


myLabel = Label(frameMyName,text="Contact me :: anilkunchalaece@gmail.com",bg="red")

buttonLabel.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
buttonLedOn.pack(side=RIGHT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
buttonLedOff.pack(side=RIGHT,ipadx = 5,ipady = 5, padx = 5,pady = 5)

scaleValue.pack(side=RIGHT,ipadx = 2,ipady = 2, padx = 2,pady = 2)
scaleLabel.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)

ledLabel.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
buttonStartLeds.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
buttonStopLeds.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
buttonChangeLeds.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
buttonSkipLeds.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)



myLabel.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)

frameButton.pack(ipadx = 15,ipady = 15, padx = 15,pady = 15)
frameScale.pack(ipadx = 15,ipady = 15, padx = 15,pady = 15)
frameLeds.pack(ipadx = 15,ipady = 15, padx = 15,pady = 15)
frameMyName.pack(ipadx = 5,ipady = 5, padx = 5,pady = 5)

#updateVal()
root.mainloop()