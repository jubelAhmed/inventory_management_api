from django.shortcuts import render

# Create your views here.

from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Inventory, Supplier
from .serializers import InventorySerializer, SupplierSerializer, InventoryFilterSerializer
from rest_framework.response import Response



class InventoryAPIView(APIView):
	
    # READ a single Todo
    
    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
       

        if pk:
            data = self.get_object(pk)
            serializer = InventorySerializer(data)

        else:
            data = Inventory.objects.all()
            serializer = InventorySerializer(data, many=True)

        
        return Response(serializer.data)
    

class InventoryFilterSupportAPIView(APIView):

    def get(self, request):
        name = request.query_params.get("name")

        if(name):
            data = Inventory.objects.filter(name=name)
            serializer = InventoryFilterSerializer(data, many=True)
        else:
            data = Inventory.objects.all()
            
            serializer = InventorySerializer(data, many=True)

        
        return Response(serializer.data)
    


