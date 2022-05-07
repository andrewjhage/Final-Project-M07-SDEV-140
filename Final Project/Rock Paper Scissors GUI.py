from tkinter import *

root = Tk()

def main():
    root.title("Rock, Paper, Scissors Game")
    root.geometry("800x800")
    randomstring = ""
    first_Label= Label(root, text= "Choose Rock, Paper, or Scissors")
    first_entry = Entry(root, text_Variable=randomstring )

    first_Label.grid(row=0, column=0)
    first_entry.grid(row=1, column=0)

def myClick():
    myButton1 = Button(root, text="This is a button", command=myClick)
    myButton1.grid(row=2, column=1)

def textBox():
    e = Entry(root, width=15)
    e.grid(row=2, column=2)
root.mainloop()

if __name__ == "__main__":
    main()