from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    #here we will get the server
    sp.get_servers()
    #here we will get speed bit per second but by dividing in 10 ** 8 we will get speed in MBPS
    # we are converting it into string format
    down = str(round(sp.download()/(10**8),3)) + "Mbps"
    up = str(round(sp.upload()/(10**8),3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)






#this is all related to grpahics
#calling tkinter class
sp = Tk()
#title
sp.title("Internet Speed Test")
#geometry of window
sp.geometry("500x650")
#background color
sp.config(bg="#6cfaec")

lab = Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="#02e0ca",fg="black")
#position of lab
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp,text="Download Speed",font=("Time New Roman",30,"bold"))
#position of lab
lab.place(x=60,y=130,height=50,width=380)

lab_down = Label(sp,text="00",font=("Time New Roman",30,"bold"))
#position of lab
lab_down.place(x=60,y=200,height=50,width=380)

lab = Label(sp,text="Upload Speed",font=("Time New Roman",30,"bold"))
#position of lab
lab.place(x=60,y=290,height=50,width=380)

lab_up = Label(sp,text="00",font=("Time New Roman",30,"bold"))
#position of lab
lab_up.place(x=60,y=360,height=50,width=380)

#creating button #relief used to make button like 3d
button = Button(sp,text="Check Speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="white",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

#This will show us window
sp.mainloop()

