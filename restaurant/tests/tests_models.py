from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
  def test_get_item(self):
    '''
    Test the creation of a menu item in the Menu model
    '''
    item = Menu.objects.create(
      name="Caramel Sundae", 
      price=80.99, 
      inventory=100,
      menu_item_description="A delightful sundae with caramel sauce and whipped cream."
    )
    
    # Call __str__ method to get the string representation of the object
    item_str = str(item)

    # Check if the fields are set correctly after creation
    self.assertEqual(item_str, "Caramel Sundae : 80.99")
    self.assertEqual(item.inventory, 100)
    self.assertEqual(item.menu_item_description,"A delightful sundae with caramel sauce and whipped cream." )