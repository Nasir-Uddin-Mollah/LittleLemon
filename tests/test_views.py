from django.test import TestCase
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        Menu.objects.create(
            title='Pizza',
            price=12.50,
            inventory=10,
        )
        Menu.objects.create(
            title='Pasta',
            price=15.00,
            inventory=8,
        )

    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/items/')

        menu_items = Menu.objects.all()
        serialized_items = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_items.data)