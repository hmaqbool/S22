from tkinter import *
import setting
import utils
from cell import Cell


root=Tk()
#override window setting
root.configure(bg="black")
root.geometry(f'{setting.width}x{setting.height}')#change windo dimensions
root.title("Minesweeper") #change title
root.resizable(False,False)
top_frame=Frame(
    root,
    bg='black',
    width=setting.width,
    height=utils.height_prct(25)
)
top_frame.place(x=0,y=0)
left_frame=Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
    )
left_frame.place(x=0,y=utils.height_prct(25))

center_frame =Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25),

)



for x in range(setting.grid_size):
    for y in range(setting.grid_size):
        c=Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,row=y
        )

Cell.randomize_mines()

#main loop tell code to run till close "x" is pressed
#run window
root.mainloop()
