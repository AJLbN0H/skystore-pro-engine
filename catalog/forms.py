from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Загрузите фотографию продукта"}
        )
        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите категорию продукта"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )

    def clean_name(self):

        name = self.cleaned_data.get("name")
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"В названии есть запрещенное слово: {name}")
        return name

    def clean_description(self):

        description = self.cleaned_data.get("description")
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(
                    f"В описании есть запрещенное слово: {description}"
                )
        return description

    def clean_price(self):

        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError(f"Цена не мржет быть отрицательной")
        return price
