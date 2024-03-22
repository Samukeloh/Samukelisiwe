from random import *
from tkinter import *


num="0123456789"
alphanum="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spalphanum="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'#@+(){}"


def create_pass():
    TheChoice = Tchoice.get()
    if TheChoice =="":
        resultBox.delete(0.0,END)
        resultBox.insert(END,"\n select the type of password you'd like")

    length = int(pass_length.get())
    randPass = []
    for i in range(length):
        randPass.append(choice(TheChoice))

    result = "".join(randPass)

    TheResult ="\n *** Your password is : "+result+" ***\n"

    resultBox.delete(0.0,END)
    resultBox.insert(END,TheResult)

##passlen = int(input("Enter password length \n"))
##randPass = []

##print("select the type of password \n1.Numbers\n2.Alphanum\n3.Special alphanumeric\n")
##selecttype = int(input())
##
##if selecttype == 1:
##    for i in range(passlen):
##        randPass.append(choice(num))
##elif selecttype ==2:
##    for i in range(passlen):
##        randPass.append(choice(alphanum))
##else:
##   for i in range(passlen):
##        randPass.append(choice(spalphanum))
##
##result = "".join(randPass)
##
##print(" Your random password is :"+result)




window = Tk()
window.geometry("800x500")

ProgName = Label(window,font=('kristen ITC',15,'bold'),text="Password Generator (^_^)",fg="blue")
ProgName.grid(row=1,column=3,padx=200,pady=30)

chooseType = Label(window,font=('kristen ITC',15,'bold'),text="choose a type of among the 3")
chooseType.place(relx=.03, rely=.25)

Tchoice= StringVar()
NumChoice = Radiobutton(window,font=('corbel',10,'italic'),text ="Numeric", variable = Tchoice,value=num)
NumChoice.place(relx=.3, rely= .35)
AlphaNumChoice = Radiobutton(window,font=('corbel',10,'italic'),text ='Alphanumeric', variable = Tchoice,value=alphanum)
AlphaNumChoice.place(relx=.3, rely= .4)
SpecialChoice = Radiobutton(window,font=('corbel',10,'italic'),text ='Special', variable = Tchoice,value=spalphanum)
SpecialChoice.place(relx=.3, rely= .45)

size =Label(window,text="size",font=('copperplate Gothic',10,'bold'))
size.place(relx=.65 , rely = .4)

pass_length = Spinbox(window,from_=8,to=100)
pass_length.place(relx=.73, rely =.4)
pass_length.config(state="readonly")



GenButton = Button(window,text = "Generate",command=create_pass)
GenButton.place(relx = .45, rely= .57)

resultBox = Text(window, height=6, width = 70)
resultBox.place(relx=.06, rely = .7)





window.mainloop()




        


