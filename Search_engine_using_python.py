import tkinter as tk
import webbrowser
root=tk.Tk()
root.title("WEB BROWSER")
root.geometry('500x150')
root.configure(bg="black")
def lk():
    webbrowser.open_new("www.linkedin.com")
def gh():
    webbrowser.open_new("www.github.com")
def fb():
    webbrowser.open_new("www.facebook.com")
def yt():
    webbrowser.open_new("www.youtube.com")
def ig():
    webbrowser.open_new("www.instagram.com")
def ws():
    webbrowser.open_new("www.w3schools.com")
def engine():
    value=a.get()
    search='https://www.google.com/search?q='+value
    webbrowser.open_new(search)
a=tk.StringVar()    
bt1=tk.Button(root,text="linkedin",fg="white",bg="#006192",command=lk)
bt2=tk.Button(root,text="GitHub",fg="white",bg="#4183c4",command=gh)
bt3=tk.Button(root,text="Facebook",fg="white",bg="#3b5998",command=fb)
bt4=tk.Button(root,text="Youtube",fg="white",bg="#FF0000",command=yt)
bt5=tk.Button(root,text="Instagram",fg="white",bg="#E1306C",command=ig)
bt6=tk.Button(root,text="w3schools",fg="white",bg="#4CAF50",command=ws)
bt7=tk.Button(root,text="Search",fg="white",bg="#EE82EE",command=engine)


bt1.place(x=10,y=70,width=70,height=30)
bt2.place(x=100,y=70,width=70,height=30)
bt3.place(x=200,y=70,width=70,height=30)
bt4.place(x=10,y=100,width=70,height=30)
bt5.place(x=100,y=100,width=70,height=30)
bt6.place(x=200,y=100,width=70,height=30)
bt7.place(x=400,y=20,width=80,height=50)

en1=tk.Entry(root,textvariable=a)
en1.place(x=10,y=20,width=380,height=50)
root.mainloop() 