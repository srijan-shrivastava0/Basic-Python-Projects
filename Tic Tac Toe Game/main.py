import tkinter as tk
from tkinter import messagebox

# Globals
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not check_winner():
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_winner():
    # Rows, Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

def is_draw():
    return all(cell != "" for row in board for cell in row)

def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for btn in row:
            btn["text"] = ""

def create_gui():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    for r in range(3):
        for c in range(3):
            btn = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2,
                            command=lambda row=r, col=c: on_click(row, col))
            btn.grid(row=r, column=c)
            buttons[r][c] = btn

    root.mainloop()

# Run the game
create_gui()
