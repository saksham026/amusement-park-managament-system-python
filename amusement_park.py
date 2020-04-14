import tkinter
from tkinter import*
from tkinter import messagebox
import random
import time
import os
import mysql.connector

root = Tk()
root.geometry("880x700+0+0")
root.title("amusement park!!")
root.config(bg='black')
db=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db1=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db2=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db3=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")

db4=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db5=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db6=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db7=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")


db8=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db9=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db10=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")
db11=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")

db12=mysql.connector.connect(host="localhost",user="root",passwd="saksham026",database="online")

Tops = Frame(root,bg="black",width = 1400,height=50,relief=SUNKEN)
Tops.pack(side=TOP)
Tops.config(bg='black')

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
f1.config(bg='black')

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
f2.config(bg='black')

#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="welcome to fun park!!",fg="white",bd=10,anchor='w')
lblinfo.config(bg='black')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="white",anchor=W)
lblinfo.grid(row=1,column=0)
lblinfo.config(bg='black')

def Ref():
   
    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    dry=float(Cheese_burger2.get())
    
    codr= float(Drinks.get())
    water1= float(Cheese_burger3.get())
    dry1=float(Cheese_burger4.get())
    
    Ser_Charge=Service_Charge.get()
    
    costoflargefries = colfries*100
    costofburger = cob*50
    
    costoffilet = cochee*400
    costofcheeseburger = dry*450
    
    costofdrinks = water1*1300
    costofdrinks1 = dry1*1200
    
    costofmeal = str('%.2f'% (costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks+ costofdrinks1))
    PayTax=((costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks+ costofdrinks1)*0.33)
    Totalcost=(costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks+ costofdrinks1)

    waterc=colfries+cochee+water1
    dryc=cob+dry+dry1
    
    #tot=costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks+ costofdrinks1
    tot=float(costofmeal)
    OverAllCost=str( PayTax + Totalcost)
    PaidTax=str('%.2f'% PayTax)

    cost.set(costofmeal)
    Tax.set(PaidTax)
    Total.set(OverAllCost)
    
    mycursor=db.cursor()
    OverAllCost=Total.get()
    sql="insert into park_customers(below_5,below_10,above_10,day) values(%s,%s,%s,%s)"
    mycursor.execute(sql,(cof,cofi,codr,Ser_Charge))
    db.commit()
    db.close()
    print(mycursor.rowcount)
    mycursor.close()
    
    mycursor1=db1.cursor()
    mycursor1.execute("SELECT ticket_no from park_customers")
    myresult = mycursor1.fetchall()
    mycursor1.close()
    db1.commit()
    db1.close()
    
    for x in myresult:
      print(x[0])
      rand.set(x[0])

    no=float(rand.get())
    
    mycursor2=db2.cursor()
    sql1="insert into park_bills(ticket_no,price,tax,total) values(%s,%s,%s,%s)"
    mycursor2.execute(sql1,(no,tot,PayTax,Totalcost))
    db2.commit()
    db2.close()

    mycursor3=db3.cursor()
    sql2="insert into rides(ticket_no,water_rides,dry_rides) values(%s,%s,%s)"
    mycursor3.execute(sql2,(no,waterc,dryc))
    db3.commit()
    db3.close()
    
def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar(root)
choices = ['0','1','2','3','4','5','6','7','8']
Largefries.set('0')

Burger = StringVar(root)
choices1 = ['0','1','2','3','4','5','6','7','8']
Burger.set('0')

Filet = StringVar()

Cheese_burger = StringVar(root)
choices2 = ['0','1','2','3','4','5','6','7','8']
Cheese_burger.set('0')

Cheese_burger2 = StringVar(root)
choices3 = ['0','1','2','3','4','5','6','7','8']
Cheese_burger2.set('0')

Drinks = StringVar()

Cheese_burger3 = StringVar(root)
choices4 = ['0','1','2','3','4','5','6','7','8']
Cheese_burger3.set('0')

Cheese_burger4 = StringVar(root)
choices5 = ['0','1','2','3','4','5','6','7','8']
Cheese_burger4.set('0')

Subtotal = StringVar()
Total = StringVar()

Service_Charge = StringVar(root)
choices6 = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
Service_Charge.set('monday')

Tax = StringVar()
cost = StringVar()
msg=StringVar()

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="ticket no.",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
lblreference.config(bg='black')
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="below age 5",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)
lblfries.config(bg='black')

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="water rides",fg="steel blue",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
lblLargefries.config(bg='black')

popupMenu = OptionMenu(f1, Largefries, *choices)
popupMenu.grid(row = 3, column =0)

def change_dropdown(*args):
    print( Largefries.get() )
    
Largefries.trace('w', change_dropdown)

lblLargefries1 = Label(f1, font=( 'aria' ,16, 'bold' ),text="dry rides",fg="steel blue",bd=10,anchor='w')
lblLargefries1.grid(row=2,column=1)
lblLargefries1.config(bg='black')

popupMenu1 = OptionMenu(f1, Burger, *choices1)
popupMenu1.grid(row = 3, column =1)
 
def change_dropdown1(*args):
    print( Burger.get() )
    
Burger.trace('w', change_dropdown1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="below age 10",fg="steel blue",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=4,column=1)
lblFilet.config(bg='black')

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="water rides",fg="steel blue",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
lblCheese_burger.config(bg='black')

popupMenu2 = OptionMenu(f1, Cheese_burger, *choices2)
popupMenu2.grid(row = 6, column =0)

def change_dropdown2(*args):
    print( Cheese_burger.get() )
    
Cheese_burger.trace('w', change_dropdown2)

lblCheese_burger1 = Label(f1, font=( 'aria' ,16, 'bold' ),text="dry rides",fg="steel blue",bd=10,anchor='w')
lblCheese_burger1.grid(row=5,column=1)
lblCheese_burger1.config(bg='black')

popupMenu3 = OptionMenu(f1, Cheese_burger2, *choices3)
popupMenu3.grid(row = 6, column =1)       #some problem with col=1

def change_dropdown3(*args):
    print( Cheese_burger2.get() )
    
Cheese_burger2.trace('w', change_dropdown3)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="above age 10",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)
lblDrinks.config(bg='black')

lblCheese_burger2 = Label(f1, font=( 'aria' ,16, 'bold' ),text="water rides",fg="steel blue",bd=10,anchor='w')
lblCheese_burger2.grid(row=1,column=2)
lblCheese_burger2.config(bg='black')

popupMenu4 = OptionMenu(f1, Cheese_burger3, *choices4)
popupMenu4.grid(row = 2, column =2)

def change_dropdown4(*args):
    print( Cheese_burger3.get() )
    
Cheese_burger3.trace('w', change_dropdown4)

lblCheese_burger3 = Label(f1, font=( 'aria' ,16, 'bold' ),text="dry rides",fg="steel blue",bd=10,anchor='w') #first these both were 2 instead of 3
lblCheese_burger3.grid(row=1,column=3)
lblCheese_burger3.config(bg='black')

popupMenu5 = OptionMenu(f1, Cheese_burger4, *choices5)
popupMenu5.grid(row = 2, column =3)

def change_dropdown5(*args):
    print( Cheese_burger4.get() )
    
Cheese_burger4.trace('w', change_dropdown5)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue",bd=10,anchor='w')
lblcost.grid(row=4,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=4,column=3)
lblcost.config(bg='black')

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="select a day",fg="steel blue",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=2)
lblService_Charge.config(bg='black')

popupMenu6 = OptionMenu(f1, Service_Charge, *choices6)
popupMenu6.grid(row = 3, column =3)

def change_dropdown6(*args):
    print( Service_Charge.get() )
    
Service_Charge.trace('w', change_dropdown6)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=5,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=5,column=3)
lblTax.config(bg='black')

#erase afterwards
lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="",fg="steel blue",bd=10,anchor='w')
lblSubtotal.grid(row=6,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=6,column=3)
lblSubtotal.config(bg='black')

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=6,column=3)
lblTotal.config(bg='black')

#-----------------------------------------buttons------------------------------------------

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="book", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="category", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="water", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=4)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="dry", fg="black", anchor=W)
    lblinfo.grid(row=0, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="below age 5", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="below age 10", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="400", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="450", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=5)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="above age 10", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1300", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1200", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=5)

    roo.mainloop()

def can():
    print("")
    x=rand.get()

    mycursor9=db8.cursor()
    sql9="SELECT below_5 from park_customers where ticket_no=%s"
    mycursor9.execute(sql9,(x,))
    myresult = mycursor9.fetchall()
    mycursor9.close()
    db8.commit()
    db8.close()

    a=100
    for w in myresult:
        print(w[0])
        a=w[0]

    if(a!=100):    
        mycursor10=db9.cursor()
        sql10="delete from park_bills where ticket_no=%s"
        mycursor10.execute(sql10,(x,))
        db9.commit()
        db9.close()

        mycursor11=db10.cursor()
        sql11="delete from park_customers where ticket_no=%s"
        mycursor11.execute(sql11,(x,))
        db10.commit()
        db10.close()

        mycursor12=db11.cursor()
        sql12="delete from rides where ticket_no=%s"
        mycursor12.execute(sql12,(x,))
        db11.commit()
        db11.close()
    else:
        messagebox.showerror("Title", "ticket no. not found")
def booked():
    print("")
    Ser_Charge=Service_Charge.get()
    print(Ser_Charge)

    mycursor13=db12.cursor()
    sql13="select rides.water_rides,rides.dry_rides from park_customers inner join rides where rides.ticket_no=park_customers.ticket_no and park_customers.day= %s"
    mycursor13.execute(sql13,(Ser_Charge,))
    myresult = mycursor13.fetchall()
    a=0
    b=0
    for w in myresult:
        print(w[0])
        a+=w[0]
        b+=w[1]
    
    db12.commit()
    db12.close()
    a1=str(a)
    b1=str(b)
    messagebox.showerror("availability:","water rides "+a1+" dry rides "+b1)
    
    
def upd():
    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    dry=float(Cheese_burger2.get())
    
    codr= float(Drinks.get())
    water1= float(Cheese_burger3.get())
    dry1=float(Cheese_burger4.get())
    
    Ser_Charge=Service_Charge.get()
    print(Ser_Charge)
    a=str(Ser_Charge)
    
    costoflargefries = colfries*100
    costofburger = cob*50
    
    costoffilet = cochee*400
    costofcheeseburger = dry*450
    
    costofdrinks = water1*1300
    costofdrinks1 = dry1*1200
    
    costofmeal = str('%.2f'% (costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks+ costofdrinks1))
    PayTax=((costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks+ costofdrinks1)*0.33)
    Totalcost=(costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks+ costofdrinks1)

    waterc=colfries+cochee+water1
    dryc=cob+dry+dry1
    
    #tot=costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks+ costofdrinks1
    tot=float(costofmeal)
    OverAllCost=str( PayTax + Totalcost)
    PaidTax=str('%.2f'% PayTax)

    cost.set(costofmeal)
    Tax.set(PaidTax)
    Total.set(OverAllCost)
    print("")
    x=rand.get()

    
    mycursor8=db7.cursor()
    sql8="SELECT below_5 from park_customers where ticket_no=%s"
    mycursor8.execute(sql8,(x,))
    myresult = mycursor8.fetchall()
    mycursor8.close()
    db7.commit()
    db7.close()

    a=1
    for w in myresult:
        print(w[0])
        a=w[0]

    if(a!=1):    
        mycursor5=db4.cursor()
        sql5="update park_bills set price=%s,tax=%s,total=%s where ticket_no=%s"
        mycursor5.execute(sql5,(tot,PayTax,Totalcost,x))
        db4.commit()
        db4.close()

        mycursor6=db5.cursor()
        sql6="update park_customers set below_5=%s,below_10=%s,above_10=%s,day=%s where ticket_no=%s"
        mycursor6.execute(sql6,(cof,cofi,codr,a,x))
        db5.commit()
        db5.close()

        mycursor7=db6.cursor()
        sql7="update rides set water_rides=%s,dry_rides=%s where ticket_no=%s"
        mycursor7.execute(sql7,(waterc,dryc,x))
        db6.commit()
        db6.close()
    else:
        messagebox.showerror("Title", "ticket no. not found")
        
def play():
    print("")
    os.system('restaurant.py')

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="ticket details", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="cancel", bg="powder blue",command=can)
btnprice.grid(row=8, column=0)

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="bookings", bg="powder blue",command=booked)
btnprice.grid(row=8, column=1)

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="food order", bg="powder blue",command=play)
btnprice.grid(row=8, column=2)

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="update", bg="powder blue",command=upd)
btnprice.grid(row=8, column=3)


root.mainloop()
