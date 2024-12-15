
from tkinter import *
import random

user_score = 0
com_score = 0
tie_score = 0

#rock
def rock_function():
    global user_score, com_score, tie_score
    options = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(options)
    #randint o use kora jae but choice is better and more random

    global computer_choice_label
    computer_choice_label.destroy() #new function i learned, it destroys label texts
    computer_choice_label = Label(root, text=f"Computer chose: {computer_choice}", font=("arial", 12))
    computer_choice_label.pack()

    if computer_choice == "rock":
        result_label["text"] = "It's a Tie!"
        tie_score += 1
    elif computer_choice == "scissor":
        result_label["text"] = "You Win!"
        user_score += 1
    else:
        result_label["text"] = "You Lose!"
        com_score += 1

#paper
def paper_function():
    global user_score, com_score, tie_score
    options = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(options)

    global computer_choice_label
    computer_choice_label.destroy()
    computer_choice_label = Label(root, text=f"Computer chose: {computer_choice}", font=("arial", 12))
    computer_choice_label.pack()

    if computer_choice == "paper":
        result_label["text"] = "It's a Tie!"
        tie_score += 1
    elif computer_choice == "rock":
        result_label["text"] = "You Win!"
        user_score += 1
    else:
        result_label["text"] = "You Lose!"
        com_score += 1

#scissor
def scissor_function():
    global user_score, com_score, tie_score
    options = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(options)

    global computer_choice_label
    computer_choice_label.destroy()
    computer_choice_label = Label(root, text=f"Computer chose: {computer_choice}", font=("arial", 12))
    computer_choice_label.pack()

    if computer_choice == "scissor":
        result_label["text"] = "It's a Tie!"
        tie_score += 1
    elif computer_choice == "paper":
        result_label["text"] = "You Win!"
        user_score += 1
    else:
        result_label["text"] = "You Lose!"
        com_score += 1
#to quit
def quit_game():
    final_result = f"You won {user_score} times.\nComputer won {com_score} times.\nTied {tie_score} times."
    result_label["text"] = final_result  #text updated in result_label
    computer_choice_label.destroy()
    rock_button["state"] = "disabled"  #state updated,disbale to off the button
    paper_button["state"] = "disabled"
    scissors_button["state"] = "disabled"
    quit_button["state"] = "disabled"

root = Tk()
root.geometry("500x500")
root.title("Rock, Paper, Scissors Game")

# score result dekhabe
Label(root, text="Rock, Paper, Scissors Game", font=("arial", 16)).pack(pady=10)
result_label = Label(root, text="", font=("arial", 14), fg="blue")
result_label.pack(pady=10)
computer_choice_label = Label(root, text="", font=("arial", 12))
computer_choice_label.pack()

# rock paper scissor button
rock_button = Button(root, text="Rock", command=rock_function, width=15)
rock_button.pack(pady=5)
paper_button = Button(root, text="Paper", command=paper_function, width=15)
paper_button.pack(pady=5)
scissors_button = Button(root, text="Scissors", command=scissor_function, width=15)
scissors_button.pack(pady=5)

# Quit button
quit_button = Button(root, text="Quit", command=quit_game, width=15)
quit_button.pack(pady=20)

root.mainloop()