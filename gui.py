import tkinter

root = tkinter.Tk()
root.title('Stock Market')
root.geometry('270x90')
l1 = tkinter.Label(root, text='Enter company name').place(x=6, y=10)
e1 = tkinter.Entry(root).place(x=130, y=10)
root.mainloop()
