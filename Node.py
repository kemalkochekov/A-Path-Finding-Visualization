import pygame
# Colors

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
 
class Node:
    def __init__(self,row,col,width,total_rows):
        self.row=row
        self.col=col
        self.x=row*width
        self.y=col*width
        self.color=WHITE
        self.neighbors=[]
        self.width=width
        self.total_rows=total_rows
    
    def get_pos(self):
        return self.row,self.col
    
    def closed(self):
        return self.color==RED
    
    def open(self):
        return self.color==GREEN
    
    def barrier(self):
        return self.color==BLACK
    
    def start(self):
        return self.color==ORANGE
    
    def end(self):
        return self.color==TURQUOISE
    
    def reset(self):
        self.color=WHITE
    
    def make_start(self):
        self.color=ORANGE
    
    def make_closed(self):
        self.color=RED
        
    def make_open(self):
        self.color=GREEN
        
    def make_barrier(self):
        self.color=BLACK
    
    def make_end(self):
        self.color=TURQUOISE
    
    def make_path(self):
        self.color=PURPLE
    
    def draw(self,window):
        pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.width))
        
    def update_neighbors(self,grid):
        self.neighbors=[]
        if self.row<self.total_rows-1 and not grid[self.row+1][self.col].barrier(): #checking Down
            self.neighbors.append(grid[self.row+1][self.col])
        if self.row>0 and not grid[self.row-1][self.col].barrier(): #checking Up
            self.neighbors.append(grid[self.row-1][self.col])
        if self.col>0 and not grid[self.row][self.col-1].barrier(): #checking Left
            self.neighbors.append(grid[self.row][self.col-1]) 
        if self.col<self.total_rows-1 and not grid[self.row][self.col+1].barrier(): #checking Right
            self.neighbors.append(grid[self.row][self.col+1])      
    def __lt__(self,other):
        return False
   