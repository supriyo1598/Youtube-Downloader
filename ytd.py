from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import os

Folder_Name=""

def openLocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please Choose the folder!!",fg="red")

def DownloadVideo():
    choice=ytdchoices.get()
    url=ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt=YouTube(url)

        if(choice==choices[0]):
            select=yt.streams.filter(progressive=True).first()
        elif (choice==choices[1]):
            select=yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif (choice==choices[2]):
            select=yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Paste Link Again",fg="red")

    select.download(Folder_Name)
    ytdError.config(text="Download Complete",fg="green")
                




root=Tk()
root.title("Youtube Downloader")

root.iconbitmap('Youtube.ico')

root.geometry("300x400")
root.columnconfigure(0,weight=1)



ytdLabel=Label(root,text="Enter the url for the video",font=("jost",15))
ytdLabel.grid()

ytdEntryVar=StringVar()
ytdEntry=Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

ytdError=Label(root,text="Error Msg",fg="red",font=("josh",10))
ytdError.grid()

saveLabel=Label(root,text="Save te video file",font=("josh",15))
saveLabel.grid()

saveEntry=Button(root,width=10,text="Choose path",fg="white",bg="blue",command=openLocation)
saveEntry.grid()

locationError=Label(root,text="Location Error Msg",fg="red",font=("josh",10))
locationError.grid()

ytdQuality=Label(root,text="Choose Quality",font=("josh",15))
ytdQuality.grid()

choices=["720p","144p","Only Audio"]
ytdchoices=ttk.Combobox(root,values=choices)
ytdchoices.grid(pady = (0,5))

saveEntry=Button(root,width=15,text="Download",fg="white",bg="blue",command=DownloadVideo)
saveEntry.grid(pady = (0,25))

devlop=Label(root,text="Build By Supriyo Sarkar",font=("josh",15))
devlop.grid()

root.mainloop()
