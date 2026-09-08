import random
from copy import deepcopy
type CellType = int

class GOLEngine:    
    def __init__(self, width: int = 12, height: int = 8) -> None:
        self.__width = width
        self.__height = height
        self.__grid=[]
        for x in range(self.width):
            for _ in range(self.__height):
                self.__grid[x].append(0)

        self.__grid_futur = deepcopy(self.__grid)
        

    def validate_size(self, size, text_info) -> None:
        if not isinstance(size, int):
            raise TypeError(f"{text_info} doit être un entier")
        if size < 3 or size > 5000:
            raise ValueError(f"la valeur de {text_info} doit être entre 3 et 5000")

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        self.validate_size(value, "width")
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        self.validate_size(value, "height")
        self.__height = value


    def get_cell(self, x:int, y:int) -> CellType:
        return self.__grille[[x,y]]

    def set_cell(self, x:int, y:int, cell:CellType) -> None:
        self.__grille[[x,y]] = cell

    def resize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def randomize(self, percent_on: float = 0.5) -> None:
        for x in range(self.width):
            for y in range(self.height):
                if (random.random() <= percent_on):
                    self.set_cell(x, y, 1)

        # CODE DU PROF
        # for x in range(1, self.__width - 1):
        #     for y in range(1, self.__height - 1):
        #           self.__current_state[x][y] = int(random() <= percent_on else 0)

    def to_string(self):
        pass
        # CODE DU PROF
        # res: str = ""
        # for y in range(self.__height):
        #     for x in range(self.__width):
        #         res += str(self.__currentstate[x][y])
        #     res += "\n"
        # return res

    def tick(self) -> None:
        row = len(self.grille)
        col = len(self.grille[0])

        for y in range(row):
            for x in range(col):
                cell_value = self.grille[y][x]
                next_status = cell_value
                # regle 1
                cell_alive = self.check_neighbours(x, y)

                if(not cell_value and cell_alive == 3):
                    next_status = 1
                elif (cell_value and cell_alive < 2 or cell_alive > 3):
                    next_status = 0
                
                self.__grille_futur[y][x] = next_status

        # CODE DU PROF
        # for x in range(1, self.__width - 1):
        #     for y in range(1, self.__height - 1):
        #         neighbours: int = 0
        #         for i in range(-1, 2):
        #             for j in range(-1, 2):
        #                 if i != 0 or j != 0:
        #                     neighbours += self.__current_state[x+i][y+j]
        #         if self.__current_state[x][y] == 0: #mort
        #             self.__new_state[x][y] = int(neighbours == 3)
        #         else: # vivant
        #             self.__new_state[x][y] = int(neighbours in (2,3))


        

                

    def check_neighbours(self, x, y) -> int:
        counter_cell_alive = 0
        if self.grille[y-1][x - 1]:
            counter_cell_alive += 1
        if self.grille[y-1][x]:
            counter_cell_alive += 1
        if self.grille[y-1][x + 1]:
            counter_cell_alive += 1
        if self.grille[y][x - 1]:
            counter_cell_alive += 1
        if self.grille[y][x + 1]:
            counter_cell_alive += 1
        if self.grille[y + 1][x - 1]:
            counter_cell_alive += 1
        if self.grille[y + 1][x]:
            counter_cell_alive += 1
        if self.grille[y + 1][x + 1]:
            counter_cell_alive += 1
        
        return counter_cell_alive

    def to_string(self) -> str:
        pass