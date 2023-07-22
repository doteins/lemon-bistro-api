from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.views import MenuView
from restaurant.serializers import menuSerializer
from operator import itemgetter

class MenuViewTest(TestCase):
  def setUp(self):
    self.item_data1 = {
      'name': 'Chocolate Brownie',
      'price': 50.99,
      'inventory': 60,
      'menu_item_description': 'A scrumptious sundae with gooey chocolate brownie, ice cream, and toppings.',
    }

    self.item_data2 = {
      'name': 'Strawberry Cheesecake Shake',
      'price': 85.00,
      'inventory': 30,
      'menu_item_description': 'A refreshing shake with strawberries and creamy cheesecake flavor.',
    }

    self.item_data1 = Menu.objects.create(**self.item_data1)
    self.item_data2 = Menu.objects.create(**self.item_data2)

  def test_getall(self):
    client = RequestFactory()
    url = reverse('menu')

    # Make a GET req to retrieve all menu items
    req = client.get(url)
    res = MenuView.as_view()(req)

    # Serialization
    menu_items = Menu.objects.all().order_by('id')
    serializer = menuSerializer(menu_items, many=True)

    # Extract the relevant data from the response
    # as the pagination adds metadata to the response
    response_data = res.data['results']
    expected_data = serializer.data

    # Sort the serialized data by 'id' for consistent ordering
    sorted_response_data = sorted(response_data, key=itemgetter('id'))
    sorted_expected_data = sorted(expected_data, key=itemgetter('id'))

    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(sorted_response_data, sorted_expected_data)

