from tkinter import *

s1=0
#################### defining window ###################
my_window = Tk()
t1= Frame(my_window)
t2= Frame(my_window)

my_window.title("#DNY slider app")
##my_window.geometry("1020x780")

#################### commands ###################
def b0c():
    s1=sl1.get()
    print(sl1.get())
    val_2['text']= s1
    s11=str(s1)
#    print(type(s11)) # for debugging
    f = open('record.txt','a')
    f.write("\n"+s11)
    f.close()
    
    
 

################# defining wedgets ####################
head_1 = Label(t1,
                bd=4 ,
                relief="solid",
                font="time 18 bold",
                bg="red",
                fg="white",
                text="slider app #DNY")
val_2 = Label(t2,
                bd=0 ,
                relief="solid",
                font="time 22 bold",
                bg="white",
                fg="black",
                text= s1)

sl1= Scale(t2,orient='horizontal',from_=0,to= 180)
sl1.set(90)
b0= Button(t2,text="get data",command= b0c)
sl1.pack()

################# position ##########################
head_1.grid(row=0, column=0)
val_2.grid(row=0, column=1)
b0.grid(row=1, column=1)
sl1.grid(row=0, column=0)

################# position frame ##########################
t1.grid(row=0,column=0)
t2.grid(row=1,column=0)

my_window.mainloop()
