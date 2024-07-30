import tkinter as tk #Graphical user Interface
from time import strftime  #imports time. strf can format time 

# root window is the main window that can display elements.
root = tk.Tk() # From this we are creating an object named root. Label class
root.title = ("Digital clock") #Title of the window

def time():                     #to define time
  string = strftime('%H:%M:%S %p \n %D' ) #strf can format time. %H-24 hours , %M-minutes , %S-second , %p-AM and PM, %D-date. \n-Date will show below 
  label.config(text = string) #assigns text attribute by string

  label.after(1000, time) # This will update time after every second. Shows current time and date


# Create and configure the label to display the time
label = tk.Label(root, font=('Helvetica', 50, 'bold',), background='#f0f0f0', foreground='#A86A24')
label.pack(anchor='center') #Align the label object to the center
text_label = tk.Label(root, text="ᗩᗷᕼIᒍITᕼ Tᑭ  ©", font=('Montserrat', 10), bg='#f0f0f0', fg='#A86A24')
text_label.pack(anchor='w')


time() #this will execute time function

root.mainloop()#Main loop method is a method of tkinter module which keeps the window in the loop

