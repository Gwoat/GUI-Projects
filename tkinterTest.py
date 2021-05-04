from tkinter import *

top = Tk()
songList = []

def addTrack():
    songList.append(E1.get())


def printList():
    print(songList)

#this is a label widget
L1 = Label(top, text="Playlist Generator")

L1.grid(column= 0, row= 1)

#This is an entry widget (for text entry)
E1 = Entry(top, bd = 5)

E1.grid(column= 0, row = 2)
#This is a button widget.
B1 = Button(text = "Add to playlist", bg = "pink", command = addTrack)

B1.grid(column= 2, row = 1)




#print button
B2 = Button(text = "Print", bg = "orange", command = printList)

B2.grid(column= 2, row = 2)



top.mainloop()
