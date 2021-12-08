from .models import Inventory, Supplier
from rest_framework import serializers


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['supplier'] = SupplierSerializer(instance.supplier).data
        return rep
    




class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name']
        
class InventoryFilterSerializer(serializers.HyperlinkedModelSerializer):
    # suppliers = SupplierSerializer(many=True, read_only=True)
    class Meta:
        model = Inventory
        fields = ['name','availability']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['supplier_name'] = SupplierSerializer(instance.supplier).data["name"]
        return rep
        