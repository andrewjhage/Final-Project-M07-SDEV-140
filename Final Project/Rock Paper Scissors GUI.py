from tkinter import *
from random import choices, randint
from PIL import Image, ImageTk

#main window
root= Tk()
root.title("Rock, Paper, Scissors")
root.configure(background="PeachPuff2")



#picture
rock_img =ImageTk.PhotoImage(Image.open('C:/Users/Drew/OneDrive/Documents/SDEV140/Final Project/Rock1.png'))
paper_img =ImageTk.PhotoImage(Image.open('C:/Users/Drew/OneDrive/Documents/SDEV140/Final Project/Paper1.png'))
scissor_img =ImageTk.PhotoImage(Image.open('C:/Users/Drew/OneDrive/Documents/SDEV140/Final Project/Scissors1.png'))
rock_img_comp =ImageTk.PhotoImage(Image.open('C:/Users/Drew/OneDrive/Documents/SDEV140/Final Project/Rock1.png'))
paper_img_comp =ImageTk.PhotoImage(Image.open('C:/Users/Drew/OneDrive/Documents/SDEV140/Final Project/Paper1.png'))
scissor_img_comp =ImageTk.PhotoImage(Image.open('C:/Users/Drew/OneDrive/Documents/SDEV140/Final Project/Scissors1.png'))

#insert picture
user_label = Label(root,image=rock_img, bg="PeachPuff2")
computer_label = Label(root, image=rock_img_comp,bg="PeachPuff2")
computer_label.grid(row=1, column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root, text=0, font=100, bg="PeachPuff2", fg="white")
computerScore = Label(root, text=0, font=100, bg="PeachPuff2", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicators
user_indicator = Label(root, font=50, text="USER",bg="PeachPuff2",fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",bg="PeachPuff2",fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root,font='Bizon 30 bold', bg="PeachPuff2", fg="white")
msg.grid(row=3, column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore["text"] =str(score)
#update computer score
def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore["text"] =str(score)

#check winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            updateMessage("You Lose!")
            updateCompScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    elif player == "Paper":
        if computer == "Scissors":
            updateMessage("You Lose!")
            updateCompScore()
        else: 
            updateMessage("You Win!")
            updateUserScore()
    elif player == "Scissors":
        if computer == "Rock":
            updateMessage("You Lose!")
            updateCompScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    else:
        pass


#update choices
choices =["Rock", "Paper", "Scissors"]
def updateChoice(x):
# #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "Rock":
        computer_label.configure(image=rock_img_comp)
    elif compChoice == "Paper":
        computer_label.configure(image=paper_img_comp)
    else:
        computer_label.configure(image=scissor_img_comp)

#for user
    if x =="Rock":
        user_label.configure(image=rock_img)
    elif x == "Paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)
#button
rock =Button(root, width=20, height=2, text="ROCK",font='Bizon 10 bold', bg="red",fg="white", command = lambda:updateChoice("Rock"))
rock.grid(row=2, column=1)
paper =Button(root, width=20, height=2, text="PAPER",font='Bizon 10 bold', bg="yellow",fg="white", command = lambda:updateChoice("Paper"))
paper.grid(row=2, column=2)
scissor =Button(root, width=20, height=2, text="SCISSORS",font='Bizon 10 bold', bg="blue",fg="white", command = lambda:updateChoice("Scissors"))
scissor.grid(row=2,column=3)

root.mainloop()
