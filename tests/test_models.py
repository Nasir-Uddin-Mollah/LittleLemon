from django.test import TestCase

from restaurant.models import Menu


class MenuTest(TestCase):
    def test_menu_string_representation(self):
        menu = Menu.objects.create(
            title='Pizza',
            price=12.50,
            inventory=10,
        )

        self.assertEqual(str(menu), 'Pizza')