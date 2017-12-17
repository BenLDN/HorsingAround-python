#Conway's game of life implemeted in Python 3 from scratch
#Using Turtle

import random
from turtle import *
hideturtle()

#Generate a random grid with c columns and r rows
#The grid is stored in a 2D list
#Each cell has 50% chance of being live in the random grid
#1 means alive, 0 means dead

def generate_random_grid(r,c):
    randomGrid=[]
    for j in range(0,r):
        randomGrid.append([])
        for i in range(0,c):
            if random.randint(0,1)==1:
                randomGrid[j].append(0)
            else:
                randomGrid[j].append(1)    
    return randomGrid

#drawing the grid with the turtle
#the grid is defined by a 2D list
#draw a frame & iterate through rows and colums
#if i,j cell is live (1) put a dot on the screen

def draw_grid(grid):
    zoom=10
    tracer(False)
    clear()
    rows=len(grid)
    cols=len(grid[0])

    #drawing frame
    setpos(0-cols*zoom/2+zoom/2,0+rows*zoom/2+zoom/2)
    pendown()
    for counter in range(0,4):
        forward(cols*zoom)
        right(90)
    penup()

    #drawing cells
    setpos(0-cols*zoom/2,0+rows*zoom/2)    
    for j in range(0,rows):
        for i in range(0,cols):
            forward(zoom)
            if grid[j][i]==1:
                dot(zoom)
        right(90)
        forward(zoom)
        right(90)
        forward(cols*zoom)
        right(180)
    tracer(True)

#calculate next generation of the grid
#the current (old) grid is defined by a 2D list
#iterate through rows and columns and count live neighbours
#apply Conway's rules and build a new 2D list that defines the next generation
#return the new 2D list
    
def next_gen(oldGrid):
    rows=len(oldGrid)
    cols=len(oldGrid[0])
    newGrid=[]
    for j in range(0,rows):
        newGrid.append([])
        for i in range(0,cols):

            #Counting live neighbours
            #If conditions: to prevent looking at position (-1) which
            #               would be the last item of the list
            #try/except: to prevent overflows at the edges
            
            cell_n=0

            if (i>0) and (j>0):
                try: cell_n+=oldGrid[j-1][i-1]
                except IndexError: pass                
            
            if i>0:
                try: cell_n+=oldGrid[j][i-1]
                except IndexError: pass
                try: cell_n+=oldGrid[j+1][i-1]
                except IndexError: pass

            if j>0:            
                try: cell_n+=oldGrid[j-1][i]
                except IndexError: pass
                try: cell_n+=oldGrid[j-1][i+1]
                except IndexError: pass

            try: cell_n+=oldGrid[j][i+1]
            except IndexError: pass
            try: cell_n+=oldGrid[j+1][i]
            except IndexError: pass
            try: cell_n+=oldGrid[j+1][i+1]
            except IndexError: pass

            #Build the new grid (2D list) by applyinh GoL rules
            
            if oldGrid[j][i]==0:
                if cell_n==3:
                    newGrid[j].append(1)
                else:
                    newGrid[j].append(0)
            else:
                if (cell_n<2) or (cell_n)>3:
                    newGrid[j].append(0)
                else:
                    newGrid[j].append(1)
        
    return newGrid

#Main loop
#Generate random grid
#Calculate next generation and update the grid

def main():
    theGrid=generate_random_grid(50,50)
    for it in range(0,100):
        draw_grid(theGrid)
        prevGrid=theGrid
        theGrid=next_gen(prevGrid)

if __name__=="__main__":
    main()
