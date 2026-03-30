import matplotlib.pyplot as plt
import matplotlib.patches as patches
class Draw:
    """
    Handles visualization of a cave grid using matplotlib.

    Attributes:
        _N (int): Size of the grid.
        _colors (list[list[tuple[float,float,float]]]): 2D list of RGB colors.
    """
    def __init__(self, colors, N):
        """
        Initializes the Draw object.

        Args:
            colors (list[list[tuple]]): 2D RGB color grid to display.
            N (int): Size of the grid.
        """
        self._N = N
        self._colors = colors

    def Show(self):
        """
        Displays the cave grid using matplotlib patches.

        Each cell is drawn as a square colored according to _colors.
        """
        fig, ax = plt.subplots()
        cell_size = 1
        for i in range(self._N):
            for j in range(self._N):
                rect = patches.Rectangle((j, i), cell_size, cell_size, facecolor=self._colors[i][j])
                ax.add_patch(rect)
        ax.set_xlim(0, self._N)
        ax.set_ylim(0, self._N)
        ax.set_aspect('equal')
        plt.gca().invert_yaxis()
        plt.show()