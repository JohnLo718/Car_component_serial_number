import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Union



class SerialNumberFinder:
    """Helper to look up cars and component serial numbers."""

    @staticmethod
    def _normalize_car(name: str) -> str:
        """Return a normalized car serial."""
        return name.strip().upper()

    @staticmethod
    def _normalize_component(name: str) -> str:
        """Return a normalized component name."""
        return name.strip().lower()

    def __init__(self, data_file: Union[str, Path]):
        self.data_file = Path(data_file)
        with self.data_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        self.cars: Dict[str, List[str]] = {
            self._normalize_car(key): [self._normalize_component(c) for c in comps]
            for key, comps in data.get("cars", {}).items()
        }
        self.components: Dict[str, str] = {
            self._normalize_component(name): serial
            for name, serial in data.get("components", {}).items()
        }

    def get_components(self, car_serial: str) -> Optional[List[str]]:
        """Return list of component names for a car serial."""
        return self.cars.get(self._normalize_car(car_serial))

    def component_serial(self, component: str) -> Optional[str]:
        """Return serial number for a component name."""
        return self.components.get(self._normalize_component(component))

    def add_car(self, car_serial: str, components: List[str]) -> None:
        """Add a new car with a list of components."""
        self.cars[self._normalize_car(car_serial)] = [self._normalize_component(c) for c in components]

    def add_component_to_car(self, car_serial: str, component: str) -> None:
        """Add a component to an existing car."""
        car = self._normalize_car(car_serial)
        comp = self._normalize_component(component)
        self.cars.setdefault(car, [])
        if comp not in self.cars[car]:
            self.cars[car].append(comp)

    def edit_component(self, component: str, serial: str) -> None:
        """Create or update a component serial number."""
        self.components[self._normalize_component(component)] = serial

    def delete_component_from_car(self, car_serial: str, component: str) -> bool:
        """Delete a component from a car. Returns True if removed."""
        car = self._normalize_car(car_serial)
        comp = self._normalize_component(component)
        comps = self.cars.get(car)
        if comps and comp in comps:
            comps.remove(comp)
            return True
        return False

    def delete_car(self, car_serial: str) -> bool:
        """Delete a car entirely. Returns True if removed."""
        car = self._normalize_car(car_serial)
        if car in self.cars:
            del self.cars[car]
            return True
        return False

    def save(self) -> Optional[str]:
        """Persist data back to the JSON file and push to GitHub.

        Returns an error message if the GitHub update fails.
        """
        with self.data_file.open("w", encoding="utf-8") as f:
            json.dump({"cars": self.cars, "components": self.components}, f, indent=2)

