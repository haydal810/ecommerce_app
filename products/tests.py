from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductTest(TestCase):
    """Here we define the tests that we run against our Poduct models """

    def test_str(self):
        test_name = Product(name='A product')
        self. assertEqual(str(test_name), 'A product')
        
