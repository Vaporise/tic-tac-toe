import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game") # creates the title for the game window
        self._cells = {} #will contain the co-ordinates for the tic-tac-toe game

    def _create_board_display(self):
        display_frame = tk.Frame(master=self) # creates a display frame
        display_frame.pack(fill=tk.X) #Puts the frame on the main window's top border
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font = font.Font(size=28, weight="bold"),
        )
        self.display.pack() #packs the above label inside the frame.

    def _create_board_grid(self:)