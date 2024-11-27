from tkinter import *
import time
import ttkthemes
from tkinter import ttk ,messagebox,filedialog
import pymysql
import pandas as pd


# function
def clock():
    c_date=time.strftime('%d/%m/%Y')
    c_time=time.strftime('%H:%M:%S')
    datetime_label.config(text=f'   Date: {c_date}\nTime : {c_time}')
    datetime_label.after(1000,clock)

def add_student() :
    def insert_student():
        if id_entry.get()== "" or name_entry.get()== '' or gpa_entry.get()==''or number_entry.get()==''or level_entry.get()=='' or email_entry.get()=='' or address_entry.get()=='' or gender_entry.get()=='' :
            messagebox.showerror('Error' , 'All fields required' ,parent=add_student_windo)
        else:
            try :
                query = "insert into student values (%s, %s, %s ,%s ,%s ,%s ,%s, %s)"
                my_cursor.execute(query , (id_entry.get(), name_entry.get(),level_entry.get(), number_entry.get(),email_entry.get(),address_entry.get() ,gender_entry.get() ,gpa_entry.get()))
                conect.commit()
                result = messagebox.askyesno('Data added successfully' , 'do you want to clean the foem ? ' ,parent=add_student_windo)
                if result :
                    id_entry.delete(0,END)
                    name_entry.delete(0,END)
                    gender_entry.delete(0,END)
                    level_entry.delete(0,END)
                    number_entry.delete(0,END)
                    address_entry.delete(0,END)
                    gpa_entry.delete(0,END)
                    email_entry.delete(0,END)
                show_student()


            except:
                messagebox.showerror('Error', 'id is taken', parent=add_student_windo)


    add_student_windo=Toplevel()
    add_student_windo.title('Add Student')
    add_student_windo.resizable(0,0)
    add_student_windo.grab_set()

    id_label =Label(add_student_windo,text='Id' , font=('times new roman',20,' bold'))
    id_label.grid(row=0 , column=0,padx=20 , pady=15 ,sticky='W')
    id_entry=Entry(add_student_windo, font=('times new roman',15,' bold') ,width= 24)
    id_entry.grid(column=1,row=0 ,padx=15 , pady= 15)

    name_label = Label(add_student_windo, text='Name', font=('times new roman', 20, ' bold'))
    name_label.grid(row=1, column=0, padx=20, pady=15,sticky='W')
    name_entry = Entry(add_student_windo, font=('times new roman', 15, ' bold'), width=24)
    name_entry.grid(column=1, row=1, padx=15, pady=15)

    level_label = Label(add_student_windo, text='Level', font=('times new roman', 20, ' bold'))
    level_label.grid(row=2, column=0, padx=20, pady=15,sticky='W')
    level_entry = Entry(add_student_windo, font=('times new roman', 15, ' bold'), width=24)
    level_entry.grid(column=1, row=2, padx=15, pady=15)

    number_label = Label(add_student_windo, text='Number', font=('times new roman', 20, ' bold'))
    number_label.grid(row=3, column=0, padx=20, pady=15,sticky='W')
    number_entry = Entry(add_student_windo, font=('times new roman', 15, ' bold'), width=24)
    number_entry.grid(column=1, row=3, padx=15, pady=15)

    address_label = Label(add_student_windo, text='Address', font=('times new roman', 20, ' bold'))
    address_label.grid(row=4, column=0, padx=20, pady=15,sticky='W')
    address_entry = Entry(add_student_windo, font=('times new roman', 15, ' bold'), width=24)
    address_entry.grid(column=1, row=4, padx=15, pady=15)

    gender_label = Label(add_student_windo, text='gender', font=('times new roman', 20, ' bold'))
    gender_label.grid(row=5, column=0, padx=20, pady=15,sticky='W')
    gender_entry = Entry(add_student_windo, font=('times new roman', 15, ' bold'), width=24)
    gender_entry.grid(column=1, row=5, padx=15, pady=15)

    email_label = Label(add_student_windo, text='Email', font=('times new roman', 20, ' bold'))
    email_label.grid(row=6, column=0, padx=20, pady=15, sticky='W')
    email_entry = Entry(add_student_windo, font=('times new roman', 15, ' bold'), width=24)
    email_entry.grid(column=1, row=6, padx=15, pady=15)

    gpa_label = Label(add_student_windo, text='GPA', font=('times new roman', 20, ' bold'))
    gpa_label.grid(row=7, column=0, padx=20, pady=15,sticky='W')
    gpa_entry = Entry(add_student_windo, font=('times new roman', 15, ' bold'), width=24)
    gpa_entry.grid(column=1, row=7, padx=15, pady=15)

    add_student_button1=ttk.Button(add_student_windo,text='Save' ,command=insert_student)
    add_student_button1.grid(column=0,row=8,columnspan=2,pady=20)

def search_student():
    def search():
        query = 'select *from student where id =%s or name =%s or level = %s or number = %s or email = %s or address = %s or email = %s or GPA = %s'
        my_cursor.execute(query,(id_entry.get(), name_entry.get(),level_entry.get(), number_entry.get(),email_entry.get(),address_entry.get() ,gender_entry.get() ,gpa_entry.get()))
        data = my_cursor.fetchall()
        student_tabel.delete(*student_tabel.get_children())
        for x in data:
            row_data = list(x)
            student_tabel.insert('', END, values=row_data)
    search_student_windo = Toplevel()
    search_student_windo.title('Search Student')
    search_student_windo.resizable(0, 0)
    search_student_windo.grab_set()
    id_label = Label(search_student_windo, text='Id', font=('times new roman', 20, ' bold'))
    id_label.grid(row=0, column=0, padx=20, pady=15, sticky='W')
    id_entry = Entry(search_student_windo, font=('times new roman', 15, ' bold'), width=24)
    id_entry.grid(column=1, row=0, padx=15, pady=15)

    name_label = Label(search_student_windo, text='Name', font=('times new roman', 20, ' bold'))
    name_label.grid(row=1, column=0, padx=20, pady=15, sticky='W')
    name_entry = Entry(search_student_windo, font=('times new roman', 15, ' bold'), width=24)
    name_entry.grid(column=1, row=1, padx=15, pady=15)

    level_label = Label(search_student_windo, text='Level', font=('times new roman', 20, ' bold'))
    level_label.grid(row=2, column=0, padx=20, pady=15, sticky='W')
    level_entry = Entry(search_student_windo, font=('times new roman', 15, ' bold'), width=24)
    level_entry.grid(column=1, row=2, padx=15, pady=15)

    number_label = Label(search_student_windo, text='Number', font=('times new roman', 20, ' bold'))
    number_label.grid(row=3, column=0, padx=20, pady=15, sticky='W')
    number_entry = Entry(search_student_windo, font=('times new roman', 15, ' bold'), width=24)
    number_entry.grid(column=1, row=3, padx=15, pady=15)

    address_label = Label(search_student_windo, text='Address', font=('times new roman', 20, ' bold'))
    address_label.grid(row=4, column=0, padx=20, pady=15, sticky='W')
    address_entry = Entry(search_student_windo, font=('times new roman', 15, ' bold'), width=24)
    address_entry.grid(column=1, row=4, padx=15, pady=15)

    gender_label = Label(search_student_windo, text='gender', font=('times new roman', 20, ' bold'))
    gender_label.grid(row=5, column=0, padx=20, pady=15, sticky='W')
    gender_entry = Entry(search_student_windo, font=('times new roman', 15, ' bold'), width=24)
    gender_entry.grid(column=1, row=5, padx=15, pady=15)

    email_label = Label(search_student_windo, text='Email', font=('times new roman', 20, ' bold'))
    email_label.grid(row=6, column=0, padx=20, pady=15, sticky='W')
    email_entry = Entry(search_student_windo, font=('times new roman', 15, ' bold'), width=24)
    email_entry.grid(column=1, row=6, padx=15, pady=15)

    gpa_label = Label(search_student_windo, text='GPA', font=('times new roman', 20, ' bold'))
    gpa_label.grid(row=7, column=0, padx=20, pady=15, sticky='W')
    gpa_entry = Entry(search_student_windo, font=('times new roman', 15, ' bold'), width=24)
    gpa_entry.grid(column=1, row=7, padx=15, pady=15)

    search_student_button1 = ttk.Button(search_student_windo, text='Search', command=search)
    search_student_button1.grid(column=0, row=8, columnspan=2, pady=20)

def delet_student ():
    index=student_tabel.focus()
    data = student_tabel.item(index)
    id = data['values'][0]
    query='delete from student where id=%s'
    my_cursor.execute(query,id)
    conect.commit()
    messagebox.showinfo('Deleted' , f'ID : {id}  id deleted')
    show_student()


def show_student():
    query = 'select *from student'
    my_cursor.execute(query)
    data = my_cursor.fetchall()
    student_tabel.delete(*student_tabel.get_children())
    for x in data:
        row_data = list(x)
        student_tabel.insert('', END, values=row_data)

def update_student():
    def up_date_student() :
        query='update student set id= %s , name = %s , level = %s ,number = %s ,email= %s , address = %s ,gander = %s ,gpa = %s where id = %s'
        my_cursor.execute(query,(id_entry.get(), name_entry.get(),level_entry.get(), number_entry.get(),email_entry.get()
                                 ,address_entry.get() ,gender_entry.get() ,gpa_entry.get() ,row[0] ))
        conect.commit()
        messagebox.showinfo('Successful' , 'your student data are update' , parent = up_date_student_windo)
        show_student()
        up_date_student_windo.destroy()

    up_date_student_windo = Toplevel()
    up_date_student_windo.title('Up-date Student')
    up_date_student_windo.resizable(0, 0)
    up_date_student_windo.grab_set()

    id_label = Label(up_date_student_windo, text='Id', font=('times new roman', 20, ' bold'))
    id_label.grid(row=0, column=0, padx=20, pady=15, sticky='W')
    id_entry = Entry(up_date_student_windo, font=('times new roman', 15, ' bold'), width=24)
    id_entry.grid(column=1, row=0, padx=15, pady=15)

    name_label = Label(up_date_student_windo, text='Name', font=('times new roman', 20, ' bold'))
    name_label.grid(row=1, column=0, padx=20, pady=15, sticky='W')
    name_entry = Entry(up_date_student_windo, font=('times new roman', 15, ' bold'), width=24)
    name_entry.grid(column=1, row=1, padx=15, pady=15)

    level_label = Label(up_date_student_windo, text='Level', font=('times new roman', 20, ' bold'))
    level_label.grid(row=2, column=0, padx=20, pady=15, sticky='W')
    level_entry = Entry(up_date_student_windo, font=('times new roman', 15, ' bold'), width=24)
    level_entry.grid(column=1, row=2, padx=15, pady=15)

    number_label = Label(up_date_student_windo, text='Number', font=('times new roman', 20, ' bold'))
    number_label.grid(row=3, column=0, padx=20, pady=15, sticky='W')
    number_entry = Entry(up_date_student_windo, font=('times new roman', 15, ' bold'), width=24)
    number_entry.grid(column=1, row=3, padx=15, pady=15)

    address_label = Label(up_date_student_windo, text='Address', font=('times new roman', 20, ' bold'))
    address_label.grid(row=4, column=0, padx=20, pady=15, sticky='W')
    address_entry = Entry(up_date_student_windo, font=('times new roman', 15, ' bold'), width=24)
    address_entry.grid(column=1, row=4, padx=15, pady=15)

    gender_label = Label(up_date_student_windo, text='gender', font=('times new roman', 20, ' bold'))
    gender_label.grid(row=5, column=0, padx=20, pady=15, sticky='W')
    gender_entry = Entry(up_date_student_windo, font=('times new roman', 15, ' bold'), width=24)
    gender_entry.grid(column=1, row=5, padx=15, pady=15)

    email_label = Label(up_date_student_windo, text='Email', font=('times new roman', 20, ' bold'))
    email_label.grid(row=6, column=0, padx=20, pady=15, sticky='W')
    email_entry = Entry(up_date_student_windo, font=('times new roman', 15, ' bold'), width=24)
    email_entry.grid(column=1, row=6, padx=15, pady=15)

    gpa_label = Label(up_date_student_windo, text='GPA', font=('times new roman', 20, ' bold'))
    gpa_label.grid(row=7, column=0, padx=20, pady=15, sticky='W')
    gpa_entry = Entry(up_date_student_windo, font=('times new roman', 15, ' bold'), width=24)
    gpa_entry.grid(column=1, row=7, padx=15, pady=15)

    update_student_button = ttk.Button(up_date_student_windo, text='Update' , command=up_date_student)
    update_student_button.grid(column=0, row=8, columnspan=2, pady=20)

    index = student_tabel.focus()
    data = student_tabel.item(index)
    row = data['values']

    id_entry.insert(0,row[0])
    name_entry.insert(0,row[1])
    level_entry.insert(0,row[2])
    number_entry.insert(0,row[3])
    email_entry.insert(0,row[4])
    address_entry.insert(0,row[5])
    gender_entry.insert(0,row[6])
    gpa_entry.insert(0,row[7])

def export_database():
    url = filedialog.asksaveasfilename(defaultextension='csv')
    index=student_tabel.get_children()
    file_list=[]
    for x in index :
        row=student_tabel.item(x)
        value=row['values']
        file_list.append(value)
    csv=pd.DataFrame(file_list,columns=['Id' , 'Name' , 'Level','Number' , 'Email' , 'Address' , 'Gender' , 'Gpa'])
    csv.to_csv(url,index=False)
    messagebox.showinfo('Success' , 'Your file is Saved' , parent = root)

def exit_project():
    result = messagebox.askyesno('Confirm' , 'Do you want to wxxit ?')
    if result:
        root.destroy()


def connect_db ():
    try:
        global conect
        conect=pymysql.connect(host='localhost' , user='root' , password='******')
        global my_cursor
        my_cursor =conect.cursor()
        messagebox.showinfo('successful', 'Connected to database ')
    except:
        messagebox.showerror('Error' , 'cannot connect to database \n '
                                  'Please restart')
    try:
        query = 'create database sms'
        my_cursor.execute(query)
        query = 'use sms'
        my_cursor.execute(query)
        query = 'create table student(Id int not null primary key  , name varchar(30) ,level int not null ,' \
                ' number varchar(11) , email varchar(30) ,address varchar(100) , gender varchar(20) , GPA float )'
        my_cursor.execute(query)
    except:
        query = 'use sms'
        my_cursor.execute(query)

# GUI
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x750+200+30')
root.resizable(False ,False)
root.title('Student management system')


#clock
datetime_label=Label(root ,font=('times new roman',20 ,' bold'))
datetime_label.place(x=5,y=5)
clock()

#add slider
slider_label =Label(root,text='Student management system',font=('times new roman',40,'italic bold') ,width=30)
slider_label.place(x=250,y=10)

#left frame
left_frame=Frame(root )
left_frame.place(x=50 , y=80 ,width=300 , height=700)

#logo
logo_img = PhotoImage(file='student.png')
logo_label = Label(left_frame,image=logo_img)
logo_label.grid(column=0,row=0 , pady=10)

#buttons

add_student_button=ttk.Button(left_frame ,text="Add Student",width=25 ,command=add_student)
add_student_button.grid(row=1 , pady= 15  )

search_student_button=ttk.Button(left_frame ,text="Search Student " ,width=25 ,command=search_student)
search_student_button.grid(row=2 , pady= 15  )

delete_student_button=ttk.Button(left_frame ,text="Delete Student " ,width=25 , command=delet_student)
delete_student_button.grid(row=3 , pady= 15  )

update_student_button=ttk.Button(left_frame ,text="Update Student ",width=25 , command=update_student)
update_student_button.grid(row=4 , pady= 15  )

show_student_button=ttk.Button(left_frame ,text="Show Student " , width=25 ,command=show_student)
show_student_button.grid(row=5 , pady= 15  )

export_student_button=ttk.Button(left_frame ,text="Export Student " ,width=25 ,command=export_database)
export_student_button.grid(row=6 , pady= 15  )

exit_button=ttk.Button(left_frame ,text="Exit " ,width=25 , command=exit_project)
exit_button.grid(row=7, pady= 15  )


# right frame
right_frame=Frame(root)
right_frame.place(x=320 , y=100 ,width=820 , height=650  )

scroll_x = Scrollbar(right_frame , orient=HORIZONTAL)
scroll_y = Scrollbar(right_frame , orient=VERTICAL)

student_tabel=ttk.Treeview(right_frame,columns=('Id','Name','level' ,'Number','Email'
                                   ,'Address','gender' , 'GPA') , xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set)

scroll_x.config(command=student_tabel.xview)
scroll_y.config(command=student_tabel.yview)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

student_tabel.pack(fill=BOTH,expand=1)

student_tabel.heading('Id',text='Id')
student_tabel.heading('level',text='level')
student_tabel.heading('Name',text='Name')
student_tabel.heading('Number',text='Number')
student_tabel.heading('Email',text='Email')
student_tabel.heading('Address',text='Address')
student_tabel.heading('gender',text='gender')
student_tabel.heading('GPA',text='GPA')

student_tabel.column('Id',width=80 , anchor=CENTER )
student_tabel.column('level',width= 80,anchor=CENTER)
student_tabel.column('Name',width=300,anchor=CENTER)
student_tabel.column('Number',width=200,anchor=CENTER)
student_tabel.column('Email',width=300,anchor=CENTER)
student_tabel.column('Address',width=300,anchor=CENTER)
student_tabel.column('gender',width=200,anchor=CENTER)
student_tabel.column('GPA',width=50,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview', rowheight=40 , font= ('arial',13,'italic') ,foreground='black' , background='white')
style.configure('Treeview.Heading' ,font= ('arial',15,'italic') )
student_tabel.config(show='headings')

connect_db ()

root.mainloop()

