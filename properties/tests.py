from django.test import TestCase
from django.urls import reverse
from .models import Property

class PropertyViewTests(TestCase):
    def setUp(self):
        # This method runs before every test
        Property.objects.create(
            title="Test Property",
            description="A lovely test property",
            price=500000.00,
            location="Nairobi"
        )

    def test_property_list_returns_200(self):
        """Test that /api/property-list/ endpoint works"""
        response = self.client.get(reverse('properties')) # uses name from urls.py
        self.assertEqual(response.status_code, 200)

    def test_property_list_returns_data(self):
        """Test that the response includes the test property"""
        response = self.client.get(reverse('properties'))
        self.assertContains(response, "Test Property")

