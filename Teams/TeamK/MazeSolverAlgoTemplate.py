
"""
This class is the template class for the Maze solver
"""

import sys
from math import sqrt
import numpy
import queue
from queue import *

class MazeSolverAlgoTemplate:

    EMPTY = 0       # empty cell
    OBSTACLE = 1    # cell with obstacle / blocked cell
    START = 2       # the start position of the maze (red color)
    TARGET = 3      # the target/end position of the maze (green color)

    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.dimCols = 0 
        self.dimRows = 0 
        self.setStartCol = 0 
        self.setStartRow = 0 
        self.setEndCol = 0 
        self.setEndRow = 0 
        self.grid=[[]]            
        print("Initialize a Maze Solver")


    # Setter method for the maze dimension of the rows
    def setDimRowsCmd(self, rows):
        self.rows = rows

    # Setter method for the maze dimension of the columns
    def setDimColsCmd(self, cols):
        self.columns = cols
        
    # Setter method for the column of the start position 
    def setStartColCmd(self, col):
        self.colums = col

    # Setter method for the row of the start position 
    def setStartRowCmd(self, row):
        self.rows = row

    # Setter method for the column of the end position 
    def setEndColCmd(self, col):
        self.columns = col

    # Setter method for the row of the end position 
    def setEndRowCmd(self, row):
        self.rows = row

    # Setter method for blocked grid elements
    def setBlocked(self,row ,col):
        self.rows = row
        self.columns = col

    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self):
        # TODO: this is you job now :-)
        self.setDimRows = 0
        self.setDimCols = 0
        self.setStartCol = 0
        self.setStartRow = 0
        self.setEndCol = 0
        self.setEndRow = 0
        self.grid[[]]

    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self, columns=0, rows=0):
        # TODO: this is you job now :-)
        #HINT: populate grid with dimension row,column with zeros
        self.setDimRows = EMPTY
        self.setDimCols = EMPTY
        self.setStartCol = EMPTY
        self.setStartRow = EMPTY
        self.setEndCol = EMPTY
        self.setEndRow = EMPTY
        self.grid[[]]

        if columns>EMPTY and rows>EMPTY:
            self.grid = numpy.empty((rows, columns), dtype=int)
            for i in range(rows):
                for j in range(columns):
                    self.grid[i][j]=EMPTY

    # Define what shall happen after the full information of a maze has been received
    def endMaze(self):
        # HINT: did you set start position and end position correctly?
        self.grid[self.setStartRow][self.setStartCol] = self.START
        self.grid[self.setEndRow][self.setEndCol] = self.TARGET

    # just prints a maze on the command line
    def printMaze(self):
        print(self.grid)

    # loads a maze from a file pathToConfigFile 
    def loadMaze(self,pathToConfigFile):
        # check whether a function numpy.loadtxt() could be useful
        self.grid=numpy.loadtxt(pathToConfigFile, delimiter=',',dtype=int)
        self.setDimCols=self.grid.shape[0]
        
        self.setDimRows=self.grid.shape[1]
        start_arr = numpy.where(self.grid == 2)
        self.setStartRow=int(start_arr[0][0])
        self.setStartCol=int(start_arr[1][0])

        end_arr = numpy.where(self.grid == 3)
        self.setEndRow=int(end_arr[0][0])
        self.setEndCol=int(end_arr[1][0])
 
        

    # clears the complete maze 
    def clearMaze(self):
        self.startMaze()
        
  
    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self,row,column):
        if row < 0:
            return False
        if column < 0:
            return False
        if row >= self.grid.shape[0]:
            return False
        if column >= self.grid.shape[1]:
            return False
        return True        


    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self,row,column):
        # TODO: this is you job now :-)
        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage
        neighbours = []

        # no neighbours for out-of-grid elements
        if self.isInGrid(row,column) == False:
            return neighbours

        # no neighbours for blocked grid elements
        if self.grid[row,column] == self.OBSTACLE:
            return neighbours
    
        nextRow = row + 1    
        if (self.isInGrid(nextRow,column) is True and self.grid[nextRow][column] != self.OBSTACLE):
            neighbours.append([nextRow,column])

        previousRow = row - 1    
        if (self.isInGrid(previousRow,column) is True and self.grid[previousRow][column] != self.OBSTACLE):
            neighbours.append([previousRow,column])

        nextColumn = column + 1    
        if (self.isInGrid(row,nextColumn) is True and self.grid[row][nextColumn] != self.OBSTACLE):
            neighbours.append([row,nextColumn])

        previousColumn = column - 1    
        if (self.isInGrid(row,previousColumn) is True and self.grid[row][previousColumn] != self.OBSTACLE):
            neighbours.append([row,previousColumn])

        return neighbours

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self,row,col):
        # TODO: this is you job now :-)
        # HINT: this method is used as primary key in a lookup table
        result = ""
        result += str(row)
        result += ","
        result += str(col)
        return result
    
    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        pass

    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]
    def heuristic(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        pass

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self,came_from):
        # TODO: this is you job now :-)
        # HINT: this method is a bit tricky as you have to invert the came_from list (follow the path from end to start)
        pass

    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    def myMazeSolver(self):
        # TODO: this is you job now :-)
        pass

    # Command for starting the solving procedure
    def solveMaze(self):
        return self.myMazeSolver()


if __name__ == '__main__':
    mg = MazeSolverAlgoTemplate()

    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    mg.loadMaze("C:\\Users\\Kim-Ly\\MazeRunner\\MazeExamples\\maze1.txt")
    neighbor = mg.getNeighbours(2,4)
    print(neighbor)
    #solutionString = mg.solveMaze()
    #print(solutionString)
    mg.printMaze()