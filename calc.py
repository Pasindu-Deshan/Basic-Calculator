from tkinter import *
import numpy as np
from tkinter import messagebox

root = Tk()
root.title("Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row =  1, column = 0, columnspan = 3, padx = 10, pady = 10)

var = StringVar()
l = Label(root, width = 5, textvariable = var)
l.grid(row = 1, column = 3)

def button_click(number):
    current =  e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    index_check(first_number)
    global f_num
    global math
    math = "add"
    try:
        f_num = int(first_number)
        var.set("+")
        e.delete(0, END)
    except ValueError:
        return

def button_equal():
    second_number = e.get()
    try:
        second_number = int(second_number)
        var.set(" ")
        e.delete(0, END)
        
        if math == "add":
            e.insert(0, f_num + second_number)
        if math == "sub":
            e.insert(0, f_num - second_number)
        if math == "mul":
            e.insert(0, f_num * second_number)
        if math == "div":
            e.insert(0, f_num / second_number)
        if math == "pow":
            e.insert(0, pow(f_num, second_number))
        if math == "remainder":
            e.insert(0, f_num % second_number)
    except ValueError:
        return
    
def button_sub():
    first_number = e.get()
    index_check(first_number)
    global f_num
    global math
    math = "sub"
    try:
        f_num = int(first_number)
        var.set("-")
        e.delete(0, END)
    except ValueError:
        return
    
def button_mul():
    first_number = e.get()
    index_check(first_number)
    global f_num
    global math
    math = "mul"
    try:
        f_num = int(first_number)
        var.set("x")
        e.delete(0, END)
    except ValueError:
        return
    
def button_div():
    first_number = e.get()
    index_check(first_number)
    global f_num
    global math
    math = "div"
    try:
        f_num = int(first_number)
        var.set("/")
        e.delete(0, END)
    except ValueError:
        return
    
def button_pow():
    first_number = e.get()
    index_check(first_number)
    global f_num
    global math
    math = "pow"
    try:
        f_num = int(first_number)
        var.set("^")
        e.delete(0, END)
    except ValueError:
        return
    
def button_back():
    first_number = e.get()
    num = first_number[0: len(first_number)-1]
    e.delete(0, END)
    e.insert(0, num)

def button_remainder():
    first_number = e.get()
    index_check(first_number)
    global f_num
    global math
    math = "remainder"
    try:
        f_num = int(first_number)
        var.set("%")
        e.delete(0, END)
    except ValueError:
        return
    
def button_root():
    first_number = e.get()
    index_check(first_number)
    try:
        f_num = int(first_number)
        var.set("^")
        e.delete(0, END)
        f_num = np.sqrt(f_num)
        f_num_res = np.round(f_num, decimals = 4)
        e.insert(0, f_num_res)
    except ValueError:
        return
    
def button_exit():
    root.destroy()

def index_check(first_number):
    if first_number != '':
        try:
            checkInt = int(first_number)
        except:
            responce = messagebox.showerror("Type Error", "Can't Insert Charactors")
            e.delete(0, END)

            #Binary Calculator
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def binary_click(number):
    current =  b.get()
    b.delete(0, END)
    b.insert(0, str(current) + str(number))
    
def button_binary():
    global binaryWin
    binaryWin = Tk()
    binaryWin.title("Binary Calculator")

    global b
    b = Entry(binaryWin, width = 35, borderwidth = 5)
    b.grid(row =  0, column = 0, columnspan = 3, padx = 10, pady = 10)
    
    button_1 = Button(binaryWin, text = "1", padx = 60, pady = 10, command = lambda: binary_click(1))
    button_0 = Button(binaryWin, text = "0", padx = 60, pady = 10, command = lambda: binary_click(0))

    button_add = Button(binaryWin, text = "+", padx = 60, pady = 10, command = binary_add)
    button_sub = Button(binaryWin, text = "-", padx = 60, pady = 10, command = binary_sub)
    button_mul = Button(binaryWin, text = "x", padx = 60, pady = 10, command = binary_mul)
    button_div = Button(binaryWin, text = "/", padx = 60, pady = 10, command = binary_div)
    button_pow = Button(binaryWin, text = "^", padx= 60, pady = 10, command = binary_pow)
    button_equal = Button(binaryWin, text = "=", padx= 60, pady = 10, command = binary_equal)
    button_back = Button(binaryWin, text = "<", padx= 60, pady = 10, command = binary_back)
    button_exit = Button(binaryWin, text = "Exit", padx= 54, pady = 10, command = binary_exit)
    button_clear = Button(binaryWin, text = "C", padx = 128, pady = 10, command = binary_clear)
    
    button_1.grid(row = 1, column = 0)
    button_0.grid(row = 1, column = 1)
    
    button_add.grid(row = 2, column = 0)
    button_sub.grid(row = 2, column = 1)
    button_mul.grid(row = 3, column = 0)
    button_div.grid(row = 3, column = 1)
    button_pow.grid(row = 4, column = 0)
    button_equal.grid(row = 4, column = 1)
    button_back.grid(row = 5, column = 0)
    button_exit.grid(row = 5, column = 1)
    button_clear.grid(row = 6, column = 0, columnspan = 2)
    
    binaryWin.mainloop()

def binary_add():
    first_number = b.get()
    checkError(first_number)
    global f_num
    global math
    math = "binary_add"
    f_num = first_number[::-1]
    b.delete(0, END)

def binary_sub():
    first_number = b.get()
    checkError(first_number)
    global f_num
    global math
    math = "binary_sub"
    f_num = first_number[::-1]
    b.delete(0, END)
    
def binary_mul():
    first_number = b.get()
    checkError(first_number)
    global f_num
    global math
    math = "binary_mul"
    f_num = first_number[::-1]
    b.delete(0, END)
    
def binary_div():
    first_number = b.get()
    checkError(first_number)
    global f_num
    global math
    math = "binary_div"
    f_num = first_number[::-1]
    b.delete(0, END)
    
def binary_pow():
    first_number = b.get()
    checkError(first_number)
    global f_num
    global math
    math = "binary_pow"
    f_num = first_number[::-1]
    b.delete(0, END)
    
def binaryCalAnswer(total):
    value = []
    c = True
    while c:
        num = total
        value.append(total%2)
        total = total//2
        if num == 0:
            res_val = value[::-1]
            res_val = ''.join(map(str, res_val))
            res_val = res_val.replace(" ", "")
            b.insert(0, res_val[1::])
            c = False
        if num == 1:
            value.append(1)
            res_val = value[::-1]
            res_val = ''.join(map(str, res_val))
            res_val = res_val.replace(" ", "")
            b.insert(0, res_val[1::])
            c = False
            
def binary_equal():
    total_f = 0
    total_s = 0
    current = 0
    num = 0
    second_number = b.get()
    s_num = second_number[::-1]
    b.delete(0, END)
    for i in range(len(f_num)):
        current = pow(2,i) * int(f_num[i])
        total_f = total_f + current
    for i in range(len(s_num)):
        current = pow(2,i) * int(s_num[i])
        total_s = total_s + current
    if math == "binary_add":
        total = total_f + total_s
        binaryCalAnswer(total)
    if math == "binary_sub":
        total = total_f - total_s
        binaryCalAnswer(total)
    if math ==  "binary_mul":
        total = total_f * total_s
        binaryCalAnswer(total)
    if math == "binary_div":
        total = total_f // total_s
        binaryCalAnswer(total)
    if math == "binary_pow":
        total = pow(total_f, total_s)
        binaryCalAnswer(total)
   
def binary_back():
    first_number = b.get()
    l_num = len(first_number)
    b.delete(0, END)
    b.insert(0, first_number[0:l_num - 1])

def binary_clear():
    b.delete(0, END)

def binary_exit():
    binaryWin.destroy()

def checkError(first_number):
    if first_number != '':
        try:
            checkInt = int(first_number)
        except:
            responce = messagebox.showerror("Type Error", "Insert only 1 or 0")
            b.delete(0, END)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

            #Octal Calculator
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def octal_click(number):
    current =  c.get()
    c.delete(0, END)
    c.insert(0, str(current) + str(number))
    
def button_octal():
    global octalWin
    octalWin = Tk()
    octalWin.title("Octal Calculator")

    global c
    c = Entry(octalWin, width = 35, borderwidth = 5)
    c.grid(row =  0, column = 0, columnspan = 3, padx = 10, pady = 10)
    
    button_1 = Button(octalWin, text = "1", padx = 60, pady = 10, command = lambda: octal_click(1))
    button_0 = Button(octalWin, text = "0", padx = 60, pady = 10, command = lambda: octal_click(0))

    button_add = Button(octalWin, text = "+", padx = 60, pady = 10, command = octal_add)
    button_sub = Button(octalWin, text = "-", padx = 60, pady = 10, command = octal_sub)
    button_mul = Button(octalWin, text = "x", padx = 60, pady = 10, command = octal_mul)
    button_div = Button(octalWin, text = "/", padx = 60, pady = 10, command = octal_div)
    button_pow = Button(octalWin, text = "^", padx= 60, pady = 10, command = octal_pow)
    button_equal = Button(octalWin, text = "=", padx= 60, pady = 10, command = octal_equal)
    button_back = Button(octalWin, text = "<", padx= 60, pady = 10, command = octal_back)
    button_exit = Button(octalWin, text = "Exit", padx= 54, pady = 10, command = octal_exit)
    button_clear = Button(octalWin, text = "C", padx = 128, pady = 10, command = octal_clear)
    
    button_1.grid(row = 1, column = 0)
    button_0.grid(row = 1, column = 1)
    
    button_add.grid(row = 2, column = 0)
    button_sub.grid(row = 2, column = 1)
    button_mul.grid(row = 3, column = 0)
    button_div.grid(row = 3, column = 1)
    button_pow.grid(row = 4, column = 0)
    button_equal.grid(row = 4, column = 1)
    button_back.grid(row = 5, column = 0)
    button_exit.grid(row = 5, column = 1)
    button_clear.grid(row = 6, column = 0, columnspan = 2)

    octalWin.mainloop()

def octal_add():
    first_number = c.get()
    checkOctalError(first_number)
    global f_num
    global math
    math = "octal_add"
    f_num = first_number[::-1]
    c.delete(0, END)

def octal_sub():
    first_number = c.get()
    checkOctalError(first_number)
    global f_num
    global math
    math = "octal_sub"
    f_num = first_number[::-1]
    c.delete(0, END)
    
def octal_mul():
    first_number = c.get()
    checkOctalError(first_number)
    global f_num
    global math
    math = "octal_mul"
    f_num = first_number[::-1]
    c.delete(0, END)
    
def octal_div():
    first_number = c.get()
    checkOctalError(first_number)
    global f_num
    global math
    math = "octal_div"
    f_num = first_number[::-1]
    c.delete(0, END)
    
def octal_pow():
    first_number = c.get()
    checkOctalError(first_number)
    global f_num
    global math
    math = "octal_pow"
    f_num = first_number[::-1]
    c.delete(0, END)
    
def octalCalAnswer(total):
    value = []
    t = True
    while t:
        num = total
        value.append(total%8)
        total = total//8
        if num == 0:
            res_val = value[::-1]
            res_val = ''.join(map(str, res_val))
            res_val = res_val.replace(" ", "")
            c.insert(0, res_val[1::])
            t = False
        if num == 1:
            value.append(1)
            res_val = value[::-1]
            res_val = ''.join(map(str, res_val))
            res_val = res_val.replace(" ", "")
            c.insert(0, res_val[1::])
            t = False
            
def octal_equal():
    total_f = 0
    total_s = 0
    current = 0
    num = 0
    second_number = c.get()
    s_num = second_number[::-1]
    c.delete(0, END)
    for i in range(len(f_num)):
        current = pow(8,i) * int(f_num[i])
        total_f = total_f + current
    for i in range(len(s_num)):
        current = pow(8,i) * int(s_num[i])
        total_s = total_s + current
    if math == "octal_add":
        total = total_f + total_s
        octalCalAnswer(total)
    if math == "octal_sub":
        total = total_f - total_s
        octalCalAnswer(total)
    if math ==  "octal_mul":
        total = total_f * total_s
        octalCalAnswer(total)
    if math == "octal_div":
        total = total_f // total_s
        octalCalAnswer(total)
    if math == "octal_pow":
        total = pow(total_f, total_s)
        octalCalAnswer(total)
            
def octal_back():
    first_number = c.get()
    l_num = len(first_number)
    c.delete(0, END)
    c.insert(0, first_number[0:l_num - 1])

def octal_clear():
    c.delete(0, END)

def octal_exit():
    octalWin.destroy()

def checkOctalError(first_number):
    if first_number != '':
        try:
            checkInt = int(first_number)
        except:
            responce = messagebox.showerror("Type Error", "Insert only 1 or 0")
            c.delete(0, END)
            
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
            
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))

button_add = Button(root, text = "+", padx = 40, pady = 20, command = button_add)
button_sub = Button(root, text = "-", padx = 40, pady = 20, command = button_sub)
button_mul = Button(root, text = "x", padx = 40, pady = 20, command = button_mul)
button_div = Button(root, text = "/", padx = 40, pady = 20, command = button_div)
button_pow = Button(root, text = "^", padx= 40, pady = 20, command = button_pow)
button_remainder = Button(root, text = "%", padx = 40, pady = 20, command = button_remainder)
button_root = Button(root, text = "Rt", padx = 38, pady = 20, command = button_root)

button_equal = Button(root, text = "=", padx = 40, pady = 20, command = button_equal)
button_clear = Button(root, text = "C", padx = 40, pady = 20, command = button_clear)
button_back = Button(root, text = "Back", padx = 80, pady = 20, command = button_back)
button_exit = Button(root, text = "Exit", padx = 35, pady = 20, command = button_exit)

button_binary = Button(root, text = "Binary", padx = 20, pady = 4, command = button_binary)
button_octal = Button(root, text = "Octal", padx = 20, pady = 4, command = button_octal)

button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)

button_0.grid(row = 5 , column = 0)

button_add.grid(row = 2, column = 3)
button_sub.grid(row = 3, column = 3)
button_mul.grid(row = 4, column = 3)
button_div.grid(row = 5, column = 3)
button_pow.grid(row = 6, column = 3)
button_remainder.grid(row = 6, column = 2)
button_root.grid(row = 7, column = 3)

button_equal.grid(row = 5, column = 1)
button_clear.grid(row = 5, column = 2)
button_back.grid(row = 6, column = 0, columnspan = 2)
button_exit.grid(row = 7, column = 2)

button_binary.grid(row = 0, column = 0)
button_octal.grid(row = 0, column = 1)

root.mainloop()

