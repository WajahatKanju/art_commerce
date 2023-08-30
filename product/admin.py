"""
This file contains the admin classes for the `Brand`, `Category`, and `Product` models.

The `BrandAdmin` class defines the settings for the `Brand` model in the Wagtail admin \
    interface.
The `CategoryAdmin` class defines the settings for the `Category` model in the Wagtail \
    admin interface.
The `ProductAdmin` class defines the settings for the `Product` model in the Wagtail \
    admin interface.
The `MyModelAdminGroup` class groups the `BrandAdmin`, `CategoryAdmin`, and \
    `ProductAdmin` together in the Wagtail admin interface.
"""

from wagtail_modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from django.utils.html import format_html
from .models import (
    Brand,
    Category,
    Product,
    VideoProvider,
    ProductImage,
    ProductVideo,
    ProductVariation,
    ProductPrice,
)


class ProductAdmin(ModelAdmin):
    """
    Admin class for the `Product` model.

    `menu_label` specifies the label for the admin menu item.
    `menu_icon` specifies the Font Awesome icon for the admin menu item.
    `list_display` specifies the columns displayed on the list view.
    """

    model = Product
    menu_label = "Products"
    menu_icon = "spinner"
    list_filter = ("category", "brand")

    list_display = (
        "name",
        "category",
        "brand",
        "prices",
        "created_at",
        "updated_at",
        "product_image",
        "product_video",
    )

    def product_image(self, obj):
        try:
            product_image = obj.images.get(is_thumbnail=True)
            if product_image.image.url:
                return format_html(
                    '<img src="{}" style="max-height: 100px; margin: 5px;" />',
                    product_image.image.url,
                )
        except ProductImage.DoesNotExist:
            pass

        return "None"

    def product_video(self, obj):
        # Check if there's a related ProductVideo with a video link
        try:
            product_video = obj.videos.get()
            if product_video.video_link:
                return format_html(
                    '<span>{}:&nbsp;<a href="{}" target="_blank">Video Link</a></span>',
                    product_video.video_provider,
                    product_video.video_link,
                )
        except ProductVideo.DoesNotExist:
            pass

        return "No Video Link"

    def prices(self, obj):
        # Get related ProductVariation instances for the current Product
        variations = obj.variations.all()

        # Create a string with price information
        price_info = ""
        for variation in variations:
            prices = variation.productprice_set.all()
            for price in prices:
                price_info += f"Attributes:\
                    {', '.join(attr.name for attr in price.attributes.all())}<br>"
                price_info += f"Unit Price: {price.unit_price}<br>"
                price_info += f"Discount: {price.discount}%<br>"
                price_info += f"Discount Start Date: {price.discount_start_date}<br>"
                price_info += f"Discount End Date: {price.discount_end_date}<br>"
                price_info += "<br>"

        if price_info:
            return format_html(price_info)
        else:
            return "Not Available"


class BrandAdmin(ModelAdmin):
    """
    Admin class for the `Brand` model.

    `menu_label` specifies the label for the admin menu item.
    `menu_icon` specifies the Font Awesome icon for the admin menu item.
    `list_display` specifies the columns displayed on the list view.
    """

    model = Brand
    menu_label = "Brands"
    menu_icon = "spinner"
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )


class CategoryAdmin(ModelAdmin):
    """
    Admin class for the `Category` model.

    `menu_label` specifies the label for the admin menu item.
    `menu_icon` specifies the Font Awesome icon for the admin menu item.
    `list_display` specifies the columns displayed on the list view.
    """

    model = Category
    menu_label = "Categories"
    menu_icon = "spinner"
    list_display = ("name", "created_at", "updated_at")


class VideoProviderAdmin(ModelAdmin):
    model = VideoProvider
    menu_label = "Video Provider"
    menu_icon = "spinner"
    list_display = ("name", "created_at", "updated_at")
    list_filter = ("name",)
    search_fields = ("name",)


class ProductImageAdmin(ModelAdmin):
    model = ProductImage
    menu_label = "Product Images"
    menu_icon = "image"  # You can choose an appropriate icon
    list_filter = ("product", "is_thumbnail")
    list_display = ("product", "is_thumbnail", "image_thumbnail", "description")

    def image_thumbnail(self, obj):
        # This method generates a thumbnail
        #  preview for the image in the admin list view.
        if obj.image:
            return f'<img src="{obj.image.url}" \
                style="max-width: 100px; max-height: 100px;" />'
        else:
            return "No Image"

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Thumbnail"


class ProductVideoAdmin(ModelAdmin):
    model = ProductVideo
    menu_label = "Product Video"
    menu_icon = "spinner"
    list_display = ("video_provider", "video_link", "created_at", "updated_at")


class ProductVariationAdmin(ModelAdmin):
    model = ProductVariation
    menu_label = "Product Variation"
    menu_icon = "spinner"

    list_display = ("product", "attributes", "attribute_value", "created_at")


class ProductPriceAdmin(ModelAdmin):
    model = ProductPrice
    list_display = (
        "id",
        "product_variation",
        "get_attributes",
        "unit_price",
        "discount_start_date",
        "discount_end_date",
        "discount",
        "created_at",
        "updated_at",
    )

    def get_attributes(self, obj):
        return ", ".join([attr.name for attr in obj.attributes.all()])

    get_attributes.short_description = "Attributes"


# Create a ModelAdminGroup to group these ModelAdmins together
class MyModelAdminGroup(ModelAdminGroup):
    """
    ModelAdminGroup that groups the BrandAdmin, CategoryAdmin, and ProductAdmin.

    `menu_label` specifies the label for the admin menu item.
    `menu_icon` specifies the Font Awesome icon for the admin menu item.
    `items` specifies the list of ModelAdmins that should be grouped together.
    """

    menu_label = "Product"
    menu_icon = "desktop"
    items = (
        ProductAdmin,
        BrandAdmin,
        CategoryAdmin,
        VideoProviderAdmin,
        ProductImageAdmin,
        ProductVideoAdmin,
        ProductVariationAdmin,
        ProductPriceAdmin,
    )


# Register the ModelAdminGroup
modeladmin_register(MyModelAdminGroup)
