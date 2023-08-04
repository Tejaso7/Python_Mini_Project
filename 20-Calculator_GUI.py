from tkinter import *
from tkinter import messagebox
import math

screen=Tk()
screen.title('My calculator')
screen.configure(background='red')
screen.maxsize(width=453,height=490)
screen.minsize(width=358,height=490)
screen.geometry('358x490')

def click(number):
    global operator
    operator+=str(number)
    tex.set(operator)
def clear():
    global operator
    operator=' '
    tex.set(operator)
def equal():
    global operator
    try:
        result=eval(operator)
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification','Try again something is wrong',parent=screen)

def cmsin():
    global operator
    try:
        result=math.sin(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification','Try again something is wrong',parent=screen)

def cmcos():
    global operator
    try:
        result=math.cos(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification','Try again something is wrong',parent=screen)

def cmtan():
    global operator
    try:
        result=math.tan(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification','Try again something is wrong',parent=screen)

def cmsqrt():
    global operator
    try:
        result=math.sqrt(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification','Try again something is wrong',parent=screen)

def cmlog():
    global operator
    try:
        result=math.log(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification','Try again something is wrong',parent=screen)
tex=StringVar()
operator=' '
entry1=Entry(screen,bg='orange',font=('arial',20,'italic bold'),bd='30',justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)
btn7=Button(screen,text='7',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(7)
            ,activebackground='green',activeforeground='white',bg='powder blue')
btn7.grid(row=1,column=0)

btn8=Button(screen,text='8',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(8),
            activebackground='green',activeforeground='white',bg='powder blue')
btn8.grid(row=1,column=1)
btn9=Button(screen,text='9',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(9),activebackground='green',activeforeground='white',bg='powder blue')
btn9.grid(row=1,column=2)
btnadd=Button(screen,text='+',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click('+'),activebackground='green',activeforeground='white',bg='powder blue')
btnadd.grid(row=1,column=3)

btn4=Button(screen,text='4',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(4),activebackground='green',activeforeground='white',bg='powder blue')
btn4.grid(row=2,column=0)
btn5=Button(screen,text='5',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(5),activebackground='green',activeforeground='white',bg='powder blue')
btn5.grid(row=2,column=1)
btn6=Button(screen,text='6',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(6),activebackground='green',activeforeground='white',bg='powder blue')
btn6.grid(row=2,column=2)
btnsub=Button(screen,text='-',font=('arial',20,'italic bold'),bd='8',padx=20,pady=16,command=lambda:click('-'),activebackground='green',activeforeground='white',bg='powder blue')
btnsub.grid(row=2,column=3)

btn1=Button(screen,text='1',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(1),activebackground='green',activeforeground='white',bg='powder blue')
btn1.grid(row=3,column=0)
btn2=Button(screen,text='2',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(2),activebackground='green',activeforeground='white',bg='powder blue')
btn2.grid(row=3,column=1)
btn3=Button(screen,text='3',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(3),activebackground='green',activeforeground='white',bg='powder blue')
btn3.grid(row=3,column=2)
btnmul=Button(screen,text='x',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click('*'),activebackground='green',activeforeground='white',bg='powder blue')
btnmul.grid(row=3,column=3)

btn0=Button(screen,text='0',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click(0),activebackground='green',activeforeground='white',bg='powder blue')
btn0.grid(row=4,column=0)
btnclear=Button(screen,text='c',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=clear,activebackground='green',activeforeground='white',bg='powder blue')
btnclear.grid(row=4,column=1)
btnequal=Button(screen,text='=',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=equal,activebackground='green',activeforeground='white',bg='powder blue')
btnequal.grid(row=4,column=2)
btndiv=Button(screen,text='/',font=('arial',20,'italic bold'),bd='8',padx=16,pady=16,command=lambda:click('/'),activebackground='green',activeforeground='white',bg='powder blue')
btndiv.grid(row=4,column=3)

#################Advanced calculations
btnsin=Button(screen,text='sin',font=('arial',15,'italic bold'),bd='8',padx=14,pady=21,command=cmsin,activebackground='green',activeforeground='white',bg='powder blue')
btnsin.grid(row=0,column=4)
btncos=Button(screen,text='cos',font=('arial',15,'italic bold'),bd='8',padx=16,pady=21,command=cmcos,activebackground='green',activeforeground='white',bg='powder blue')
btncos.grid(row=1,column=4)
btntan=Button(screen,text='tan',font=('arial',15,'italic bold'),bd='8',padx=16,pady=21,command=cmtan,activebackground='green',activeforeground='white',bg='powder blue')
btntan.grid(row=2,column=4)
btnsqrt=Button(screen,text='sqrt',font=('arial',15,'italic bold'),bd='8',padx=14,pady=21,command=cmsqrt,activebackground='green',activeforeground='white',bg='powder blue')
btnsqrt.grid(row=3,column=4)
btnlog=Button(screen,text='log',font=('arial',15,'italic bold'),bd='8',padx=18,pady=25,command=cmlog,activebackground='green',activeforeground='white',bg='powder blue')
btnlog.grid(row=4,column=4)
################### Binding


screen.mainloop()
