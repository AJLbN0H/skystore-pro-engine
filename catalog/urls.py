from django.urls import path
from catalog.views import (
    ProductDetailView,
    ProductListView,
    HomeTemplatesView,
    ContactsTemplateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, ProductCategoryView,
)

app_name = "catalog"

urlpatterns = [
    path("home/", HomeTemplatesView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path("", ProductListView.as_view(), name="product_list"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "product_category/<int:category_id>", ProductCategoryView.as_view(), name="product_category"
    ),
]
