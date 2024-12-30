import tkinter as tk
import ttkbootstrap as ttk

#window
window = ttk.Window(themename= "darkly")
window.geometry("1000x1000")
window.title("To do List")

#Title
Title_label = ttk.Label(window, text = "To do list:", font = "Rubik 20 bold")
Title_label.pack()

#Add
Add_frame = ttk.Frame(window)
class add_func():
  pass
Add_text = ttk.Text(Add_frame, width = 15, height = 3)
Add_text.pack(side="left")
Add_button = ttk.Button(Add_frame, text = " Add ", command = add_func)
Add_button.pack(side = "left", padx = 5)
Add_frame.pack(pady = 5)

#To do
Do_frame = ttk.Frame(window)
Do_label = ttk.Label(Do_frame)
Do_label.pack(side="left")
Do_frame.pack(pady = 5)

#Exit
Exit = ttk.Button(window,text="Exit", command = window.destroy)
Exit.pack()


#mainlooop
window.mainloop()