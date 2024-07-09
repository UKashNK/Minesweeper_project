"""This is to draw the board at any given time"""
import random as rd

class Cell():
    """ Class to define cell objects, their functions and attributes"""
    def __init__(self, location, is_bomb):
        #Define attributes of the cell
        self.location = location
        self.is_bomb = is_bomb
        self.explode = False
        self.num_bomb_neighbours = 0

        #Change the attrinutes of the cell if it is a bomb
        if self.is_bomb == True:
            self.num_bomb_neighbours = None
            self.explode = True

        #Define the locations of the cells neighbours
        self.neighour_locations = [[size[0]-1, size[1]-1],
                                   [size[0]-1, size[1]-0],
                                   [size[0]-1, size[1]+1],

                                   [size[0]-0, size[1]-1],
                                   [size[0]-0, size[1]+1],

                                   [size[0]+1,size[1]-1],
                                   [size[0]+1,size[1]-0],
                                   [size[0]+1,size[1]+1],
                                   ]



    def countBombNeighbours(self):
        """ Counts the neighbours that are bombs"""
        if self.is_bomb == False:
            count = 0
            for  neighbour_location in self.neighour_locations:
                if neighbour_location in Bombs:
                    count += 1
            return count

    def actions(self):
        """ End the game if the cell is a bomb"""
        if self.explode == True:
            action = "EXPLODE"
        else:
            action = "REVEAL"
        return action


def drawStart(size,bombs):
    """Size must be a list containing length and width of the board being drawn"""
    board_size = size[0]*size[1] # Calculates the size of the board from the dimensions given
    if bombs < board_size: # determines the number of bombs to be placed on the board
        nBombs = bombs
    else:
        nBombs = board_size

    #Randomly deciding which cells are bombs
    Bombs = []
    while len(Bombs) < nBombs:
        cordinates = [rd.randrange(0,size[0]+1,1), rd.randrange(0,size[1]+1,1)]
        if cordinates not in Bombs:
            Bombs.append(cordinates)
        else:
            pass

    return Bombs

def popCell(location):
    """Play a cell i.e. Display the number in the cell or explode the cell"""
    if location in Bombs:
        is_bomb=True
    else:
        is_bomb=False

    #Define the cell being played
    cell = Cell(location=location, is_bomb=is_bomb)
    Action = cell.actions() # get the action for the cell

    if Action == "EXPLODE":
        print("Game over!!! That was a mine")
    else:
        display_number = cell.countBombNeighbours() #Get neighbours that are bombs
        print(f"{display_number} neighbours are mines")

    return Action

status = "playing"
while status == "playing":
    #get the board's parameters
    length = int(input("Length of the Board:"))
    width = int(input("Width of the Board:"))
    bombs = int(input("Number of Bombs:"))
    size = [length,width]
    #Draw the board basing on given parameters
    Bombs = drawStart(size, bombs)
    print(Bombs)
    #start playing game
    player_status = "Alive"
    while player_status=="Alive":
        action = popCell([int(input(f"X cordinate of cell being played(0-{length}):")),
                          int(input(f"Y cordinate of cell being played(0-{width}):")),
                          ])
        if action == "EXPLODE":
            player_status = "Dead"
        else:
            pass
