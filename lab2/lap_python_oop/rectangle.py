from lab_python_oop.figure import Figure
from lab_python_oop.figure_color import Figure_color
class Rectangle(Figure):
    """
        Класс «Прямоугольник» наследуется от класса «Геометрическая фигура».
        """
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        """
                Класс должен содержать конструктор по параметрам «ширина», «высота» и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета.
                """
        self._figure_color = Figure_color()
        self._width = width
        self._height = height
        self._figure_color.colorproperty = color

    def get_area(self):
        """
                Класс должен переопределять метод, вычисляющий площадь фигуры.
                """
        return self._width * self._height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self._figure_color.colorproperty,
            self._width,
            self._height,
            self.get_area()
        )