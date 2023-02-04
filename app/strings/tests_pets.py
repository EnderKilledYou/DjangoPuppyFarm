from django.test import TestCase
from django.urls import reverse
from django_factory_boy.auth import UserFactory
from rest_framework import status

from app.strings.pets import PetFactory, Pet


class PetViewSetTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(email='testuser@example.com')
        self.user.set_password('testpassword')
        self.user.save()
        self.client.login(email=self.user.email, password='testpassword')
        self.list_url = reverse('Pet-list')
        self.Pet = Pet

    def test_post(self):
        """POST to create a Pet."""
        data = {
            'name': 'New name',
            'description': 'New description',

        }
        self.assertEqual(self.Pet.objects.count(), 0)
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.Pet.objects.count(), 1)
        Pet = self.Pet.objects.all().first()
        for field_name in data.keys():
            self.assertEqual(getattr(Pet, field_name), data[field_name])

    def test_put(self):
        """PUT to update a Pet."""
        Pet = PetFactory()
        data = {
            'name': 'New name',
            'description': 'New description',
            'street_line_1': 'New street_line_1',
            'city': 'New City',
            'state': 'NY',
            'zipcode': '12345',
        }
        response = self.client.put(
            self.get_detail_url(Pet.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # The object has really been updated
        Pet.refresh_from_db()
        for field_name in data.keys():
            self.assertEqual(getattr(Pet, field_name), data[field_name])

    def test_patch(self):
        """PATCH to update a Pet."""
        Pet = PetFactory()
        data = {'name': 'New name'}
        response = self.client.patch(
            self.get_detail_url(Pet.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # The object has really been updated
        Pet.refresh_from_db()
        self.assertEqual(Pet.name, data['name'])

    def test_delete(self):
        """DELETEing is not implemented."""
        Pet = PetFactory()
        response = self.client.delete(self.get_detail_url(Pet.id))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
