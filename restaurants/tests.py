import json

from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
from restaurants.models import Restaurant

valid_restaurant = {
    "name": "Crazy Pizza",
    "address": "Crazy Street 0",
    "city": "Crazyland"
}

new_restaurant = {
    "name": "Crazy New",
    "address": "Crazy Street 9999",
    "city": "Crazyburg"
}


class TestRestaunt(TestCase):

    def setUp(self):
        Restaurant.objects.create(**valid_restaurant)
        self.client = APIClient()

    def tearDown(self):
        Restaurant.objects.filter().delete()

    def test_list_restaurants_must_return_200_OK(self):
        response = self.client.get('/api/v1/restaurants/')
        self.assertEqual(response.status_code, 200)

    def test_should_return_empty_list_if_there_is_no_restaurants(self):
        Restaurant.objects.filter().delete()
        response = self.client.get('/api/v1/restaurants/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_list_restaurants_must_contain_a_list_of_valid_JSON_objects(self):
        response = self.client.get('/api/v1/restaurants/')
        self.assertIsInstance(response.data, list)

    def test_returns_a_list_of_valid_restaurant_objects_as_JSON(self):
        response = self.client.get('/api/v1/restaurants/')
        self.assertEqual(response.data[0], valid_restaurant)

    def test_adding_a_new_restaurant_must_return_201_CREATED(self):
        response = self.client.post('/api/v1/restaurants/', data=new_restaurant, format='json')
        self.assertEqual(response.status_code, 201)

    def test_if_after_adding_a_new_restaurant_it_must_appear_in_the_restaurant_list(self):
        response = self.client.get('/api/v1/restaurants/')
        self.assertNotIn(new_restaurant, response.data)

        response = self.client.post('/api/v1/restaurants/', data=new_restaurant, format='json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/v1/restaurants/')

        self.assertIn(new_restaurant, response.data)

    def test_should_return_400_if_invalid_data_id_given(self):
        response = self.client.post('/api/v1/restaurants/', data={"thisis": "invalid"}, format='json')
        self.assertEqual(response.status_code, 400)

    def test_should_return_405_if_calling_DELETE(self):
        response = self.client.delete('/api/v1/restaurants/')
        self.assertEqual(response.status_code, 405)

    def test_should_return_405_if_calling_PUT(self):
        response = self.client.put('/api/v1/restaurants/')
        self.assertEqual(response.status_code, 405)

    # def test_list_restaurants_must_return_403_FORBIDDEN_if_not_amdin(self):
    #     client = APIClient()
    #     response = client.get('/api/v1/restaurants')
    #     self.assertEqual(response.status_code, 403)
