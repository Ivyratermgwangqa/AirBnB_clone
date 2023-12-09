import unittest
import sys
import os

# Adjust the path to include the project root directory
sys.path.append(os.path.abspath('..'))

from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_instance_creation(self):
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertEqual(len(self.base_model.id), 36)  # UUID length

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_str_representation(self):
        str_representation = str(self.base_model)
        self.assertIsInstance(str_representation, str)
        self.assertIn('BaseModel', str_representation)
        self.assertIn(self.base_model.id, str_representation)

    def test_reload_method(self):
        self.base_model.save()
        storage_path = 'file.json'
        self.assertTrue(os.path.isfile(storage_path))

        # Creating a new BaseModel to clear the objects
        new_base_model = BaseModel()
        new_base_model.save()

        # Reload the data from file
        new_base_model.reload()

        # Check if the old model is in the dictionary
        self.assertIn(self.base_model.id, new_base_model.all())

if __name__ == '__main__':
    unittest.main()
