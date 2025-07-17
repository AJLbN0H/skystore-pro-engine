from django.urls import path
from catalog.views import home, contacts, product_detail, home_page

app_name = 'catalog'

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('', home_page, name='home_page')
]