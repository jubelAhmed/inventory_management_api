from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('inventory', views.InventoryAPIView.as_view())


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('inventory/', views.InventoryAPIView.as_view(),name="inventory"),
    path('api/inventory/', views.InventoryFilterSupportAPIView.as_view(),name='apiinventory'),
    path('inventory/<int:pk>', views.InventoryAPIView.as_view(),name="single-inventory")
    
]