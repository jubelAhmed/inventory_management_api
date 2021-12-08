from django.test import TestCase

# Create your tests here.


import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Inventory, Supplier
from .serializers import InventorySerializer, InventoryFilterSerializer


# initialize the APIClient app
client = Client()


class GetAllInventoryTest(TestCase):
    """ Test module for GET all experiments API """

    def setUp(self):
        sp = Supplier.objects.create(name="Jubel Ahmed")
        Inventory.objects.create(
            name='Inventory 1', description='Inventory product number 1', note="THis is note",stock=20,availability=True,supplier=sp)

    def test_get_all_inventory(self):
        # get API response
        response = client.get('/inventory/')
        # get data from db
        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_get_all_api_inventory(self):
        # get API response
        response = client.get('/api/inventory/')
        # get data from db
        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_all_filter_api_inventory(self):
        # get API response
        response = client.get('/api/inventory/?name=Inventory 1')
        # get data from db
        inventories = Inventory.objects.all()
        serializer = InventoryFilterSerializer(inventories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_single_inventory(self):
        # get API response
        response = client.get('/inventory/1')
        # get data from db
        inventory = Inventory.objects.get(pk=1)
        serializer = InventorySerializer(inventory)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

