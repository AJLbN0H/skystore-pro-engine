from django.urls import path
from catalog.views import ProductDetailView, ProductListView, HomeTemplatesView, ContactsTemplateView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeTemplatesView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='home_page')
]