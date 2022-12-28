from tkinter import *
from functools import reduce

root = Tk()
root.title('Simple Calculator')
root.iconbitmap('calc_icon.ico')

# create the console screen, using entry
operation_scr = Entry(root, width=20)
operation_scr.grid(row=0, column=0, columnspan=3)
console_scr = Entry(root, width=30, borderwidth=12)
console_scr.grid(row=1, column=0, columnspan=3, pady=15)


#Global variable used for checking if a operatoin was asked to be done so that when we click on another button it clears the Answer currently shown on the ENTRY widget
global set_1
set_1 = set()

#function used for inputing button into the console/entry widget
def button_click(number):
    if set_1:
        operation_scr.delete(0, END)
        console_scr.delete(0, END)
        console_scr.insert(END, number)
        set_1.clear()
    else:
        console_scr.insert(END,number)

#Global list variable to do concatenations in real time of operations asked by the user, (stores numbers inputed by the user to do operation in the --> def operatoion function
global list_1
list_1 = []
#Global list variable to do concatenation in real time of operations asked by the user, (stores operands inputed by the user to calcuate operating in --> def operation function
global list_2
list_2 = []
#to check if the previouse was a '='
global list_3
list_3 = []

# used for the clear button to erase all previouse/current operation that's being done on the screen to start a new operation.
def button_clear():
    console_scr.delete(0, END)
    operation_scr.delete(0, END)
    list_1.clear()
    list_2.clear()
    list_3.clear()

#function created to concatenate operations inputed by the user. (note: improvement could be useing somme try and except to avoid error logs)
def operation(operand):
    list_2.append(operand)
    list_3.append(operand)
    if len(list_3) >= 3:
        if list_3[-2] == '=':
            # clearing the console screen so next concatenation can be done.
            console_scr.delete(0, END)
        else:
            pass
    if console_scr.get():
        list_1.append(int(console_scr.get()))
        console_scr.delete(0, END)
        if len(list_2) > 1:
            cond = False
            # do concatentions depeding on the operand that was last asked for to do concatentions
            if list_2[-1] == '+' and operand != '=' and len(list_2) <= 1 or operand == '=' and list_2[-2] == '+' or list_2[-2] == '+' and operand != '=' and len(list_2) >= 1 :
                total = sum(list_1)
                cond = True
            elif list_2[-1] == '*' and operand != '=' and len(list_2) <= 1 or operand == '=' and list_2[-2] == '*' or list_2[-2] == '*' and operand != '=' and len(list_2) >= 1:
                total = reduce((lambda x, y: x * y), list_1)
                cond = True
            elif list_2[-1] == '-' and operand != '=' and len(list_2) <= 1 or operand == '=' and list_2[-2] == '-'  or list_2[-2] == '-' and operand != '=' and len(list_2) >= 1:
                total = reduce((lambda x, y: x - y), list_1)
                cond = True
            elif list_2[-1] == '/' and operand != '='  and len(list_2) <= 1 or operand == '=' and list_2[-2] == '/' or list_2[-2] == '/' and operand != '=' and len(list_2) >= 1:
                total = reduce((lambda x, y: x / y), list_1)
                cond = True
            concatenation = str(list_1[-2]) + str(list_2[-2]) + str(list_1[-1]) + ' = ' + str(total)
            list_1.clear()
            if operand == '=':
                list_2.pop()
            # used to input total value into the screen, and make set condition true so that the total value gets deleted when a button is clicked on after total has been inputed to the screen
            if cond is True:
                # created to show the current operation that was done to the user on the entry widget(console screen)
                #concatenation = str(list_1[-2]) + str(list_2[-2]) + str(list_1[-1]) + ' = ' + str(total)
                # actually printing the concatention variable out to them screen for the user to see
                console_scr.insert(0, total)
                operation_scr.insert(0, concatenation)
                list_1.append(total)
                set_1.add(4)

  # ---> extra repeated work managed to remove XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        #Note: went back after some review, made some adjustments to shorten reapted works and extra lines of code
        #else:
            # created to do conatenations in the case where the user only wants to do a simple calcuation: 2 + 2 =4
            #if list_2[-1] == '+':
                #total = sum(list_1)
            #elif list_2[-1] == '*':
                #total = reduce((lambda x, y: x * y), list_1)
            #elif list_2[-1] == '-':
                #total = reduce((lambda x, y: x - y), list_1)
            #elif list_2[-1] == '/':
                #total = reduce((lambda x, y: x / y), list_1)
            # used to input total value into the screen, and make set condition true so that the total value gets deleted when a button is clicked on after total has been inpute
            #console_scr.insert(0, total)
            #list_1.clear()
            #list_1.append(total)
            #set_1.add(4)
                            #  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX <---------- repearted work #



#Define buttons for calculator and put them on the screen using the grid method
button_1 = Button(root, text='1', command=lambda: button_click(1), padx=25, pady=15).grid(row=4, column=0)
button_2 = Button(root, text='2', command=lambda: button_click(2), padx=25, pady=15).grid(row=4, column=1)
button_3 = Button(root, text='3', command=lambda: button_click(3), padx=25, pady=15).grid(row=4, column=2)
button_4 = Button(root, text='4', command=lambda: button_click(4), padx=25, pady=15).grid(row=3, column=0)
button_5 = Button(root, text='5', command=lambda: button_click(5), padx=25, pady=15).grid(row=3, column=1)
button_6 = Button(root, text='6', command=lambda: button_click(6), padx=25, pady=15).grid(row=3, column=2)
button_7 = Button(root, text='7', command=lambda: button_click(7), padx=25, pady=15).grid(row=2, column=0)
button_8 = Button(root, text='8', command=lambda: button_click(8), padx=25, pady=15).grid(row=2, column=1)
button_9 = Button(root, text='9', command=lambda: button_click(9), padx=25, pady=15).grid(row=2, column=2)
button_0 = Button(root, text='0', command=lambda: button_click(0), padx=25, pady=15).grid(row=5, column=0)
button_C = Button(root, text='clear', command=lambda: button_clear(), padx=50, pady=15).grid(row=5, column= 1, columnspan=2)
button_E = Button(root, text='=', command=lambda: operation('='), padx=18.5, pady=15).grid(row=1, column= 4)
button_A = Button(root, text='+', command=lambda: operation('+'), padx=17.5, pady=15).grid(row=2, column= 4)
button_S = Button(root, text='-', command=lambda: operation('-'), padx=20, pady=15).grid(row=3, column= 4)
button_M = Button(root, text='*', command=lambda: operation('*'), padx=20, pady=15).grid(row=4, column= 4)
button_D = Button(root, text='/', command=lambda: operation('/'), padx=20, pady=15).grid(row=5, column= 4)


#allows from mouse to move on the GUI and for the GUI TO continue running
root.mainloop()
