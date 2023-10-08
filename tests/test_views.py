from django.test import TestCase
from restaurant.models import Menu
from rest_framework import status


class MenuViewTest(TestCase):
    
    def setUp(self):
        menu_item = Menu.objects.create(title='Item1', price=80, inventory=100)
        menu_item.save()
        Menu.objects.create(title='Item2', price=80, inventory=100)
        Menu.objects.create(title='Item3', price=80, inventory=100)
        
    def test_get_all(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Menu.objects.count(), 3)
        self.assertEqual(len(response.data), 3)
        