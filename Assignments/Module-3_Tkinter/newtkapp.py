import tkinter
from tkinter import ttk

tk=tkinter.Tk()
tk.title("MyApp")
tk.geometry("500x500")
tk.config(bg="skyblue")

#flbl=tkinter.Label(text="Firstname:").pack()
#llbl=tkinter.Label(text="Lastname:").pack()

#flbl=tkinter.Label(text="Firstname:").place(x=0,y=0)
#llbl=tkinter.Label(text="Lastname:").place(x=0,y=30)

flbl=tkinter.Label(text="Firstname:",bg="skyblue",fg='red',font='Constantia 15 bold')
flbl.grid(row=0,column=0,sticky='w')
llbl=tkinter.Label(text="Lastname:",bg="skyblue",fg='red',font='Constantia 15 bold')
llbl.grid(row=1,column=0,sticky='w')

ftxt=tkinter.Entry()
ftxt.grid(row=0,column=1,sticky='w')

ltxt=tkinter.Entry()
ltxt.grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0,text="Male",bg="skyblue",fg='red',font='Constantia 15 bold').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text="Female",bg="skyblue",fg='red',font='Constantia 15 bold').grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Gujarati",bg="skyblue",fg='red',font='Constantia 15 bold').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Hindi",bg="skyblue",fg='red',font='Constantia 15 bold').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="English",bg="skyblue",fg='red',font='Constantia 15 bold').grid(row=5,column=0,sticky='w')

city=["Rajkot","Ahmedabad","Baroda","Surat","Jamnagar"]
ttk.Combobox(values=city).grid(row=6,column=0)

def btn():
    print("Button clicked!")

tkinter.Button(text="Submit",font='Constantia 15 bold',command=btn).place(x=200,y=250)
tk.mainloop()