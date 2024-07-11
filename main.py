from tkinter import *
from Game import * 
from Map import *

def main():
    root = Tk()
    root.resizable(False, False) # Windows is not resizable
    root.config(bg='black') # Grey background
    root.geometry("1960x940") # Window size

    # Left frame for map and drawings
    left_frame = Frame(root, width=1300, height=928)
    left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

    # Right frame for commands
    right_frame = Frame(root, width=500, height=928)
    right_frame.pack(side=LEFT, padx=10, pady=10)

    # Canvas to draw map and nodes
    canvas = Canvas(left_frame)
    canvas.pack(fill=BOTH, expand=True)

    # Load map image
    image = ImageTk.PhotoImage(file = 'assets/board.jpg')
    canvas.create_image(0, 0, image = image, anchor = NW)

    m = Map(canvas)
    g = Game(m)

    hint_value = IntVar()
    time_value = IntVar()
    Label(right_frame, text='Hint node: ').grid(row=1, column=0)
    entry1 = Entry(right_frame, textvariable=hint_value).grid(row=1, column=1, pady=4)
    entry2 = Entry(right_frame, textvariable=time_value).grid(row=1, column=2, pady=4)
    Button(right_frame, text='Hint', command=lambda v=(hint_value, time_value): g.hint(v)).grid(row=1,column=3, pady=4)

    Button(right_frame, text='Advance', command=lambda: g.advance()).grid(row=2,column=2, pady=4)

    round = g.get_current_round()
    round.set_starting_node(m.get_node(27))

    while 1:
        root.update()
        m.update()
    
    root.mainloop()

if __name__ == "__main__":
    main()