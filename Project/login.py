from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login() :
    if  username_text.get()== 'Ahmed' and pass_text.get() == '1234' :
        messagebox.showinfo('Success', 'Welcome')
        main_windo.destroy()
        import sms

    elif  pass_text.get() == '' or username_text.get()== '':
        messagebox.showerror('Error' ,'User or password fields can not be empty ' )
    else :
        messagebox.showerror('Error', 'Invaild user or password')


# creat main windo
main_windo = Tk()
main_windo.geometry('1280x700')
main_windo.resizable(False ,False)
main_windo.title('Login')


# add background to windo
bki = ImageTk.PhotoImage(file='bg.jpg')
bkil= Label(main_windo,image=bki)
bkil.place(x=0, y=0)

#creat login frame

loginframe =Frame(main_windo ,bg='white')
loginframe.place(x=400,y=150)

#add logo to frame
logo_image = PhotoImage(file="logo.png")
logo_image_label = Label(loginframe,image= logo_image)
logo_image_label.grid(row=0,column=0,columnspan=2,pady=10)

#add username label
username_image = PhotoImage(file='user.png')
username_label = Label(loginframe ,image=username_image,text='Username' , compound=LEFT ,
                       font=('times new roman',20,'bold') , bg='white' )
username_text=Entry(loginframe , font=('times new roman',20) , bd=5)
username_text.grid(row=1,column=1,padx=20)
username_label.grid(row=1, column=0,pady=10)




#add pass label
pass_image = PhotoImage(file='password.png')
pass_label = Label(loginframe ,image=pass_image,text='Password' , compound=LEFT ,
                       font=('times new roman',20,'bold') , bg='white' )
pass_text=Entry(loginframe , font=('times new roman',20) , bd=5)
pass_text.grid(row=2,column=1,padx=20)
pass_label.grid(row=2, column=0,pady=10)

#creat button

login_button =Button(loginframe,text='Login',font=('times new roman',15,'bold') ,width=15
                     , bg='white' ,activebackground= 'cornflowerblue' ,cursor='hand2' , command= login)
login_button.grid(row=3 ,column=0,columnspan=2 ,pady=10 ,padx=20)

main_windo.mainloop()