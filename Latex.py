from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Latex:
    def __init__(self,tab1):
    
       self.fnt_size = 20
       self.gap_size = 0.1
       
       self.text = Text(tab1,width=1,height=1)
       
       label = Label(tab1)
       matplotlib.use('TkAgg')
       fig = matplotlib.figure.Figure(figsize=(1, 1), dpi=100)
       self.mthplt = fig.add_subplot(111)
       self.canvas = FigureCanvasTkAgg(fig, master=label)
       self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
       self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
       self.mthplt.get_xaxis().set_visible(False)
       self.mthplt.get_yaxis().set_visible(False)
       
       scroll = Scrollbar(tab1, orient="vertical", command=self.text.yview)
       
       self.text.pack(side=LEFT,fill='both',expand=1)
       scroll.pack(side=LEFT,fill='both')
       label.pack(side=RIGHT,fill='both',expand=1)
       
       self.math_mod = False
       self.tag_mod = False   
        
    def graph(self,event):
        self.update()
        
    def update(self):
        tmptext = self.text.get(1.0, "end-1c")
        v = tmptext.split('\n')
        self.mthplt.clear()
        print((self.fnt_size,self.gap_size))
        for i in range(len(v)):
            tmptext = v[i]
            s=self.mthplt.text(0,1-((i+1)*self.gap_size), tmptext, fontsize = self.fnt_size)
        self.canvas.draw()