class TrainingManager:

    def __init__(self, simulators_list):
        self.simulators_list = simulators_list

    def sort_simulators_list_by_price(self, reverse):
        return sorted(self.simulators_list, key=lambda simulator: simulator.price, reverse=reverse)

    def sort_simulators_list_by_name(self, reverse):
        return sorted(self.simulators_list, key=lambda simulator: simulator.name, reverse=reverse)

    def find_simulator_by_name(self, name):
        return list(filter(lambda simulator: simulator.name == name, self.simulators_list))

