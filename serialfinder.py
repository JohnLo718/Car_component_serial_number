import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Union

from github import Github
from github.GithubException import GithubException

REPO_NAME = "JohnLo718/Car_component_serial_number"
DATA_FILE_REPO_PATH = "data/serial_numbers.json"
COMMIT_MESSAGE = "Auto update from Streamlit app"


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

    def save(self) -> Optional[str]:
        """Persist data back to the JSON file and push to GitHub.

        Returns an error message if the GitHub update fails.
        """
        with self.data_file.open("w", encoding="utf-8") as f:
            json.dump({"cars": self.cars, "components": self.components}, f, indent=2)
        return push_to_github(self.data_file)


def push_to_github(file_path: Path) -> Optional[str]:
    """Commit and push the given file to GitHub.

    Returns an error message on failure or None on success.
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return "GITHUB_TOKEN not set"

    try:
        g = Github(token)
        repo = g.get_repo(REPO_NAME)
        with file_path.open("r", encoding="utf-8") as f:
            content = f.read()
        contents = repo.get_contents(DATA_FILE_REPO_PATH, ref="main")
        repo.update_file(contents.path, COMMIT_MESSAGE, content, contents.sha, branch="main")
    except GithubException as e:
        return str(e)
    except Exception as e:
        return str(e)
    return None
