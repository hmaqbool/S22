from pydoc import locate
from tkinter import Button, Label
import setting
import random
class Cell:
    all=[]
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object = None
        self.x=x
        self.y=y
        Cell.all.append(self)
    
    def create_btn_object(self,location):
        btn= Button(
            location,
            width=12,
            height=4,
            
        )
        btn.bind('<Button-1>',self.left_click_actions)
        btn.bind('<Button-3>',self.right_click_actions)
        self.cell_btn_object=btn
    @staticmethod
    def create_cell_count_label(self,location):
        lbl=Label(
            location,
        text=f"Cells Left:{settings.cell_count}")
        return lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
        

    @property
    def surrounded_cells(self):
        cells=[
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)
        ]
        cells=[cell for cell in cells if cell is not None]
        return cells
    @property
    def surrounded_cells_mines_length(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter=counter+1
        return counter



    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell

    def show_mine(self):
        self.cell_btn_object.configure(bg="red")

    def right_click_actions(self, event):
        print(event)
        print("i am rightt clicked")

    @staticmethod
    def randomize_mines():
        picked_cells=random.sample(Cell.all,setting.mines_count)
        for picked_cell in picked_cells:
            picked_cell.is_mine=True
    def __repr__(self): 
        return f'{self.x},{self.y}'



    