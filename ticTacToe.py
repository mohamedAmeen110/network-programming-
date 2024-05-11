from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic-Tac-Toe")
window.geometry("400x300")

# Label for the game title
title_label = Label(window, text="Tic-Tac-Toe Game", font=('Helvetica', 15))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Labels for players
player1_label = Label(window, text="Player 1: X", font=('Helvetica', 10))
player1_label.grid(row=1, column=0)
player2_label = Label(window, text="Player 2: O", font=('Helvetica', 10))
player2_label.grid(row=2, column=0)

turn = 1  # For player's turn

def reset():
    global turn
    for btn in buttons:
        btn["text"] = " "
    turn = 1

def clicked(index):
    global turn
    btn = buttons[index]
    if btn["text"] == " ":
        if turn == 1:
            btn["text"] = "X"
            turn = 2
        else:
            btn["text"] = "O"
            turn = 1
        check_winner()

def check_winner():
    for combo in win_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != " ":
            messagebox.showinfo("Congratulations", f"Player {buttons[combo[0]]['text']} wins!")
            window.destroy()
            return
    if all(btn["text"] != " " for btn in buttons):
        messagebox.showinfo("Tie", "Match Tied! Try again :)")
        window.destroy()

# Buttons for the game
buttons = []
for i in range(3):
    for j in range(3):
        btn = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', 20),
                     command=lambda index=i*3+j: clicked(index))
        btn.grid(row=i + 1, column=j + 1)
        buttons.append(btn)

# Reset button
reset_btn = Button(window, text="Reset", bg="white", fg="Black", width=5, height=1, font=('Helvetica', 12), command=reset)
reset_btn.grid(row=4, column=1, columnspan=3, pady=10)

# Possible winning combinations
win_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

window.mainloop()
