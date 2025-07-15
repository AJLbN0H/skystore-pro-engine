from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    help = "Добавяет тестовые данные в базу данных для модуля Product"

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category1, _ = Category.objects.get_or_create(
            name="Мясная продукция", description="мясо"
        )
        category2, _ = Category.objects.get_or_create(
            name="Шоколадная продукция", description="шоколад"
        )

        products = [
            {
                "name": "Свинина",
                "description": "жареная свинка",
                "category": category1,
                "price": 1,
            },
            {
                "name": "Шоколад бабаевский",
                "description": "горький шоколад",
                "category": category2,
                "price": 2,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Продукт добавлен: {product.name}")
                )
