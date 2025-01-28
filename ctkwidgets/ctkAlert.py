import ctkcomponents as ctk
from ctkcomponents import CTkAlert, CTkInput
from customtkinter import CTk, CTkSlider
from tkinter import messagebox
from ctkmvc import CTkModel
# CTkInput
app = CTk()
app.geometry("500x400")

my_input = CTkInput(master=app, width=250, height=35, icon_width=20, icon_height=20, border_width=1)
my_input.pack(padx=20, pady=20)
my_input.show_waring(border_color="green") # Create a warning input
# Call this function to reset input default
my_input.reset_default()
app.mainloop()