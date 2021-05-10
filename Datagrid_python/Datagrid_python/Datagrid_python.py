
import tkinter as tk
from tkinter.ttk import *


class App(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.label_frame = tk.Frame(self.master)
        self.label_frame.grid()

        self.label_list = []

        for i in range(3):
            self.label_list.append(tk.Label(self.label_frame, text="Some Data"))
            self.label_list[i].grid(row=i)

        self.label_list.append(tk.Button(self.label_frame, text="Add new data", command=self.add_new_data))
        self.label_list[2].grid(row=2)

    def add_new_data(self):
        self.label_list.insert(1, tk.Label(self.label_frame, text="<<New Data>>"))

        for widget in self.label_frame.children.values():
            widget.grid_forget() 

        for ndex, i in enumerate(self.label_list):
            i.grid(row=ndex)


if __name__ == "__main__":
    root = tk.Tk() 
    my_app = App(root)
    root.mainloop()



#class MyGui(Frame):

#    def CreateGrid(self):
#        tv = Treeview(self)
#        tv['columns'] = ('Name', 'Mobile', 'Course')
#        tv.heading("#0", text = 'RollNo', anchor = 'w')
#        tv.column("#0", anchor="w")
#        tv.heading('Name', text='Name')
#        tv.column('Name', anchor='center', width=100)
#        tv.heading('Mobile', text='Mobile')
#        tv.column('Mobile', anchor='center', width=100)
#        tv.heading('course', text='course')
#        tv.column('course', anchor='center', width=100)
#        tv.grid(sticky = (N,S,W,E))
#        self.treeview = tv
#        self.grid_rowconfigure(0, weight = 1)
#        self.grid_columnconfigure(0, weight = 1)


#root = tk.Tk()
#MyGui(root)

#def adddata():
#    Label(root, text="<<some data>>").grid(row=1)


#Button(root, text="Add Data", command=adddata).grid(row=3)

##entry = tk.Entry(root)
##entry.grid(row=0, column = 0, sticky = "ew")
##entry.insert(0, "hello, world")
##entry.grid(row=1, column = 1, sticky = "ew")
##entry.insert(0, "stuff")

#root.mainloop()
