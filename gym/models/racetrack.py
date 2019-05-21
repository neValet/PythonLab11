from gym.models.simulators import Simulators


class Racetrack(Simulators):
    def __init__(self, name, price, colour, exercise, muscles_group, speed):
        super().__init__(name, price, colour, exercise, muscles_group)
        self.speed = speed

    def __del__(self):
        print("Destructor called")
