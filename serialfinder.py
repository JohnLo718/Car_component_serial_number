import json
from typing import Optional, Dict, List

class SerialNumberFinder:
    """Helper to look up cars and component serial numbers."""

    def __init__(self, data_file: str):
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.cars: Dict[str, List[str]] = {
            key.upper(): [c.lower() for c in comps]
            for key, comps in data.get('cars', {}).items()
        }
        self.components: Dict[str, str] = {
            name.lower(): serial
            for name, serial in data.get('components', {}).items()
        }

    def get_components(self, car_serial: str) -> Optional[List[str]]:
        """Return list of component names for a car serial."""
        return self.cars.get(car_serial.upper())

    def component_serial(self, component: str) -> Optional[str]:
        """Return serial number for a component name."""
        return self.components.get(component.lower())
