from django.urls import path 
from . import views


urlpatterns = [
    path('add-address', views.AddAddressApiView.as_view(), name="AddAddressApiView"),
    path('get-address', views.GetAddressApiView.as_view(), name="GetAddressApiView"),
    path('update-address', views.UpdateAddressApiView.as_view(), name="UpdateAddressApiView"),
    path('delete-address', views.DeleteAddressApiView.as_view(), name="DeleteAddressApiView"),
]