import unittest
import os
from src.storage import Storage

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.filename = "data/test.json"
        self.data = [{"name": "Hilton"}]

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load(self):
        Storage.save(self.filename, self.data)
        loaded = Storage.load(self.filename)
        self.assertEqual(loaded, self.data)

    def test_load_nonexistent_file(self):
        loaded = Storage.load("data/nonexistent.json")
        self.assertEqual(loaded, [])

    def test_save_invalid_data(self):
        Storage.save(self.filename, set([1, 2, 3]))
        self.assertFalse(os.path.exists(self.filename))