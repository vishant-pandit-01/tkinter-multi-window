from tkinter import *
def second_window():
    second=Toplevel()
    second.title("hello")
    second.geometry("300x300")
    root.config(background="pink")

    Label(second,text="welcome on second wiondow",bd=5,background="pink").pack()

root=Tk()
root.geometry("350x350")
root.config(background="pink")
root.title("window")

bt=Button(root,text="press for open second window",command=second_window,background="black",relief="ridge",foreground="white").pack(pady=30)

root.mainloop()