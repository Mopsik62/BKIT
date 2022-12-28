from abc import ABC, abstractmethod
class Figure(ABC):
    """
        Абстрактный класс «Геометрическая фигура»
        """
    @abstractmethod
    def get_area(self):
        """
                содержит виртуальный метод для вычисления площади фигуры.
                """
        pass