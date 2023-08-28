from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from .models import Brand, Category, Product


class BrandAdmin(ModelAdmin):
    model = Brand
    menu_label = "Brands"  # Label for the admin menu item
    menu_icon = "placeholder"  # Font Awesome icon for the admin menu item
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )  # Columns displayed on the list view


class CategoryAdmin(ModelAdmin):
    model = Category
    menu_label = "Categories"
    menu_icon = "placeholder"
    list_display = ("name", "created_at", "updated_at")


class ProductAdmin(ModelAdmin):
    model = Product
    menu_label = "Products"
    menu_icon = "placeholder"
    list_display = ("name", "category", "brand", "price", "created_at", "updated_at")


# Create a ModelAdminGroup to group these ModelAdmins together
class MyModelAdminGroup(ModelAdminGroup):
    menu_label = "Products"
    menu_icon = "desktop"  # You can choose a different icon if you prefer
    items = (BrandAdmin, CategoryAdmin, ProductAdmin)


# Register the ModelAdminGroup
modeladmin_register(MyModelAdminGroup)
