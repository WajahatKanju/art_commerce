"""
This module defines the database models for the Product app.

The Product app includes models for managing product categories and individual products.

Models:
- Category: Represents a product category.
- Brand: Represents a product brand.
- Product: Represents an individual product, including its name, description, price,
  stock quantity, and category.
- ProductImage: Represents an image associated with a product.
- ProductVideo: Represents a video associated with a product.
- Attribute: Represents an attribute.
- ProductVariation: Represents a product variation.
- ProductPrice: Represents the price information for a product variation.

Each model provides a user-friendly string representation for use in the admin panel
and other contexts.

Example Usage:
To create a new product category, you can use the Category model as follows:
>>> category = Category.objects.create(name="Electronics")

To create a new product brand, you can use the Brand model as follows:
>>> brand = Brand.objects.create(name="nike")

To create a new product belonging to a category, you can use the Product model as\
    follows:
>>> product = Product.objects.create(
...     name="Smartphone",
...     category=category,
...     brand=brand,
...     weight=0.2,  # Weight in kilograms
...     min_purchase_qty=10,
...     tags=["electronics", "smartphone"],
...     barcode="123456789",
...     refundable=True,
...     description="A high-end smartphone with advanced features."
... )

To add an image to a product, you can use the ProductImage model as follows:
>>> image = ProductImage.objects.create(
...     product=product,
...     is_thumbnail=True,
...     image="path/to/your/image.jpg"
... )

To add a video to a product, you can use the ProductVideo model as follows:
>>> video_provider = VideoProvider.objects.create(name="YouTube")
>>> video = ProductVideo.objects.create(
...     product=product,
...     video_provider=video_provider,
...     video_link="https://www.youtube.com/watch?v=your_video_id"
... )

To define available attributes for a product variation, you can use the
ProductVariation model as follows:
>>> variation = ProductVariation.objects.create(product=product)
>>> variation.attributes.add(attribute1, attribute2)  # Add available attributes

To set the price and discount information for a product variation, you can use the
ProductPrice model as follows:
>>> price = ProductPrice.objects.create(product_variation=variation, unit_price=599.99)
>>> price.attributes.add(attribute1, attribute2)  # Add associated attributes
>>> price.discount_start_date = "2023-01-01"  # Set discount start date
>>> price.discount_end_date = "2023-01-15"  # Set discount end date
>>> price.discount = 10.0  # Set discount percentage
>>> price.save()
"""
from django.db import models
from taggit.managers import TaggableManager
from wagtail.snippets.models import register_snippet


class Brand(models.Model):
    """
    Model representing a product Brand.
    """

    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    """
    Model representing a product category.
    """

    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        """
        Meta options for the Category model.

        Attributes:
            verbose_name_plural (str): The plural name to display in the admin panel.
        """

        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class VideoProvider(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """
    Model representing a product.
    """

    # Product Information
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name="weight in Kg(Kilograms)",
    )
    min_purchase_qty = models.PositiveIntegerField()

    tags = TaggableManager()

    barcode = models.CharField(max_length=50, blank=True, null=True)
    refundable = models.BooleanField(default=False)

    base_price = models.DecimalField(max_digits=8, decimal_places=2)

    # Product Description
    description = models.TextField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        """
        Meta options for the Product model.

        Attributes:
            verbose_name_plural (str): The plural name to display in the admin panel.
        """

        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    is_thumbnail = models.BooleanField()
    image = models.ImageField(upload_to="product_images/")
    description = models.TextField(max_length=12)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Image for {self.product}"


class ProductVideo(models.Model):
    product = models.ForeignKey(
        Product, related_name="videos", on_delete=models.CASCADE
    )
    video_provider = models.ForeignKey(VideoProvider, on_delete=models.CASCADE)
    video_link = models.URLField(max_length=255, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # You can add other fields like a caption or description for the image if needed

    def __str__(self):
        return f"{self.video_provider}: {self.video_link}"


@register_snippet
class Attribute(models.Model):
    name = models.CharField(max_length=15)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


@register_snippet
class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=15)

    def __str__(self):
        return self.value


class ProductVariation(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variations",
    )
    attributes = models.ForeignKey(
        Attribute,
        related_name="attribute",
        on_delete=models.CASCADE,
    )
    attribute_value = models.ForeignKey(
        AttributeValue,
        related_name="attribute_values",
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"ProductVariation ID: {self.pk}"


class ProductPrice(models.Model):
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    discount_start_date = models.DateField(blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Price for ProductVariation ID: {self.product_variation}"
