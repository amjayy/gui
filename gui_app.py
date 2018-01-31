#from tkinter, root = tk(), root.mainloop()  are basic layouts needed fro GUI
from tkinter import *

root = Tk()

root.mainloop()
#making invisible container that goes in mainroot.Works by default
topFrame = frame(root)
#anytime you want anything displayed you have to pack it in. place it somewhere in main program or window
topFrame.pack()
bottomFrame =frame(root)
bottomFrame.pack(side=BOTTOM)
#throw in parameter in bottom frame to put where it is
#name object button and the first parameter is what frame .
#Fg is set to equal to a color
button1 = Button(topFrame, text= "Button 1", fg="")

root.mainloop()
