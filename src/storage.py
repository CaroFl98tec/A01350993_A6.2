import json
import os


class StorageManager:
    """Handles JSON file operations with error handling."""

    @staticmethod
    def read_file(file_path):
        """Read data from a JSON file."""
        if not os.path.exists(file_path):
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error reading file {file_path}: {error}")
            return []

    @staticmethod
    def write_file(file_path, data):
        """Write data to a JSON file."""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except IOError as error:
            print(f"Error writing file {file_path}: {error}")