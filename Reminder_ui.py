from tkinter import *
import tkinter as tk
from tkinter import messagebox as mbox

from dbreminder import Database

database=Database("nudgeme.db")

class Window(object):

    def __init__(self,window):

        self.window = window

        self.window.wm_title("Nudge Me")

        b1=Button(window,text="View", width=12,command=self.cmd_view)
        b1.grid(row=0,column=0)
		
        b3=Button(window,text="Add Reminder", width=12,command=self.cmd_add)
        b3.grid(row=0,column=1)

        b4=Button(window,text="Update Reminder", width=12,command=self.cmd_update)
        b4.grid(row=0,column=2)

        b5=Button(window,text="Delete Reminder", width=12,command=self.cmd_delete)
        b5.grid(row=0,column=3)

        b6=Button(window,text="Close", width=12,command=window.destroy)
        b6.grid(row=0,column=4)

        l1=Label(window,text="Event")
        l1.grid(row=2,column=0)
        l1.visible = True

        l2=Label(window,text="Description")
        l2.grid(row=2,column=2)
        l2.visible = True

        l3=Label(window,text="Date")
        l3.grid(row=3,column=0)
        l3.visible = True

        l4=Label(window,text="Status")
        l4.grid(row=3,column=2)
        l4.visible = True

        self.txt_event=StringVar()
        self.e1=Entry(window,textvariable=self.txt_event)
        self.e1.grid(row=2,column=1)
        #e1.visible = True

        self.txt_desc=StringVar()
        self.e2=Entry(window,textvariable=self.txt_desc)
        self.e2.grid(row=2,column=3)
        #e2.visible = False

        self.txt_date=StringVar()
        self.e3=Entry(window,textvariable=self.txt_date)
        self.e3.grid(row=3,column=1)
        #e3.visible = False


        self.txt_status=StringVar()
        self.e4=Entry(window,textvariable=self.txt_status)
        self.e4.grid(row=3,column=3)
        #e4.visible = False

        self.list1=Listbox(window, height=6,width=35)
        self.list1.grid(row=4,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=4,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        

    def get_selected_row(self,event):
        if len(self.list1.curselection())>0:
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])

    def cmd_view(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def cmd_add(self):
        database.add(self.txt_event.get(),self.txt_desc.get(),self.txt_date.get(),self.txt_status.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.txt_event.get(),self.txt_desc.get(),self.txt_date.get(),self.txt_status.get()))
        mbox.showinfo("Message", "added")
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)


    def cmd_delete(self):
        database.delete(self.selected_tuple[0])
        mbox.showinfo("Message", "deleted")
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        
    

    def cmd_update(self):
        database.update(self.selected_tuple[0],self.txt_event.get(),self.txt_desc.get(),self.txt_date.get(),self.txt_status.get())
        mbox.showinfo("Message", "updated")
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)

window=Tk()
Window(window)
window.mainloop()
