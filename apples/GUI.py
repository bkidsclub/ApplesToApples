from Tkinter import *
import Tkinter as tk
root = tk.Tk ()
canvas = Canvas(root, width=1280, height=1080, bg="black")
image1 = tk.PhotoImage(file="C:\Users\Happy\Desktop\Programming\Apples To Apples\Table.gif")
w = image1.width()
h = image1.height()
panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1
canvas.pack()
canvas.create_rectangle( 300, 250, 600, 500, fill="#33cc33", outline="white", width=4)
canvas.create_text(450, 350, fill="white", font="Times 20 italic bold",
                   text="Gapple Function")
root.mainloop()