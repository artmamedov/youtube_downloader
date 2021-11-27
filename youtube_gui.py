from tkinter import *
from youtube import *

root = Tk()
root.geometry('400x100')

def run():
    url = youtube_link_enter.get()
    download_url(url)

youtube_link_label = Label(root, text="Enter Youtube Link", font=("Verdana", 15))
youtube_link_label.grid(row=0, column=0, sticky="NSEW")
youtube_link_enter = Entry(root, justify='left', font=("Verdana", 15))
youtube_link_enter.grid(row=0, column=1, columnspan=2, sticky="NSEW")

startButton = Button(root, text="Download", command=run, font=("Verdana", 15))
startButton.grid(row=1, columnspan=3, sticky="NSEW")

if __name__ == "__main__":
    root.mainloop()
