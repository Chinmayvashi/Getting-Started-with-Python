from tkinter import*
from tkinter import messagebox

#Creating Window as root
root = Tk()
root.title('GUI DEVELOPMENT')
root.geometry('400x300')

#Defining Checking for Quit and Entry Button
def Checking():
    uname= entry1.get()
    pwd= entry2.get()
    if (uname == "" and pwd == ""):
         messagebox.showinfo("Error","Blank Space Not allowed")
    elif(uname == "Admin" and pwd == "password"):
         messagebox.showinfo("Succes","LoginSucces")
    else:messagebox.showinfo("ERROR","TryAgian")
#Labels to label entrybox
Label(text='Enter your Username',font=0.5).grid(row=0, column=0)
Label(text='Enter your Password',font=0.5).grid(row=1, column=0)

#Creating Entry Box
entry1 = Entry(root)
entry2 = Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

#Entry and Quit Buttons
entre_button = Button(root,text='Enter', command=Checking).grid(row=3, column=1)
quit_button = Button(root, text='Quit', command=root.quit).grid(row=3, column=0,padx=22)


root.mainloop()

