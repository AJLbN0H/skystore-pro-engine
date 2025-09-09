from .models import Product

from .models import Category

def categories_processor(request):
    return {'all_categories': Category.objects.all()}


class ProductService:

    @staticmethod
    def output_list_of_products_in_the_specified_category(category_id):
        products = Product.objects.filter(category_id=category_id)
        if not products.exists():
            return None
        return products