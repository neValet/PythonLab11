from gym.models.simulators import Simulators


class PressTrainingSimulator(Simulators):
    def __init__(self, name, price, colour, exercise, muscles_group, press_part):
        super().__init__(name, price, colour, exercise, muscles_group)
        self.press_part = press_part

    def __del__(self):
        print("Destructor called")
