from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import ProductForm
from .models import Product


class HomeTemplatesView(TemplateView):
    template_name = "catalog/home.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = "product"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    context_object_name = "products"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
