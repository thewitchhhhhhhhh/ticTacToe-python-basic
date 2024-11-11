import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        self.player = "X"
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.game_frame, text="", font='normal 20 bold', width=5, height=2,
                                               command=lambda i=i, j=j: self.click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, i, j):
        if self.buttons[i][j]['text'] == "" and self.check_winner() is False:
            self.buttons[i][j]['text'] = self.player
            if self.check_winner() is False:
                self.player = "O" if self.player == "X" else "X"
            elif self.check_winner() is True:
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
            elif self.check_winner() == "Tie":
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                
    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        if all(self.buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
            return "Tie"
        return False
