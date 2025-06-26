import json
from pathlib import Path
from typing import Dict, List, Optional, Union
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit

=======
from typing import Optional, Dict, List
>>>>>>> main

class SerialNumberFinder:
    """Helper to look up cars and component serial numbers."""

    def __init__(self, data_file: Union[str, Path]):
        self.data_file = Path(data_file)
        with self.data_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        self.cars: Dict[str, List[str]] = {
            key.upper(): [c.lower() for c in comps]
            for key, comps in data.get("cars", {}).items()
        }
        self.components: Dict[str, str] = {
            name.lower(): serial for name, serial in data.get("components", {}).items()
        }

<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
=======
    def __init__(self, data_file: str):
        self.data_file = data_file
        with open(data_file, "r", encoding="utf-8") as f:
            for key, comps in data.get("cars", {}).items()
            name.lower(): serial for name, serial in data.get("components", {}).items()
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump({"cars": self.cars, "components": self.components}, f, indent=2)
        }
        self.components: Dict[str, str] = {
            name.lower(): serial
            for name, serial in data.get('components', {}).items()
        }

        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.cars: Dict[str, List[str]] = {
                k.upper(): [c.lower() for c in comps]
                for k, comps in data.get('cars', {}).items()
            }
            self.components: Dict[str, str] = {
                name.lower(): serial
                for name, serial in data.get('components', {}).items()
            }

>>>>>>> main
    def get_components(self, car_serial: str) -> Optional[List[str]]:
        """Return list of component names for a car serial."""
        return self.cars.get(car_serial.upper())

    def component_serial(self, component: str) -> Optional[str]:
        """Return serial number for a component name."""
        return self.components.get(component.lower())

    def add_car(self, car_serial: str, components: List[str]) -> None:
        """Add a new car with a list of components."""
        self.cars[car_serial.upper()] = [c.lower() for c in components]

    def add_component_to_car(self, car_serial: str, component: str) -> None:
        """Add a component to an existing car."""
        car = car_serial.upper()
        comp = component.lower()
        self.cars.setdefault(car, [])
        if comp not in self.cars[car]:
            self.cars[car].append(comp)

    def edit_component(self, component: str, serial: str) -> None:
        """Create or update a component serial number."""
        self.components[component.lower()] = serial

    def delete_component_from_car(self, car_serial: str, component: str) -> bool:
        """Delete a component from a car. Returns True if removed."""
        car = car_serial.upper()
        comp = component.lower()
        comps = self.cars.get(car)
        if comps and comp in comps:
            comps.remove(comp)
            return True
        return False

    def delete_car(self, car_serial: str) -> bool:
        """Delete a car entirely. Returns True if removed."""
        car = car_serial.upper()
        if car in self.cars:
            del self.cars[car]
            return True
        return False

    def save(self) -> None:
        """Persist data back to the JSON file."""
        with self.data_file.open("w", encoding="utf-8") as f:
            json.dump({"cars": self.cars, "components": self.components}, f, indent=2)
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
=======
        if car not in self.cars:
            self.cars[car] = []
        self.cars[car].append(comp)

    def edit_component(self, component: str, serial: str) -> None:
        """Overwrite/update a component serial number."""
        self.components[component.lower()] = serial

    def save(self) -> None:
        """Persist data back to the JSON file."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump({'cars': self.cars, 'components': self.components}, f, indent=2)
>>>>>>> main
