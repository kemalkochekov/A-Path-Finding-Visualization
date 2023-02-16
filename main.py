import pygame
import math
from queue import PriorityQueue
from Node import Node,GREY
from Dijiktra import algorithm

w=800

window=pygame.display.set_mode((w,w))
pygame.display.set_caption("A Path Finding Algorithm")


def make_grid(rows,width):
    grid=[]
    gap=width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot=Node(i, j, gap, rows)
            grid[i].append(spot)    
    return grid

def draw_grid(window,rows,width):
    GAP=width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0,i*GAP),(width,i*GAP)) 
        for j in range(rows):
            pygame.draw.line(window, GREY, (j*GAP,0),(j*GAP,width))

def draw_all(window,grid,rows,width):
    # window.fill(WHITE)
    
    for row in grid:
        for spot in row:
            spot.draw(window)
    draw_grid(window, rows, width)
    pygame.display.update()
    
def get_click_pos(pos,rows,width):
    gap=width // rows
    y,x = pos
    row=y // gap
    col=x // gap
    return row, col    

def main(window,width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    while(run):
        draw_all(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 run=False
            if pygame.mouse.get_pressed()[0]: #Left
                pos=pygame.mouse.get_pos()
                row,col=get_click_pos(pos, ROWS, width)
                spot=grid[row][col]
                if not start and spot!=end:
                    start=spot
                    start.make_start()
                elif not end and spot!=start:
                    end=spot
                    end.make_end()
                elif spot!=end and spot!=start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]: #Right
                pos=pygame.mouse.get_pos()
                row,col=get_click_pos(pos, ROWS, width)
                spot=grid[row][col]
                spot.reset()
                if spot==start:
                    start=None
                if spot==end:
                    end=None
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(lambda: draw_all(window,grid,ROWS,width),grid,start,end)
                if event.key==pygame.K_c:
                    start=None
                    end=None
                    grid=make_grid(ROWS, width)   
            
    pygame.quit()
    
main(window, w)