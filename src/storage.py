# src/storage.py

import json
import os

class Storage:
    @staticmethod
    def save(filename, data):
        if not isinstance(data, list):
            return False
        try:
            with open(filename, "w") as f:
                json.dump(data, f)
            return True
        except:
            return False

    @staticmethod
    def load(filename):
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except:
            return []