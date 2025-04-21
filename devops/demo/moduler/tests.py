from django.test import TestCase
from .models import MyModel
# Create your tests here.

class MyModelTestCase(TestCase):
    
    def test_models(self):
        obj=MyModel.objects.create(name="Test Object")
        self.assertEqual(obj.name, "Test Object")
        self.assertTrue(MyModel.objects.exists())
