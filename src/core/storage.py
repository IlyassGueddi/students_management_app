import json
from pathlib import Path

class StorageManager:
    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent.parent
        self.data_dir = self.root / "data"
        self.data_dir.mkdir(exist_ok=True)

        self.files = {
            "students": self.data_dir / "students.json",
            "matieres": self.data_dir / "matieres.json",
            "absences": self.data_dir / "absences.json"
        }

    def _load_generic(self, key):
        """Internal helper to read any JSON file safely."""
        file_path = self.files[key]
        if not file_path.exists():
            return []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []

    def _save_generic(self, key, data):
        """Internal helper to write any JSON file safely."""
        file_path = self.files[key]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


    def load_all_absences(self):
        return self._load_generic("absences")

    def save_absence(self, absence_dict):
        """Adds a new absence to the list and saves it."""
        current_data = self.load_all_absences()
        current_data.append(absence_dict)
        self._save_generic("absences", current_data)

    def load_students(self):
        return self._load_generic("students")