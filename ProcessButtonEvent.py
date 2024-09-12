from tkinter import * # Import tkinter

def processOK():
    print("OK button is clicked")
 
def processCancel():
    print("Cancel button is clicked")
    
window = Tk() # Create a root window
btOK = Button(window, text = "OK", fg = "red", 
    command = processOK) # Invoke processOK when OK button is clicked
btCancel = Button(window, text = "Cancel", bg = "yellow", 
                  command = processCancel) 
btOK.pack() # Place the button in the window
btCancel.pack() # Place the button in the window

window.mainloop() # Create an event loop