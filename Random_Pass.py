from tkinter import *
import random

window = Tk()
window.title("Random Pass")

def random_pass():
    pass_dict = {'Password Length(min 12): ': range(12, 100),
                 'Include Symbols(y/n): ': '@#$%',
                 'Include Numbers(y/n): ': '1234567890',
                 'Include Lowercase Characters(y/n): ': 'qwertyuioplkjhgfdsazxcvbnm',
                 'Include Uppercase Characters(y/n): ': 'QWERTYUIOPLKJHGFDSAZXCVBNM',
                 'Include Similar Characters(y/n): ': '',
                 'Include Ambiguous Characters(y/n): ': '(){}[]/\'"`~,:.<>'}
    x = list(pass_dict.items())
    # input password length
    pass_len = int(e1_value.get())

    password = ''

    if (var1.get())==1:
        password += x[1][1]

    if (var2.get())==1:
        password += x[2][1]

    if (var3.get())==1:
        password += x[3][1]

    if (var4.get())==1:
        password += x[4][1]

    if (var5.get())==1:
        password += x[5][1]

    if (var6.get())==1:
        password += x[6][1]

    final_pass = ''
    for i in range(pass_len):
        c = random.choice(password)
        while ((var5.get()== 0) and (c not in password)):
            c = random.choice(password)
        final_pass += c

    t1.insert(END, final_pass)


labelText=StringVar()
labelText.set("Password Length")
labelDir=Label(window, textvariable=labelText, height=1)
labelDir.grid(row=0,column=0)

e1_value=IntVar()
e1=Entry(window,textvariable=e1_value,width=50)
e1.grid(row=0,column=5)

var1 = IntVar()
Checkbutton(window, text="Include Symbols", variable=var1).grid(row=1, sticky=W)

var2 = IntVar()
Checkbutton(window, text="Include Numbers", variable=var2).grid(row=2, sticky=W)

var3 = IntVar()
Checkbutton(window, text="Include Lowercase Characters", variable=var3).grid(row=3, sticky=W)

var4 = IntVar()
Checkbutton(window, text="Include Uppercase Characters", variable=var4).grid(row=4, sticky=W)

var5 = IntVar()
Checkbutton(window, text="Include Similar Characters", variable=var5).grid(row=5, sticky=W)

var6 = IntVar()
Checkbutton(window, text="Include Ambiguous Characters", variable=var6).grid(row=6, sticky=W)

b1=Button(window,text="Generate",command=random_pass)
b1.grid(row=7,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=7,column=0)


window.mainloop()
