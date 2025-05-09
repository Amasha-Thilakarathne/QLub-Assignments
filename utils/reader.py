import yaml
import os

class LocatorReader:
    def __init__(self):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        locators_path = os.path.join(base_path, "configs", "locators.yaml")
        with open(locators_path, "r") as file:
            self.locators = yaml.safe_load(file)

    def get(self, page, element):
        return self.locators[page][element]
