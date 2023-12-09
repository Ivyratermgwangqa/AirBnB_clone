import unittest
import sys
import os

# Adjust the path to include the project root directory
sys.path.append(os.path.abspath('..'))

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        del self.base_model
        del self.storage

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
        # Create a new instance of FileStorage
        new_storage = FileStorage()
        
        print("Before reload:", new_storage.all())
        # Save the current base_model to the new storage
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        new_storage.all()[key] = self.base_model.to_dict()
        new_storage.save()
        
        print("After save:", new_storage.all())
        
        # Clear the current instance of BaseModel
        del self.base_model
        # Create a new instance of BaseModel
        new_base_model = BaseModel()
        
        # Reload the new_base_model from the new_storage
        new_base_model.reload(new_storage)
        
        print("After reload:", new_storage.all())
        # Assert that the reloaded base_model is in the storage
        self.assertIn(new_base_model.id, new_storage.all())

if __name__ == '__main__':
    unittest.main()
