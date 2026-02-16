from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    DetailView,
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import ProductForm
from .models import Product, Category
from .services import ProductService


class HomeTemplatesView(TemplateView):
    template_name = "catalog/home.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = "product"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get('product_list_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('product_list_queryset', queryset, 60 * 15)
        return queryset and Product.objects.filter(publication_sign=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def post(self, request, pk):
        product = get_object_or_404(self.model, pk=pk)
        true_publication_sign = request.POST.get("publication_sign") == "on"

        if product.publication_sign != true_publication_sign:
            if not request.user.has_perm("catalog.can_unpublish_product"):
                return HttpResponseForbidden("У вас нет прав для отмены публикации.")

            else:
                product.name = request.POST.get("name", product.name)
                product.description = request.POST.get(
                    "description", product.description
                )
                product.image = request.POST.get("image", product.image)
                if request.POST.get("category"):
                    product.category = Category.objects.get(
                        id=request.POST.get("category")
                    )
                product.price = request.POST.get("price", product.price)
                product.updated_at = request.POST.get("updated_at", product.updated_at)
                product.publication_sign = False
                product.save()
        else:
            product.name = request.POST.get("name", product.name)
            product.description = request.POST.get("description", product.description)
            product.image = request.POST.get("image", product.image)
            if request.POST.get("category"):
                product.category = Category.objects.get(id=request.POST.get("category"))
            product.price = request.POST.get("price", product.price)
            product.updated_at = request.POST.get("updated_at", product.updated_at)
            product.save()

        return redirect("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm("catalog.delete_product"):
            if self.request.user != product.owner:
                print(self.request.user)
                print(product.owner)
                return HttpResponseForbidden("У вас нет прав для удаления продукта.")

        product.delete()

        return redirect("catalog:product_list")


class ProductCategoryView(ListView):
    model = Product
    template_name = "catalog/product_category.html"
    context_object_name = 'products_category'

    def get_queryset(self):
        return ProductService.output_list_of_products_in_the_specified_category(self.kwargs['category_id'])

