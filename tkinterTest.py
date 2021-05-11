from tkinter import *

top = Tk()
songList = []



def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()
        
def mainMenu():
    clearWindow()
    LMain = Label(top, text= "Block 5 GUI Projects")
    LMain.grid(column = 0, row= 1)
    
    B1Main = Button(text = "Week 1", bg = "pink", command = week1)
    B1Main.grid(column = 0, row=1)
    
    B2Main = Button(text = "Week 2", bg = "purple", command = week2)
    B2Main.grid(column = 1, row = 2)
    
    B3Main = Button(text = "Week 3", bg = "orange", command = week3)
    B3Main.grid(column = 1, row = 3)

def week1():


    
    def addTrack():
        songList.append(E1.get())
        E1.delete(0, END)
        
    clearWindow()

    
    #this is a label widget
    L1 = Label(top, text="LETS GO")

    L1.grid(column= 0, row= 1)

    #This is an entry widget (for text entry)
    E1 = Entry(top, bd = 5)

    E1.grid(column= 0, row = 2)
    #This is a button widget.
    B1 = Button(text = "+", bg = "pink", command = addTrack)

    B1.grid(column= 2, row = 1)


    #print button
    B2 = Button(text = "Print", bg = "orange", command = printList)

    B2.grid(column= 2, row = 2)

    #export button
    B3 = Button(text = "Exporte", bg = "purple", command = exportList)

    B3.grid(column= 3, row = 2)
    

def week2():
    clearWindow()

    L1W2 = Label(top, text= "Dice Roller App")
    L1W2.grid(column = 2, row = 1)

    
    L2W2 = Label(top, text= "# of sides")
    L2W2.grid(column = 0, row = 2)
    
    L3W2 = Lable(top, text= "# of rolls")
    L3W2.grid(column = 0, row = 3)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 3, row = 3)

    
    B1W2 = Button(text= "Roll 'em", bg = "yellow")
    B1W2.grid(column = 2, row = 4)






if __name__ == "__main__":
    mainMenu()
    top.mainloop()
    
