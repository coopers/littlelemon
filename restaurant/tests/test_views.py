from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        coffee = Menu.objects.create(title='Coffee', price=2.99, inventory=29)
        water = Menu.objects.create(title='Water', price=3.99, inventory=39)
        soda = Menu.objects.create(title='Soda', price=1.99, inventory=19)
    
    def test_get_all(self):
        count = Menu.objects.count()
        self.assertEqual(3, count)
