from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    """
       Класс «Квадрат» наследуется от класса «Прямоугольник».
       """
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, side, color):
        """
                Класс должен содержать конструктор по параметрам «сторона» и «цвет».
                """
        self._side = side
        super().__init__(side, side, color)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self._figure_color.colorproperty,
            self._side,
            self.get_area()
        )