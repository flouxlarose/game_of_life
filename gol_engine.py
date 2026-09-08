from random import random
from copy import deepcopy


type CellType = int

class GOLEngine:

    def __init__(self, width: int = 12, height: int = 8) -> None:
        self.__width: int
        self.__height: int
        self.__current_state: list[list[CellType]]
        self.__new_state: list[list[CellType]]
        #                                0  1  2  3  4  5  6  7  8
        self.__alive_rule: tuple[int] = (0, 0, 1, 1, 0, 0, 0, 0, 0)
        self.__dead_rule:  tuple[int] = (0, 0, 0, 1, 0, 0, 0, 0, 0)
        self._rules: tuple[tuple[int]] = (self.__dead_rule, self.__alive_rule)

        self.resize(width, height)

    def __validate_size(self, size: int, text_info: str) -> None:
        if not isinstance(size, int):
            raise TypeError(f"{text_info} doit être un entier")
        if size < 3 or size > 5000:
            raise ValueError("la valeur de {text_info} doit être entre 3 et 5000")

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        self.resize(value, self.__height)

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        self.resize(self.__width, value)

    def get_cell(self, x: int, y: int) -> CellType:
        return self.__current_state[x][y]

    def set_cell(self, x: int, y: int, cell_value: CellType) -> None:
        self.__current_state[x][y] = cell_value

    def resize(self, width: int, height: int) -> None:
        self.__validate_size(width, "width")
        self.__validate_size(height, "height")

        self.__width = width
        self.__height = height

        self.__current_state = [[0 for _ in range(self.__height)]for _ in range(self.__width)]
        # version moins efficace
        # self.__current_state = []
        # for x in range(self.__width):
        #     self.__current_state.append([])
        #     for _ in range(self.__height):
        #         self.__current_state[x].append(0)
        self.__new_state = deepcopy(self.__current_state)

    def randomize(self, percent_on: float = 0.5) -> None:
        for x in range(1, self.__width - 1):
            for y in range(1, self.__height - 1):
                self.__current_state[x][y] = int(random() <= percent_on)

    def process(self) -> None:
        for x in range(1, self.__width - 1):
            for y in range(1, self.__height - 1):
                neighbours: int = sum(self.__current_state[x-1][y-1:y+2]) + \
                                  sum(self.__current_state[x+1][y-1:y+2]) + \
                                  sum(self.__current_state[x][y-1:y+2:2])
                self.__new_state[x][y] = self._rules[self.__current_state[x][y]][neighbours]
                # MOIN EFFICACE (ligne 76)
                # if bool(self.__current_state[x][y]): # vivant
                #     self.__new_state[x][y] = int(neighbours in (2, 3))
                # else: # mort
                #     self.__new_state[x][y] = int(neighbours == 3)

        self.__current_state, self.__new_state = self.__new_state, self.__current_state

    def to_string(self) -> str:
        res: str = ""
        for y in range(self.__height):
            for x in range(self.__width):
                res += str(self.__current_state[x][y])
            res += "\n"
        return res



g = GOLEngine()
g.resize(14, 5)
g.randomize()
print(g.to_string())
g.process()
print(g.to_string())
pass
  