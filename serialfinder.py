import json
from typing import Optional, Dict

class SerialNumberFinder:
    """Simple library to look up car component serial numbers."""

    def __init__(self, data_file: str):
        self.serials = self._load_serials(data_file)

    def _load_serials(self, data_file: str) -> Dict[str, str]:
        """Load serial numbers from a JSON data file."""
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def find(self, component: str) -> Optional[str]:
        """Return the serial number for a component or None if not found."""
        return self.serials.get(component.lower())
