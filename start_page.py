import tkinter as tk
from tkinter import messagebox
from game_logic import TicTacToe

class StartPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x300")

        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack()

        tk.Label(self.start_frame, text="Tic Tac Toe", font=("Helvetica", 24)).pack(pady=20)
        tk.Button(self.start_frame, text="Start Game", command=self.start_game).pack()
        tk.Label(self.start_frame, text="Developed by Rimsha Shaikh", font=("Helvetica", 10)).pack(side="bottom", anchor="e")

    def start_game(self):
        self.start_frame.pack_forget()
        self.game = TicTacToe(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = StartPage(root)
    root.mainloop()
