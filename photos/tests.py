from django.test import TestCase
from .models import Category, Photo

# Create your tests here.
class CategoryTestClass(TestCase):

    def setUp(self):
        self.moringa= Category(name = 'Food')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.moringa,Category))

class PhotoTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.moringa= Category(name='Food')
        self.moringa.save_category()

        # Creating a new tag and saving it
        self.new_category= Photo()
        self.new_category.save()

        self.new_category.photos.add(self.new_photo)
    

    def __str__(self):
        return self.name

    def save_editor(self):
        self.save()