from gym.models.simulators import Simulators


class Barbell(Simulators):
    def __init__(self, name, price, colour, exercise, muscles_group, barbell_type):
        super().__init__(name, price, colour, exercise, muscles_group)
        self.barbell_type = barbell_type

    def __del__(self):
        print("Destructor called")
