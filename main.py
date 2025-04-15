import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game") # creates the title for the game window
        self._cells = {} #will contain the co-ordinates for the tic-tac-toe game
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self) # creates a display frame
        display_frame.pack(fill=tk.X) #Puts the frame on the main window's top border
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font = font.Font(size=28, weight="bold"),
        )
        self.display.pack() #packs the above label inside the frame.

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self) #create the grid's frame
        grid_frame.pack()
        for row in range(3): #iterates over 3 in a row
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3): #iterates over 3 in a column
                button = tk.Button( #creates a button on each grid slot
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row,col) #adds every new button to the cell dictionary created in the __init__.
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

def main():
    #create  the game loop
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()