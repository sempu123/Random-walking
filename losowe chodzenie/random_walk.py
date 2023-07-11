from random import choice


class RandomWalk():
    """Klasa generuje losowe chodzenie"""

    def __init__(self, num_points=5000):
        """Inicjalizacja atrybutów"""
        self.num_points = num_points

        # Punkty początkowe
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """generowanie punktów w losowym chodzeniu"""

        # Wykonywanie kroków az do osiagniecia limitu
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            # odrzucenie ruchów do nikąd
            if x_step == 0 and y_step == 0:
                continue

            # Ustalenie następnych wartosci X i Y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
