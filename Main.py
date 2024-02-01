from tkinter import *
from Latex import *
from Settings import *

def main():
    win = Tk()
    win.geometry("700x350")
    win.title("LaTex Viewer")
    tabcontrol = ttk.Notebook(win)
    tab1 = ttk.Frame(tabcontrol)
    tab2 = ttk.Frame(tabcontrol)
    tabcontrol.add(tab1,text='Latex Editor')
    tabcontrol.add(tab2,text='Settings')
    tabcontrol.pack(expand=1,fill='both')
    lt = Latex(tab1)
    st = Settings(tab2,lt)
    win.bind('<Return>', lt.graph)
    win.mainloop()

if __name__=="__main__":
   main()