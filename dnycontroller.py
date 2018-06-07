from tkinter import *

val1=0
val2=0
do = 0

#################### defining window ###################
my_window = Tk()
t1= Frame(my_window)
t2= Frame(my_window)
t3= Frame(my_window)


my_window.title("#DNY calculater")

##my_window.geometry("1020x780")


#################### commands ###################
def b0c():
    val1=val_2['text']
    val1=(val1 * 10 )+0
    val_2['text']= val1
def b1c():
    val1=val_2['text']
    val1=(val1 * 10 )+1
    val_2['text']= val1
def b2c():
    val1=val_2['text']
    val1=(val1 * 10 )+2
    val_2['text']= val1
def b3c():
    val1=val_2['text']
    val1=(val1 * 10 )+3
    val_2['text']= val1
def b4c():
    val1=val_2['text']
    val1=(val1 * 10 )+4
    val_2['text']= val1
def b5c():
    val1=val_2['text']
    val1=(val1 * 10 )+5
    val_2['text']= val1
def b6c():
    val1=val_2['text']
    val1=(val1 * 10 )+6
    val_2['text']= val1
def b7c():
    val1=val_2['text']
    val1=(val1 * 10 )+7
    val_2['text']= val1
def b8c():
    val1=val_2['text']
    val1=(val1 * 10 )+8
    val_2['text']= val1
def b9c():
    val1=val_2['text']
    val1=(val1 * 10 )+9
    val_2['text']= val1
def badd():
    val1=val_2['text']
    do=val_0['text']
    val2=val_1['text']
    val2=val1
    val1=0
    do= "1"
    val_2['text']= val1
    val_1['text']= val2
    val_0['text']= do
def bsub():
    val1=val_2['text']
    val2=val_1['text']
    do=val_0['text']
    val2=val1
    val1=0
    do= "2"
    val_2['text']= val1
    val_1['text']= val2
    val_0['text']= do
def bdev():
    val1=val_2['text']
    val2=val_1['text']
    do=val_0['text']
    val2=val1
    val1=0
    do= "3"
    val_2['text']= val1
    val_1['text']= val2
    val_0['text']= do
def bmul():
    val1=val_2['text']
    val2=val_1['text']
    do=val_0['text']
    val2=val1
    val1=0
    do= "4"
    val_2['text']= val1
    val_1['text']= val2
    val_0['text']= do
def bequal():
    do=val_0['text']
    val1=val_2['text']
    val2=val_1['text']
    if do == '1':
        val1= val2+val1
        val_2['text']= val1
    elif do == '2':
        val1= val2-val1
        val_2['text']= val1
    elif do == '3':
        val1= val2/val1
        val_2['text']= val1
    elif do == '4':
        val1= val2*val1
        val_2['text']= val1
        
def bclear():
    val1=0
    val2=0
    do=0
    val_2['text']= val1
    val_1['text']= val2
    val_0['text']= do




    

################# defining wedgets ####################
head_1 = Label(t1,
                bd=4 ,
                relief="solid",
                font="time 18 bold",
                bg="red",
                fg="white",
                text="python calculator #DNY")
val_2 = Label(t2,
                bd=0 ,
                relief="solid",
                font="time 22 bold",
                bg="white",
                fg="black",
                text= val1)
val_1 = Label(t2,
                bd=0 ,
                relief="solid",
                font="time 22 bold",
                bg="white",
                fg="gray",
                text= val2)
val_0 = Label(t2,
                bd=0 ,
                relief="solid",
                font="time 22 bold",
                bg="white",
                fg="gray",
                text= do)
b0= Button(t3,text="0",command= b0c)
b1= Button(t3,text="1",command= b1c)
b2= Button(t3,text="2",command= b2c)
b3= Button(t3,text="3",command= b3c)
b4= Button(t3,text="4",command= b4c)
b5= Button(t3,text="5",command= b5c)
b6= Button(t3,text="6",command= b6c)
b7= Button(t3,text="7",command= b7c)
b8= Button(t3,text="8",command= b8c)
b9= Button(t3,text="9",command= b9c)
add= Button(t3,text="+",command= badd)
sub= Button(t3,text="-",command= bsub)
dev= Button(t3,text="/",command= bdev)
mul= Button(t3,text="*",command= bmul)
equal= Button(t3,text="=",command= bequal)
clear= Button(t3,text="clear",command= bclear)

################# position ##########################
head_1.grid(row=0, column=0)
val_2.grid(row=0, column=2)
#val_1.grid(row=0, column=0)##for debugging
#val_0.grid(row=0, column=1)##for debugging
b0.grid(row=3, column=1)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=0, column=0)
b8.grid(row=0, column=1)
b9.grid(row=0, column=2)
add.grid(row=0, column=3)
sub.grid(row=1, column=3)
dev.grid(row=2, column=3)
mul.grid(row=3, column=3)
equal.grid(row=3, column=2)
clear.grid(row=3, column=0)


################# position frame ##########################
t1.grid(row=0,column=0)
t2.grid(row=1,column=0)
t3.grid(row=2,column=0)



my_window.mainloop()
