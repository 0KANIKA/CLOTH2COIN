from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import mysql.connector as s
import webbrowser as w1
from tkinter import messagebox

mc=s.connect(host='localhost',user='root',passwd='99Jan2012',database='cloth_donate')
cr=mc.cursor()
def cloth1():
    w8=Tk()
    w8.geometry("1570x1170")
    
    w8.configure(bg='#f5e6d0')
    w8.mainloop()
    
def disp():
    win3=Toplevel()
    win3.geometry("1570x1170")
    win3.configure(bg='#f5e6d0')
    img2= PhotoImage(file='bill.png', master= win3)
    img_label2= Label(win3,image=img2)
    img_label2.place(x=300, y=25)
    img1= PhotoImage(file='comp1.png', master= win3)
    img_label1= Label(win3,image=img1)
    img_label1.place(x=650, y=120)
##    Label(win3,text=""" No 15, Nageshwar Rao Road, Chrompet Chennai-600044""",font=('monotype corsiva',25),
##          fg='black',bg='#ebca9a').place(x=400,y=340)
##    Label(win3,text="""CIN U56789TN2023BAB125678               GSTIN:22ASDRT22356H1WE""",font=('monotype corsiva',20),
##          fg='black',bg='#ebca9a').place(x=400,y=400)
    d={}
##    d1={'Red Eye':180,'Black Coffee':100,'Espresso':120,'Mocha':110,'Irish Coffee':300,
##        'Cappuccino':120,'Latte':140,'Iced Americano':200}
##    
    if (combo21.get()!='' and combo31.get()!=''):
        d[combo21.get()]=combo31.get()
    if (combo22.get()!='' and combo32.get()!=''):
        d[combo22.get()]=combo32.get()
    if (combo23.get()!='' and  combo33.get()!=''):
        d[combo23.get()]=combo33.get()
    if (combo24.get()!='' and combo34.get()!=''):
        d[combo24.get()]=combo34.get()
    if (combo25.get()!='' and  combo35.get()!=''):
        d[combo25.get()]=combo35.get()
    if (combo26.get()!='' and  combo36.get()!=''):
        d[combo26.get()]=combo36.get()
    if (combo27.get()!='' and  combo37.get()!=''):
        d[combo27.get()]=combo37.get()
    if (combo28.get()!='' and combo38.get()!=''):
        d[combo28.get()]=combo38.get()
    if (combo29.get()!='' and combo39.get()!=''):
        d[combo29.get()]=combo39.get()
    if (combo30.get()!='' and  combo40.get()!=''):
        d[combo30.get()]=combo40.get()
        
    l=list(d.keys())
    print(d)
    i=0
    total=0
    for x in l:
        Label(win3,text=x,font=('monotype corsiva',20),
          fg='black',bg='#ebca9a').place(x=400,y=360+i*50)
        Label(win3,text=d[x],font=('monotype corsiva',20),
          fg='black',bg='#ebca9a').place(x=700,y=360+i*50)
        i+=1
        total+=1
        Label(win3,text="Total: ",font=('monotype corsiva',20),
          fg='black',bg='#ebca9a').place(x=900,y=800)
    Label(win3,text=total,font=('monotype corsiva',20),
          fg='black',bg='#ebca9a').place(x=1000,y=800)
##        
##    btn = Button(win1, text="PAY", command=web, font=('Bahnschrift Condensed', 20))
##    btn.place(x=1300, y=800)
##    
    win3.mainloop()

def cloth():
    w3=Tk()
    w3.geometry("1570x1170")
    w3.configure(background='light sea green')
    img= PhotoImage(file='pant.png', master= w3)
    img_label= Label(w3,image=img)
    img_label.place(x=50,y=10)

    img1= PhotoImage(file='tshirt.png', master= w3)
    img_label1= Label(w3,image=img1)
    img_label1.place(x=50, y=190)

    img2= PhotoImage(file='top.png', master= w3)
    img_label2= Label(w3,image=img2)
    img_label2.place(x=50, y=370)

    global combo21
    combo21= ttk.Combobox(w3, values=["Men's Pant","Women's Pant"],width=10,height=50)
    combo21.pack()
    combo21.config(font=('Bahnschrift Condensed',20))
    combo21.place(x=350,y=50)
    global combo22
    combo22= ttk.Combobox(w3, values=["Men's Shirt","Women's Shirt"],width=10,height=50)
    combo22.pack()
    combo22.config(font=('Bahnschrift Condensed',20))
    combo22.place(x=350,y=230)
    global combo23
    combo23= ttk.Combobox(w3, values=["Women's Short Kurtis"],width=10,height=50)
    combo23.pack()
    combo23.config(font=('Bahnschrift Condensed',20))
    combo23.place(x=350,y=410)
    global combo24
    combo24= ttk.Combobox(w3, values=["Women's Skirt"],width=10,height=50)
    combo24.pack()
    combo24.config(font=('Bahnschrift Condensed',20))
    combo24.place(x=350,y=590)
    global combo25
    combo25= ttk.Combobox(w3, values=["Women's Frock"],width=10,height=50)
    combo25.pack()
    combo25.config(font=('Bahnschrift Condensed',20))
    combo25.place(x=350,y=770)


    img3= PhotoImage(file='skirt.png', master= w3)
    img_label3= Label(w3,image=img3)
    img_label3.place(x=50,y=550)

    img4= PhotoImage(file='frock.png', master= w3)
    img_label4= Label(w3,image=img4)
    img_label4.place(x=50, y=730)

    img5= PhotoImage(file='jack.png', master= w3)
    img_label5= Label(w3,image=img5)
    img_label5.place(x=750, y=10)

    img6= PhotoImage(file='ts1.png', master= w3)
    img_label6= Label(w3,image=img6)
    img_label6.place(x=750,y=190)

    img7= PhotoImage(file='baby1.png', master= w3)
    img_label7= Label(w3,image=img7)
    img_label7.place(x=750, y=370)

    img8= PhotoImage(file='baby2.png', master= w3)
    img_label8= Label(w3,image=img8)
    img_label8.place(x=750, y=550)

    img9= PhotoImage(file='baby3.png', master= w3)
    img_label9= Label(w3,image=img9)
    img_label9.place(x=750, y=730)

    global combo26
    combo26= ttk.Combobox(w3, values=["Women's Jacket"],width=10,height=50)
    combo26.pack()
    combo26.config(font=('Bahnschrift Condensed',20))
    combo26.place(x=1050,y=50)
    global combo27
    combo27= ttk.Combobox(w3, values=["Men's Tshirt","Women's Tshirt"],width=10,height=50)
    combo27.pack()
    combo27.config(font=('Bahnschrift Condensed',20))
    combo27.place(x=1050,y=230)
    global combo28
    combo28= ttk.Combobox(w3, values=["Kids:Sweater"],width=10,height=50)
    combo28.pack()
    combo28.config(font=('Bahnschrift Condensed',20))
    combo28.place(x=1050,y=410)
    global combo29
    combo29= ttk.Combobox(w3, values=["Kids:Boy"],width=10,height=50)
    combo29.pack()
    combo29.config(font=('Bahnschrift Condensed',20))
    combo29.place(x=1050,y=590)
    global combo30
    combo30= ttk.Combobox(w3, values=["Kids:Frock"],width=10,height=50)
    combo30.pack()
    combo30.config(font=('Bahnschrift Condensed',20))
    combo30.place(x=1050,y=770)

    #combo 2.1
    global combo31
    combo31= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo31.pack()
    combo31.config(font=('Bahnschrift Condensed',20))
    combo31.place(x=550,y=50)
    global combo32
    combo32= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo32.pack()
    combo32.config(font=('Bahnschrift Condensed',20))
    combo32.place(x=550,y=230)
    global combo33
    combo33= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo33.pack()
    combo33.config(font=('Bahnschrift Condensed',20))
    combo33.place(x=550,y=410)
    global combo34
    combo34= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo34.pack()
    combo34.config(font=('Bahnschrift Condensed',20))
    combo34.place(x=550,y=590)
    global combo35
    combo35= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo35.pack()
    combo35.config(font=('Bahnschrift Condensed',20))
    combo35.place(x=550,y=770)
    

    #combo2.2
    global combo36
    combo36= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo36.pack()
    combo36.config(font=('Bahnschrift Condensed',20))
    combo36.place(x=1250,y=50)
    global combo37
    combo37= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo37.pack()
    combo37.config(font=('Bahnschrift Condensed',20))
    combo37.place(x=1250,y=230)
    global combo38
    combo38= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo38.pack()
    combo38.config(font=('Bahnschrift Condensed',20))
    combo38.place(x=1250,y=410)
    global combo39
    combo39= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo39.pack()
    combo39.config(font=('Bahnschrift Condensed',20))
    combo39.place(x=1250,y=590)
    global combo40
    combo40= ttk.Combobox(w3, values=[1,2,3,4,5,6,7,8,9,10],width=10,height=50)
    combo40.pack()
    combo40.config(font=('Bahnschrift Condensed',20))
    combo40.place(x=1250,y=770)
    sb=Button(w3,text='Submit',font=('ariel',20),fg='blue',bg='light green',command=disp)
    sb.place(x=1200,y=850)
    w3.mainloop()

def log1():

    usi2=us2.get()
    uni2=an2.get()
    edi2=ed2.get()
    phi2=ph2.get()
    psi2=ps2.get()
    #addi2=add.get()
    if not(usi2 or uni2 or edi2 or phi2 or psi2 or adi2):
        messagebox.showinfo("Error!!!","Please enter the valid Credentials",parent=w2)
        w.destroy()

    sql="insert into login4 values('{}','{}','{}',{},'{}');".format(usi2,uni2,edi2,phi2,psi2)
    cr.execute(sql)
    mc.commit()
    sql1="insert into login3 values('{}','{}');".format(usi2,psi2)
    cr.execute(sql1)
    mc.commit()
    #menu()
def newuser1():
    global w2
    w2=Tk()
    w2.geometry('1800x1520')
    w2.configure(background='light sea green')
##    img= PhotoImage(file='n222.png', master= w)
##    img_label= Label(w,image=img)
##    img_label.place(x=0, y=0)    
    Label(w2,text='''PLEASE ENTER THE REQUIRED CREDENTIALS ''',font=('ariel',22),bg='#F4A460').place(x=200,y=250)
    Label(w2,text='Enter your userid:',font=('ariel',25),bg='#F4A460').place(x=90,y=350)
    Label(w2,text='Enter your username:',font=('ariel',25),bg='#F4A460').place(x=90,y=410)
    Label(w2,text='Enter your email id:',font=('ariel',25),bg='#F4A460').place(x=90,y=470)
    Label(w2,text='Enter your phonenumber:',font=('ariel',25),bg='#F4A460').place(x=90,y=530)
    Label(w2,text='Enter your password:',font=('ariel',25),bg='#F4A460').place(x=90,y=590)
    #Label(w2,text='Enter your address:',font=('ariel',25),bg='#F4A460').place(x=90,y=650)



    global us2
    us2=Entry(w2,font=('ariel',25),bg='beige')
    us2.place(x=600,y=350)
    global an2
    an2=Entry(w2,font=('ariel',25),bg='beige')
    an2.place(x=600,y=410)
    global ed2
    ed2=Entry(w2,font=('ariel',25),bg='beige')
    ed2.place(x=600,y=470)
    global ph2
    ph2=Entry(w2,font=('ariel',25),bg='beige')
    ph2.place(x=600,y=530)
    global ps2
    ps2=Entry(w2,font=('ariel',25),show='*',bg='beige')
    ps2.place(x=600,y=590)
    Button(w2,text='submit',font=('ariel',25),bg='AliceBlue',command=log1).place(x=550,y=750)
   
    
    w2.mainloop()


def canc1():
    us5=Entry(fr,font=('ariel',25),bg='lavender')
    us5.place(x=300,y=200)
    ps5=Entry(fr,font=('ariel',25),show='*',bg='lavender')
    ps5.place(x=300,y=300)
    win1.mainloop()
    dtb1()
def dtb1():
    l1=()
    us4=us3.get()
    ps4=ps3.get()
    
    if not(us4 or ps4):
        messagebox.showinfo("Error!!!","Please enter valid Credentials",parent=win1)
    else:
        
        l1=l1+(us4,)
        l1=l1+(ps4,)
        q1='select * from login3'
        cr.execute(q1)
        d1=cr.fetchall()
        
        #food()
        if l1 in d1:
            #menu()
            print()
        else:
            messagebox.showinfo("Error!!!","Entered Username or Password is incorrect",parent=win1)

def f2():
    global win1
    win1 = Tk()
    win1.geometry("1670x980")

#Define the PhotoImage Constructor by passing the image file
##    img= PhotoImage(file='n119.png', master= win)
##    img_label= Label(win,image=img)
    img= PhotoImage(file='log1.png', master= win1)
    img_label= Label(win1,image=img)

###define the position of the image
    img_label.place(x=0, y=0)
##
###define the position of the image
##    img_label.place(x=0, y=0)
##    login_label = Label(win, text="Login", font=("Helvetica", 20, "bold"), fg="blue")
##    login_label.pack(pady=150)
    global fr1
    global us3,ps3
    
    fr1= Frame(win1, highlightbackground="brown", height=650, width=690,highlightthickness=5, bg='light yellow')
    fr1.pack(side=TOP)
    fr1.place(x=10, y=250)
    Label(fr1,text='LOGIN',font=('monotype corsiva',50),
          fg='black',bg='light yellow').place(x=250,y=50)
    Label(fr1,text='Enter your userid:',font=('Bahnschrift condensed',25),
          bg='light yellow').place(x=40,y=200)
    us3=Entry(fr1,font=('lucida handwritting',25),bg='lavender',fg='green')
    us3.place(x=300,y=200)
    Label(fr1,text='Enter your password:',font=('Bahnschrift condensed',25)
          ,bg='light yellow').place(x=40,y=300)   
    ps3=Entry(fr1,font=('ariel',25),show='*',bg='lavender')
    ps3.place(x=300,y=300)

    Button(win1,text='Cancel',font=('ariel',20),
           fg='blue',bg='light green',command=canc1).place(x=100,y=650)
    Button(win1,text='New User',font=('ariel',20),fg='blue',bg='light green',command=newuser1).place(x=250,y=650)
    sb=Button(win1,text='Submit',font=('ariel',20),fg='blue',bg='light green',command=dtb1)
    sb.place(x=430,y=650)
    win1.mainloop()
######

def log():

    usi=us.get()
    uni=an.get()
    edi=ed.get()
    phi=ph.get()
    psi=ps.get()
    addi=add.get()
    if not(usi or uni or edi or phi or psi or adi):
        messagebox.showinfo("Error!!!","Please enter the valid Credentials",parent=w)
        w.destroy()

    sql="insert into login1 values('{}','{}','{}',{},'{}','{}');".format(usi,uni,edi,phi,psi,addi)
    cr.execute(sql)
    mc.commit()
    sql1="insert into login values('{}','{}');".format(usi,psi)
    cr.execute(sql1)
    mc.commit()
    #menu()
def newuser():
    global w
    w=Tk()
    w.geometry('1800x1520')
    w.configure(background='light sea green')
##    img= PhotoImage(file='n222.png', master= w)
##    img_label= Label(w,image=img)
##    img_label.place(x=0, y=0)    
    Label(w,text='''PLEASE ENTER THE REQUIRED CREDENTIALS ''',font=('ariel',22),bg='#F4A460').place(x=200,y=250)
    Label(w,text='Enter your userid:',font=('ariel',25),bg='#F4A460').place(x=90,y=350)
    Label(w,text='Enter your username:',font=('ariel',25),bg='#F4A460').place(x=90,y=410)
    Label(w,text='Enter your email id:',font=('ariel',25),bg='#F4A460').place(x=90,y=470)
    Label(w,text='Enter your phonenumber:',font=('ariel',25),bg='#F4A460').place(x=90,y=530)
    Label(w,text='Enter your password:',font=('ariel',25),bg='#F4A460').place(x=90,y=590)
    Label(w,text='Enter your address:',font=('ariel',25),bg='#F4A460').place(x=90,y=650)



    global us
    us=Entry(w,font=('ariel',25),bg='beige')
    us.place(x=600,y=350)
    global an
    an=Entry(w,font=('ariel',25),bg='beige')
    an.place(x=600,y=410)
    global ed
    ed=Entry(w,font=('ariel',25),bg='beige')
    ed.place(x=600,y=470)
    global ph
    ph=Entry(w,font=('ariel',25),bg='beige')
    ph.place(x=600,y=530)
    global ps
    ps=Entry(w,font=('ariel',25),show='*',bg='beige')
    ps.place(x=600,y=590)
    global add
    add=Entry(w,font=('ariel',25),bg='beige')
    add.place(x=600,y=650)
    Button(w,text='submit',font=('ariel',25),bg='AliceBlue',command=log).place(x=550,y=750)
    w.mainloop()

def token():
    global img4, img5,img6 # retain both image references

    w5 = Tk()  # use Toplevel instead of Tk
    w5.geometry("1570x1170")

    img4 = PhotoImage(file='dona.png', master=w5)
    img_label4 = Label(w5, image=img4)
    img_label4.place(x=0, y=0)

    img5 = PhotoImage(file="donar.png", master=w5)
    img_button5 = Button(w5, image=img5, command=cloth, borderwidth=0)
    img_button5.image = img5  # also store on widget for safety
    img_button5.place(x=100, y=140)

    img6 = PhotoImage(file="profile.png", master=w5)
    img_button6 = Button(w5, image=img6, command=cloth1, borderwidth=0)
    img_button6.image = img6  # also store on widget for safety
    img_button6.place(x=500, y=140)
def canc():
    us=Entry(fr,font=('ariel',25),bg='lavender')
    us.place(x=300,y=200)
    ps=Entry(fr,font=('ariel',25),show='*',bg='lavender')
    ps.place(x=300,y=300)
    win.mainloop()
    dtb()
def dtb():
    l=()
    us1=us2.get()
    ps1=ps2.get()
    
    if not(us1 or ps1):
        messagebox.showinfo("Error!!!","Please enter valid Credentials",parent=win)
    else:
        
        l=l+(us1,)
        l=l+(ps1,)
        q1='select * from login'
        cr.execute(q1)
        d=cr.fetchall()
        
        #food()
        if l in d:
            cloth()
            print()
        else:
            messagebox.showinfo("Error!!!","Entered Username or Password is incorrect",parent=win)

def f1():
    global win
    win = Tk()
    win.geometry("1670x980")

#Define the PhotoImage Constructor by passing the image file
    img= PhotoImage(file='log1.png', master= win)
    img_label= Label(win,image=img)

###define the position of the image
    img_label.place(x=0, y=0)
##    login_label = Label(win, text="Login", font=("Helvetica", 20, "bold"), fg="blue")
##    login_label.pack(pady=150)
    global fr
    global us2,ps2
    
    fr = Frame(win, highlightbackground="brown", height=650, width=690,highlightthickness=5, bg='light yellow')
    fr.pack(side=TOP)
    fr.place(x=10, y=250)
    Label(fr,text='LOGIN',font=('monotype corsiva',50),
          fg='black',bg='light yellow').place(x=250,y=50)
    Label(fr,text='Enter your userid:',font=('Bahnschrift condensed',25),
          bg='light yellow').place(x=40,y=200)
    us2=Entry(fr,font=('lucida handwritting',25),bg='lavender',fg='green')
    us2.place(x=300,y=200)
    Label(fr,text='Enter your password:',font=('Bahnschrift condensed',25)
          ,bg='light yellow').place(x=40,y=300)   
    ps2=Entry(fr,font=('ariel',25),show='*',bg='lavender')
    ps2.place(x=300,y=300)

    Button(win,text='Cancel',font=('ariel',20),
           fg='blue',bg='light green',command=canc).place(x=100,y=650)
    Button(win,text='New User',font=('ariel',20),fg='blue',bg='light green',command=newuser).place(x=250,y=650)
    sb=Button(win,text='Submit',font=('ariel',20),fg='blue',bg='light green',command=dtb)
    sb.place(x=430,y=650)
    win.mainloop()
    
#f1()
win2=Tk()
win2.geometry("1570x1170")
#win.configure(bg='lightblue')
##
#Define the PhotoImage Constructor by passing the image file
img1= PhotoImage(file='img4.png', master= win2)
img_label1= Label(win2,image=img1)
img_label1.place(x=0, y=0)

img2 = PhotoImage(file="don.png")
img_button2 = Button(win2, image=img2,command=f1,borderwidth=0)
img_button2.place(x=300,y=140)
img3 = PhotoImage(file="admin.png")
img_button3= Button(win2, image=img3,command=f2,borderwidth=0)
img_button3.place(x=950,y=140)

#define the position of the image

win2.mainloop()
