from gym.models.simulators import Simulators


class Dumbbells(Simulators):
    def __init__(self, name, price, colour, exercise, muscles_group, weight):
        super().__init__(name, price, colour, exercise, muscles_group)
        self.weight = weight

    def __del__(self):
        print("Destructor called")
