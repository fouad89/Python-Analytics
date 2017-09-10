from tkinter import *
window=Tk()
file=open('user_gui.txt','a+')
def add():
    file.write(entry.get()+'\n') #to get file from window entry
    entry.delete(0,END)
def save():
    global file
    file.close()
    file=open('user_gui.txt','a+')
def close():
    file.close
    window.destroy()
'''
Text entry field
'''
user_value = StringVar()
entry=Entry(window,textvariable=user_value)
entry.pack()
entry.grid(row=0,column=0)

'''
Add line button
'''
button_add=Button(window, text='Add Line', command=add)
button_add.grid(row=0,column=1)

button_save=Button(window, text='Save Changes', command=save)
button_save.grid(row=0,column=2)

button_close=Button(window, text='Save&Close', command=close)
button_close.grid(row=0,column=3)

window.mainloop()