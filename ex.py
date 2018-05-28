from Tkinter import *
from tkMessageBox import *
#from ttk import *
import serial



def updateVal():
	#scaleValue.set(float(ser.readline()))
	#tempValue.set()
	#humiValue.set()
	#lightValue.set()
	#root.after(10,updateVal)

def connectToBaseStation():
	try:
		ser = serial.Serial(usbEntry.get(),baudRateEntry.get())
		liveStreamValue.set("connecion established sucessfully ")
	except:
		showwarning("Unable to Connect", "Check USB and Baud rate or else Reconnect Base Station")
	
def startLeds():
	ser.write('C')

def stopLeds():
	ser.write('D')
def changeLeds():
	ser.write('E')
def skipLeds():
	ser.write('F')




root = Tk()
root.title("XM1000 - Alice Bob Relay")
root["bg"] = "green"
root.geometry("600x600+300+300")

#variable for live stream
liveStreamValue = StringVar()
liveStreamValueOld2 = StringVar()
liveStreamValueOld1 = StringVar()



frameBaudRate = Frame(root,width=300,height=300,bg="green")
frameSettings = Frame(root, width=300, height=300,bg="green")
frameTempValue = Frame(root,width = 300,height=200,bg="green")
frameLightValue = Frame(root,width = 300,height=200,bg="green")
frameHumiValue = Frame(root,width = 300,height=200,bg="green")
frameStream = Frame(root,width = 300,height=300,bg="green")
frameMyName = Frame(root,width = 300,height=300,bg="yellow")

buttonConnect = Button(frameSettings, text="Connect !",bg="yellow",command = connectToBaseStation)
buttonDisconnect = Button(frameSettings,text="Disconnect !",bg="red",command = disconnectToBaseStation)

usbEntryLabel = Label(frameBaudRate,text="USB")
usbEntry = Entry(frameBaudRate)

baudRateEntryLabel = Label(frameBaudRate,text="Baud Rate")
baudRateEntry = Entry(frameBaudRate)

buttonLabel = Label(frameSettings,text="Enter USB and BaudRate and Click Connect")



tempValue = Scale(frameTempValue,from_=0, to=1024,orient=HORIZONTAL,bg="yellow",length = 300,resolution=10)
tempLabel = Label(frameTempValue,text="Temperature    ")
tempValue.set(100)

lightValue = Scale(frameLightValue,from_=0, to=1024,orient=HORIZONTAL,bg="yellow",length = 300,resolution=10)
lightLabel = Label(frameLightValue,text="Light Intensity")
lightValue.set(100)

humiValue = Scale(frameHumiValue,from_=0, to=1024,orient=HORIZONTAL,bg="yellow",length = 300,resolution=10)
humiLabel = Label(frameHumiValue,text="Humidity       ")
humiValue.set(100)


liveStreamLabel = Label(frameStream,textvariable=liveStreamValue,height=1,width=600)
liveStreamOld1Label = Label(frameStream,textvariable=liveStreamValueOld1,height=1,width=600)
liveStreamOld2Label = Label(frameStream,textvariable=liveStreamValueOld2,height=1,width=600)


infoLabel = Label(frameMyName,text="yada yada yada .......",height=6,width=600,bg="white");

usbEntryLabel.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
usbEntry.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
baudRateEntryLabel.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
baudRateEntry.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)


buttonLabel.pack(side=LEFT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
#buttonDisconnect.pack(side=RIGHT,ipadx = 5,ipady = 5, padx = 5,pady = 5)
buttonConnect.pack(side=RIGHT,ipadx = 5,ipady = 5, padx = 5,pady = 5)

tempLabel.pack(side=LEFT,ipadx=5,ipady=5,padx=5,pady=5)
tempValue.pack(side=RIGHT,ipadx=5,ipady=5,padx=5,pady=5)

lightLabel.pack(side=LEFT,ipadx=5,ipady=5,padx=5,pady=5)
lightValue.pack(side=RIGHT,ipadx=5,ipady=5,padx=5,pady=5)

humiLabel.pack(side=LEFT,ipadx=5,ipady=5,padx=5,pady=5)
humiValue.pack(side=RIGHT,ipadx=5,ipady=5,padx=5,pady=5)


liveStreamOld2Label.pack(side=TOP)
liveStreamOld1Label.pack(side=TOP)
liveStreamLabel.pack(side=TOP)

infoLabel.pack(side=LEFT,ipadx=5,ipady=5,padx=5,pady=5)
frameBaudRate.pack(ipadx = 15,ipady = 15, padx = 15,pady = 15)
frameSettings.pack(ipadx = 15,ipady = 15, padx = 15,pady = 15)

frameTempValue.pack(ipadx = 5,ipady= 5,padx=5,pady=5)
frameLightValue.pack(ipadx = 5,ipady= 5,padx=5,pady=5)
frameHumiValue.pack(ipadx = 5,ipady= 5,padx=5,pady=5)

frameStream.pack(ipadx = 15,ipady= 15,padx=15,pady=15)
frameMyName.pack(ipadx = 15,ipady= 15,padx=15,pady=15)

usbEntry.insert(0,"/dev/ttyUSB0")
baudRateEntry.insert(0,"115200")
#updateVal()
root.mainloop()