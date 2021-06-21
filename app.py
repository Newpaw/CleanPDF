
from tkinter import *
from tkinter import filedialog
from pdf2image import convert_from_path

# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/Users/Honza/Nextcloud/MAS KPZ",
                                          title = "Select a File",
                                          filetypes = (("PDF files",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))
      
    print(filename)
    # Change label contents
    label_file_explorer.configure(text="DONE")
      
      
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('Make the PDF clean.')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "Make our PDF clean like never before. :)",
                            width = 75, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)
  
# Let the window wait for any events
window.mainloop()
