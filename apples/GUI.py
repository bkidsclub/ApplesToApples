from tkinter import *
import tkinter as tk
#Creating the Canvas
root = tk.Tk ()
canvas = Canvas(root, width=1280, height=1080, bg="#cc9900")
canvas.pack()
#Green Card
canvas.create_rectangle( 300, 300, 650, 600, fill="#33cc33", outline="white", width=4)
#Choices
canvas.create_text(50, 10, fill="white", font="Times 20 italic bold",
                   text="Rapple1")
canvas.create_text(50, 30, fill="white", font="Times 20 italic bold",
                   text="Rapple2")
canvas.create_text(50, 50, fill="white", font="Times 20 italic bold",
                   text="Rapple3")
canvas.create_text(50, 70, fill="white", font="Times 20 italic bold",
                   text="Rapple4")
canvas.create_text(50, 90, fill="white", font="Times 20 italic bold",
                   text="Rapple5")
canvas.create_text(50, 110, fill="white", font="Times 20 italic bold",
                   text="Rapple6")
canvas.create_text(50, 130, fill="white", font="Times 20 italic bold",
                   text="Rapple7")
#Buttons to choose the word
master = Tk()
b = Button(master, text="OK", command=print("good"))
b.pack()
#Red Cards
canvas.create_rectangle( 750, 700, 950, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 800, 700, 1000, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 850, 700, 1050, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 900, 700, 1100, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 950, 700, 1150, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 1000, 700, 1200, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 1050, 700, 1250, 900, fill="#ff3300", outline="white", width=4)
root.mainloop()
