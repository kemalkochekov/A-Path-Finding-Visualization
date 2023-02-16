import pygame
from queue import PriorityQueue


def H(point1,point2):
    x1,y1=point1
    x2,y2=point2
    return abs(x2-x1)+abs(y2-y1)
    #distance between two points

def final_path(came_from,current,draw):
    while current in came_from:
        current=came_from[current]
        current.make_path()
        draw()

def algorithm(draw,grid,start,end):
    open_set=PriorityQueue()
    
    count=0
    open_set=PriorityQueue()
    open_set.put((0,count,start))
    came_from={}
    g_score={spot: float("inf") for row in grid for spot in row}
    g_score[start]=0
    f_score={spot: float("inf") for row in grid for spot in row}
    f_score[start]=H(start.get_pos(),end.get_pos())
    open_set_hash={start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current=open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            final_path(came_from,end,draw)
            end.make_end()
            start.make_start()
            return True
        for neighbor in current.neighbors:
            temp_g_score=g_score[current]+1
            if temp_g_score<g_score[neighbor]:
                came_from[neighbor]=current
                g_score[neighbor]=temp_g_score
                f_score[neighbor]=temp_g_score+H(neighbor.get_pos(),end.get_pos())
                if neighbor not in open_set_hash:
                    count+=1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        
        if current!=start:
            current.make_closed()
    return False
