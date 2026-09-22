from random import random
from copy import deepcopy
import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import (QApplication, 
                               QWidget, 
                               QLabel,
                               QPushButton, 
                               QSlider, 
                               QVBoxLayout, QHBoxLayout)

from __feature__ import snake_case, true_property # type: ignore[import-not-found]


type CellType = int

class GOLEngine:

    def __init__(self, width: int = 12, height: int = 8) -> None:
        self.__width: int
        self.__height: int
        self.__current_state: list[list[CellType]]
        self.__new_state: list[list[CellType]]

        # Nombre de voisins              0  1  2  3  4  5  6  7  8
        #                                |  |  |  |  |  |  |  |  |
        self.__dead_rule: tuple[int]  = (0, 0, 0, 1, 0, 0, 0, 0, 0)
        self.__alive_rule: tuple[int] = (0, 0, 1, 1, 0, 0, 0, 0, 0)
        # État courant                     0 = mort          1 = vivant
        self.__rules: tuple[tuple[int]] = (self.__dead_rule, self.__alive_rule)

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

    @property
    def cell_count(self) -> int:
        pass

    @property
    def alive_count(self) -> int:
        pass

    @property
    def dead_count(self) -> int:
        pass

    @property
    def current_generation(self) -> int:
        pass

    def get_cell(self, x: int, y: int) -> CellType:
        return self.__current_state[x][y]

    def set_cell(self, x: int, y: int, cell_value: CellType) -> None:
        self.__current_state[x][y] = cell_value

    def resize(self, width: int, height: int) -> None:
        self.__validate_size(width, "width")
        self.__validate_size(height, "height")

        self.__width = width
        self.__height = height

        self.__current_state = [[0 for _ in range(self.__height)] for _ in range(self.__width)]
        self.__new_state = deepcopy(self.__current_state)

    def randomize(self, percent_on: float = 0.5) -> None:
        for x in range(1, self.__width - 1):
            for y in range(1, self.__height - 1):
                self.__current_state[x][y] = int(random() <= percent_on)

    def process(self) -> None:
        for x in range(1, self.__width - 1):
            for y in range(1, self.__height - 1):
                neighbours: int = sum(self.__current_state[x-1][y-1:y+2]) + \
                                  sum(self.__current_state[x  ][y-1:y+2:2]) + \
                                  sum(self.__current_state[x+1][y-1:y+2])
                self.__new_state[x][y] = self.__rules[self.__current_state[x][y]][neighbours]

        self.__current_state, self.__new_state = self.__new_state, self.__current_state

    def to_string(self) -> str:
        res: str = ""
        for y in range(self.__height):
            for x in range(self.__width):
                res += str(self.__current_state[x][y])
            res += "\n"
        return res
    
class GOLVue(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        control_layout = QVBoxLayout()
        controlTitle = QLabel("Controller")
        startButton = QPushButton("Start", parent)
        stepButton = QPushButton("Next Step", parent)
        speedSlider = QSlider()
        speedSlider.set_range(0, 100)
        speedSlider.value = 25
        speedSlider.orientation = Qt.Orientation.Horizontal
        control_layout.add_widget(controlTitle)
        control_layout.add_widget(startButton)
        control_layout.add_widget(stepButton)
        control_layout.add_widget(speedSlider)

        # startButton.valueChanged.connect(colorValue.setNum)
    #   \_______/                      \______/ 
    #    émetteur                       récepteur
    #             \___________/                  \____/ 
    #              signal émis                    connecteur

        self.set_layout(control_layout)

def main():
    app = QApplication(sys.argv)

    g = GOLEngine()
    g.resize(14, 5)
    g.randomize()
    g.process()
    print(g.to_string())

    w = GOLVue()
    w.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()