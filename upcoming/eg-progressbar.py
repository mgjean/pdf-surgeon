import tkinter as tk
from tkinter import ttk
from time import sleep

teams = range(5)

def button_command():
    #start progress bar
    popup = tk.Toplevel()
    tk.Label(popup, text="processing files").grid(row=0,column=0)

    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=100,length=200)
    progress_bar.grid(row=1, column=0)#.pack(fill=tk.X, expand=1, side=tk.BOTTOM)
    popup.pack_slaves()

    progress_step = float(100.0/len(teams))
    for team in teams:
        popup.update()
        sleep(1) # lauch task
        progress += progress_step
        progress_var.set(progress)

    return popup.destroy()

root = tk.Tk()

tk.Button(root, text="Launch", command=button_command).pack()

root.mainloop()