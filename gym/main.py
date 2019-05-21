from gym.enums.barbell_types import BarbellTypes
from gym.enums.muscles_group import MusclesGroup
from gym.enums.press_part import PressPart
from gym.managers.training_manager import TrainingManager
from gym.models.barbell import Barbell
from gym.models.dumbbells import Dumbbells
from gym.models.press_training_simulator import PressTrainingSimulator
from gym.models.racetrack import Racetrack


def main():
    barbell = Barbell("barbell", 150, "silver", "barbell_lifting", MusclesGroup.CHEST, BarbellTypes.OLYMPIC)
    dumbbells = Dumbbells("dumbbells", 200, "silver", "dumbbells_lifting", MusclesGroup.HANDS, 8)
    press_training_simulator = PressTrainingSimulator("press training simulator", 400, "black", "press_lifting",
                                                       MusclesGroup.PRESS, PressPart.MIDDLE_PRESS)
    racetrack = Racetrack("racetrack", 1000, "white", "jogging", MusclesGroup.LEGS, 10)

    simulators = [barbell, dumbbells, press_training_simulator, racetrack]
    manager = TrainingManager(simulators)

    print("\n", manager.sort_simulators_list_by_price(False))
    print("\n", manager.sort_simulators_list_by_name(True))
    print("\n", manager.find_simulator_by_name("racetrack"))


if __name__ == '__main__':
    main()
