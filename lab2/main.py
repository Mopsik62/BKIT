from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from prettytable import PrettyTable

N = 15

def main():
    r = Rectangle(N, N, "синего")
    c = Circle(N, "зеленого")
    s = Square(N, "красного")
    print(r)
    print(c)
    print(s)

    x = PrettyTable()
    x.field_names = ["Название фигуры", "Цвет фигуры", "Площадь фигуры"]
    x.add_rows([
        ["Прямоугольник", r._figure_color.colorproperty, r.get_area()],
        ["Круг", c._figure_color.colorproperty, c.get_area()],
        ["Квадрат", s._figure_color.colorproperty, s.get_area()]
    ])
    print(x)

if __name__ == "__main__":
    main()