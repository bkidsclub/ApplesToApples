from tkinter import *
import tkinter as tk
#Buttons

class ApplesGUI:
    def __init__(self):
        self.root = tk.Tk()


    def start_screen(self):
        frame = Frame(self.root, bg='#cc9900', width=1200, height=1800)
        frame.pack()
        canvas = Canvas(self.root, width=1280, height=1080, bg="grey")
        canvas.pack()
        b = Button(frame, text="Start", command=self.start)
        b.pack()
        self.root.mainloop()

    def start(self):
        print("started")

r = ApplesGUI().start_screen()

root = tk.Tk ()
frame = Frame(root, bg='grey', width=400, height=40)
frame.pack(fill='x')
button1 = Button(frame, text='Card1', width="12")
button1.pack(side='left')
button2 = Button(frame, text='Card2', width="12")
button2.pack(side='left')
button3 = Button(frame, text='Card3', width="12")
button3.pack(side='left')
button4 = Button(frame, text='Card4', width="12")
button4.pack(side='left')
button5 = Button(frame, text='Card5', width="12")
button5.pack(side='left')
button6 = Button(frame, text='Card6', width="12")
button6.pack(side='left')
button7 = Button(frame, text='Card7', width="12")
button7.pack(side='left')
#Canvas Creation
canvas = Canvas(root, width=1280, height=1080, bg="#cc9900")
canvas.pack()
#Green Card
canvas.create_rectangle( 300, 300, 650, 600, fill="#33cc33", outline="white", width=4)
canvas.create_text(475, 450, fill="white", font="Times 20 italic bold",
                    text="GappleCard")
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
#Red Cards
canvas.create_rectangle( 750, 700, 950, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 800, 700, 1000, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 850, 700, 1050, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 900, 700, 1100, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 950, 700, 1150, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 1000, 700, 1200, 900, fill="#ff3300", outline="white", width=4)
canvas.create_rectangle( 1050, 700, 1250, 900, fill="#ff3300", outline="white", width=4)
root.mainloop()
