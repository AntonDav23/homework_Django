from django.core.exceptions import ValidationError
from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    def clean(self):
        cleaned_data = super().clean()
        forbidden_words = [
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
        name = cleaned_data.get("name", "")
        description = cleaned_data.get("description", "")
        for word in forbidden_words:
            if word in name.lower():
                self.add_error(
                    "name",
                    f"Название содержит запрещённое слово: {word}",
                )
            if word in description.lower():
                self.add_error(
                    "description",
                    f"Название содержит запрещённое слово: {word}",
                )
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and hasattr(image, "content_type"):
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Размер изображения не должен превышать 5 МБ.")
            if image.content_type not in ["image/jpeg", "image/png"]:
                raise ValidationError("Допустимые форматы изображения: JPEG и PNG.")
            return image
