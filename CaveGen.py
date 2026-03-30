from random import randint
class Cave:
    """
    Generates cave-like structures using cellular automata.

    Attributes:
        _N (int): Size of the cave (NxN grid).
        _Temp (int): Initial density of walls (1-100).
        _dx, _dy (list[int]): Neighbor offsets for 8 directions.
        _a (list[list[int]]): Current state of the cave grid.
        _newa (list[list[int]]): Temporary grid used during simulation.
    """
    def __init__(self, N, Temp):
        """
        Initializes the cave grid.

        Args:
            N (int): Size of the cave (NxN).
            Temp (int): Initial wall density (1-100).

        Initializes the cave with random walls and empty spaces
        according to the Temp parameter.
        """
        self._N = N
        self._Temp = Temp
        self._dx = [-1,-1,-1,0,1,1,1,0]
        self._dy = [-1,0,1,1,1,0,-1,-1]
        self._a = [[0]*N for _ in range(N)]
        self._newa = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                self._a[i][j] = self.rnd()

    def Modify(self):
        """
        Updates the cave grid by applying cellular automata rules:
            - Count the number of wall neighbors for each cell.
            - If <=2 neighbors, cell becomes empty (0).
            - If >=6 neighbors, cell becomes wall (1).
            - Otherwise, cell remains the same.
        """
        for i in range(self._N):
            for j in range(self._N):
                self._newa[i][j] = self._a[i][j]
        for i in range(self._N):
            for j in range(self._N):
                d = 0
                for k in range(8):
                    if 0 <= i + self._dx[k] < self._N and 0 <= j + self._dy[k] < self._N:
                        d += self._a[i + self._dx[k]][j + self._dy[k]]
                if d <= 2:
                    self._newa[i][j] = 0
                elif d >= 6:
                    self._newa[i][j] = 1
                else:
                    self._newa[i][j] = self._a[i][j]
        for i in range(self._N):
            for j in range(self._N):
                self._a[i][j] = self._newa[i][j]
    def ReturnCols(self):
        """
        Converts the cave grid into an RGB color grid for visualization.

        Returns:
            list[list[tuple[float,float,float]]]: A 2D list of RGB colors.

        Empty cells are beige, walls are orange-brown, with subtle shading
        based on neighbor density.
        """
        colors = [[(0.0,0.0,0.0)]*self._N for _ in range(self._N)]
        for i in range(self._N):
            for j in range(self._N):
                d = 0.0
                for k in range(8):
                    if 0 <= i + self._dx[k] < self._N and 0 <= j + self._dy[k] < self._N:
                        d += self._a[i + self._dx[k]][j + self._dy[k]]
                d /= 8.0
                if d == 0 or self._a[i][j] == 0:
                    colors[i][j] = (222.0 / 255.0, 198 / 255.0, 175.0 / 255.0)
                else:
                    colors[i][j] = ((181.0 * (1.125 - d)) / 255.0, (90.0 * (1.125 - d)) / 255.0, 0.0)
        return colors
    def rnd(self):
        """
        Generates a random cell value (1 for wall, 0 for empty) based on Temp.

        Returns:
            int: 1 if wall, 0 if empty
        """
        x = randint(0, 100)
        if x <= self._Temp:
            return 1
        return 0
    def simulate(self):
        """
        Runs the cellular automata simulation for 10 iterations
        to generate cave-like structures.
        """
        for i in range(10):
            self.Modify()