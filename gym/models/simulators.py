class Simulators:
    def __init__(self, name, price, colour, exercise, muscles_group):
        self.name = name
        self.price = price
        self.colour = colour
        self.exercise = exercise
        self.musclesGroup = muscles_group

    def __del__(self):
        print("Destructor called")
