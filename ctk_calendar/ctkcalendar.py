import customtkinter as ctk
from ctkdateentry import CTkDateEntry, CTkStringVar
from tkinter import *

root = ctk.CTk()

root.geometry('200x200')
root.title('CTkDateEntry')
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')

var = CTkStringVar(root, value='Ingresa la fecha') #Variable that will be inserted in CTkDateEntry

date_entry = CTkDateEntry(root,
    width=200,
    variable =var,
    justify ='left',
    font=('Roboto', 14, 'bold'))
date_entry.pack(pady=50)

root.mainloop()