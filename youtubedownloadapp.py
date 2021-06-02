from tkinter import *                                   #importing tkinter
from pytube import YouTube                              # importing youtube module

root = Tk()                                             # initializing tkinter

root.geometry("400x350")                                # setting the geometry of the GUI ( To set a specific size of the window)          

root.title("Youtube video downloader application")      # setting the title of the GUI

def download():                                         # defining download function
    
    try:                                                 # using try and except to execute program without errors
        Var.set("Start download...")                      # set is to set and change value within tkinter
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successfully")
    except Exception as e:
        Var.set("Mistake")
        root.update()
        link.set("Enter correct link")


Label(root, text="Welcome to youtube\nDownloader Application", font="Consolas 15 bold").pack()     # created the Label widget to welcome user

Var = StringVar()                                                   # declaring StringVar type variable

Var.set("Enter the link below")                                       # setting the default text to Var

Entry(root, textvariable=Var, width=40).pack(pady=10)                 # created the Entry widget to ask user to enter the url (getting input)

link = StringVar()                                                    # declaring StringVar type variable

Entry(root, textvariable=link, width=40).pack(pady=10)                 # created the Entry widget to get the link

Button(root, text="Download video", command=download).pack()           # created and called the download function to download video








#root.mainloop()                                                        # running the mainloop
