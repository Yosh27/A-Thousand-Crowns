# Code for automating the map

WARN = '⚠️'
ERR = '❌'
CHECK = '✔'

class Graph:
    def __init__(self, x = 1000, y = 1000):
        self.x = x
        self.y = y
        self.graph = list()

    @property
    def graph(self):
        for i in range(self.x):
            self.graph += [None]

            for j in range(self.y):
                self.graph[i] += [None]

    def placeIcon(self, x, y, icon):
        if not x.isinstance(int) or not y.isinstance(int) or icon.isinstance(str):
            return ERR

        self.graph[x][y] = icon

    '''
    This method is just for ease of access. If people don't feel like scrolling up all the 
    way to find where they put an icon, they could use this to find it.
    '''
    def findIcon(self, SID, icon): #Sector ID (SID) refers to a numerical representation of part of the grid where SID == xy, and x and y refer to an area 1/10 as large as the side lengths
        rightX = (SID // 10) * 100 - 1
        leftX = (SID // 10 - 1) * 100
        bottomY = (SID % 10) * 100 - 1
        topY = (SID % 10 - 1) * 100

        for i in range(leftX, rightX):
            for j in range(topY, bottomY):
                if icon in self.graph[i][j]:
                    return f"{icon} at coordinates {i}, {j}."

        return f"{icon} does not exist in SID {SID}."

    def removeIcon(self, x, y, icon):
        if icon in self.graph[x][y]:
            self.graph[x][y] = None
        
        else:
            return f"There is no {icon} at those coordinates."