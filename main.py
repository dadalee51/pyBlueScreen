from tkinter import *


class BlueScreenGUI:


    def __init__(self, master, w_wid, w_hgt):
        self.blue_id = StringVar()
        self.master = master
        master.title("A BlueScreen")
        frame = Frame(master)
        Label(frame, text="Left", font=("Courier New", 60)).grid(row=0, column=0)
        Label(frame, text="Right", font=("Courier New", 60)).grid(row=0, column=2)
        Label(frame, font=("Courier New", 60)).grid(row=1, column=0)
        Label(frame, font=("Courier New", 60)).grid(row=1, column=1)
        Button(frame, text="connect", command=self.connect).grid(row=2, column=0)
        self.en = Entry(frame, textvariable=self.blue_id)
        self.en.grid(row=2,column=1)
        frame.pack(expand=1)

    def connect(self):
        print("connecting to %s" % self.blue_id.get())


root = Tk()
scrWidth = root.winfo_screenwidth()
scrHeight = root.winfo_screenheight()
# scrWidth = 1024
# scrHeight = 768
root.geometry("%sx%s" % (scrWidth, scrHeight))
myApp = BlueScreenGUI(root, scrWidth, scrHeight)
root.mainloop()
