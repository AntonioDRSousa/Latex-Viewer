from tkinter import Entry, Label, ttk, StringVar

class Settings:
    def __init__(self,tab2,lt):
        self.lt = lt
        label_sizefont = Label(tab2,text='Size Font : ')
        label_sizegap = Label(tab2,text='Size Gap : ')
        label_inf = Label(tab2,text='Gap Size Between 0 to 1')
        
        n1 = StringVar() 
        n1.set("20")
        n2 = StringVar() 
        n2.set("0.1")
        self.entry_sizefont = Entry(tab2,justify = "center", textvariable=n1)
        self.entry_sizegap = Entry(tab2,justify = "center", textvariable=n2)
        
        button = ttk.Button(tab2,text='OK')
        
        label_sizefont.grid(row=0,column=0)
        label_sizegap.grid(row=1,column=0)
        self.entry_sizefont.grid(row=0,column=1)
        self.entry_sizegap.grid(row=1,column=1)
        label_inf.grid(row=0,column=2,rowspan=2,columnspan=1)
        button.grid(row=2,column=0,rowspan=1,columnspan=3,sticky="news")
        
        button.bind('<Button 1>', self.updateSettings)
    
    def updateSettings(self,event):
        print(int(self.entry_sizefont.get()))
        self.lt.fnt_size = int(self.entry_sizefont.get())
        self.lt.gap_size = float(self.entry_sizegap.get())
        self.lt.update()