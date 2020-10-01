from tkinter import *
root = Tk()

root.iconbitmap(r'C:\Users\Sumit kosta\Documents\Python Project\Calculator\icn.ico')
value = ""
def binary(num): 
    if num > 1: 
        DecimalToBinary(num // 2) 
    scvalue.set(num % 2)
    screen.update()    
    print(num % 2, end = '')
     
def click(event):
    text=event.widget.cget("text")
    if text== "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
            
        scvalue.set(value)
        screen.update()
    
    elif text== "C":
        scvalue.set("")
        screen.update()
        
    elif text== "Find Binary":
        num = eval(scvalue.get())
        num = str(num)
        if num> "1":
            num = int(num)
            binary = bin(num)
            binary = binary[2:len(binary)]
        scvalue.set(binary)
        screen.update()
        

        
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

  
root.title("Calculator")
root.geometry("450x800")
root['bg'] = '#232324'
root.minsize(450, 800)
calculator = Label(text="Thanks CodeWithHarry",bg='#232324',fg='white',font=('calibre',30,'bold')).pack(fill='x',padx=5)
scvalue = StringVar()
screen = Entry(root,bg='#616163',fg='white',textvariable=scvalue,relief=SUNKEN,font=('calibre',30,'bold'))
screen.pack(fill="x" ,ipadx = 30, ipady = 6,padx=10,pady=10)

f1 = Frame(root,bg='#232324')
f1.pack(fill='x',pady=5,padx=10)

button1 = Button(f1,text='1',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button1.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button1.bind("<Button-1>",click)

button2 = Button(f1,text='2',activebackground='grey', bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button2.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button2.bind("<Button-1>",click)

button3 = Button(f1,text='3',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button3.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button3.bind("<Button-1>",click)

buttonPlus = Button(f1,text='+',activebackground='grey', bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
buttonPlus.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
buttonPlus.bind("<Button-1>",click)





f2 = Frame(root,bg='#232324')
f2.pack(fill='x',pady=5,padx=10)
button4 = Button(f2,text='4',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button4.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button4.bind("<Button-1>",click)

button5 = Button(f2,text='5',activebackground='grey', bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button5.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button5.bind("<Button-1>",click)

button6 = Button(f2,text='6',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button6.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button6.bind("<Button-1>",click)

buttonminus = Button(f2,text='-',activebackground='grey', bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
buttonminus.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
buttonminus.bind("<Button-1>",click)



f3 = Frame(root,bg='#232324')
f3.pack(fill='x',pady=5,padx=10)
button7 = Button(f3,text='7',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button7.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button7.bind("<Button-1>",click)

button8 = Button(f3,text='8',activebackground='grey', bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button8.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button8.bind("<Button-1>",click)

button9 = Button(f3,text='9',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button9.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button9.bind("<Button-1>",click)

buttonmultiply = Button(f3,text='*',activebackground='grey', bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
buttonmultiply.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
buttonmultiply.bind("<Button-1>",click)




f4 = Frame(root,bg='#232324')
f4.pack(fill='x',pady=5,padx=10)
button0 = Button(f4,text='0',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button0.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button0.bind("<Button-1>",click)

button00 = Button(f4,text='.',activebackground='grey', bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
button00.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
button00.bind("<Button-1>",click)

buttonpercentage = Button(f4,text='%',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
buttonpercentage.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
buttonpercentage.bind("<Button-1>",click)

buttondivision = Button(f4,text='/',activebackground='grey', bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
buttondivision.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
buttondivision.bind("<Button-1>",click)




f5 = Frame(root,bg='#232324')
f5.pack(fill='x',pady=5,padx=10)
buttonequal = Button(f5,text='=',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
buttonequal.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
buttonequal.bind("<Button-1>",click)

buttonclear = Button(f5,text='C',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
buttonclear.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
buttonclear.bind("<Button-1>",click)

f6 = Frame(root,bg='#232324')
f6.pack(fill='x',pady=5,padx=10)
buttonbinary = Button(f6,text='Find Binary',activebackground='grey' ,bg='black', fg='white',font=('calibre',25,'bold'),borderwidth=0)
buttonbinary.pack(side=LEFT, ipadx=5,ipady=5, padx=5,pady=5,fill="x",expand=True)
buttonbinary.bind("<Button-1>",click)



root.mainloop()



