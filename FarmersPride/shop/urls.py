from django.urls import path
from .views import showcategories, showproducts

urlpatterns = [

    path('shop/', showcategories, name='shop'),
    path('showproducts/<slug:category>', showproducts),
]
