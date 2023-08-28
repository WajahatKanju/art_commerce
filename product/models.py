"""
This module defines the database models for the Product app.

The Product app includes models for managing product categories and individual products.

Models:
- Category: Represents a product category.
- Product: Represents an individual product, including its name, description, price,\
  stock quantity, and category.

Each model provides a user-friendly string representation for use in the admin panel\
  and other contexts.

Example:
    To create a new product category, you can use the Category model\
        as follows:
    >>> category = Category.objects.create(name="Electronics")
    To create a new product Brand, you can use the Brand model\
        as follows:
    >>> brand = Brand.objects.create(name="nike")
    To create a new product belonging to a category, you can use the Product model\
        as follows:
    >>> product = Product.objects.create(
    ...     name="Smartphone",
    ...     description="A high-end smartphone with advanced features.",
    ...     price=799.99,
    ...     stock_quantity=100,
    ...     category=category
    ... )
"""

from django.db import models
from taggit.managers import TaggableManager


class Brand(models.Model):
    """
    Model representing a product Brand.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    """
    Model representing a product category.
    """

    name = models.CharField(max_length=100)

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
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """
    Model representing a product.
    """

    # Product Information
    product_name = models.CharField(max_length=255)
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

    # Product Description
    description = models.TextField(blank=True, null=True)

    class Meta:
        """
        Meta options for the Product model.

        Attributes:
            verbose_name_plural (str): The plural name to display in the admin panel.
        """

        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.product_name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    is_thumbnail = models.BooleanField()
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"Image for {self.product.product_name}"


class ProductVideo(models.Model):
    product = models.ForeignKey(
        Product, related_name="videos", on_delete=models.CASCADE
    )
    video_provider = models.ForeignKey(VideoProvider, on_delete=models.CASCADE)
    video_link = models.URLField(max_length=255, blank=True, null=True)
    # You can add other fields like a caption or description for the image if needed

    def __str__(self):
        return f"{self.video_provider}: {self.video_link}"


class Color(models.Model):
    name = models.CharField(max_length=12)
    color_code = models.CharField(verbose_name="Hexadecimal Color Code", max_length=8)

    def __str__(self):
        return f"{self.name}"


class Attribute(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}"


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color, verbose_name="Available Colors")
    attributes = models.ManyToManyField(Attribute, verbose_name="Available Attributes")

    def __str__(self):
        return f"ProductVariation ID: {self.pk}"


class ProductPrice(models.Model):
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    attributes = models.ManyToManyField(Attribute, verbose_name="Attributes")
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    discount_start_date = models.DateField(blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return f"Price for ProductVariation ID: {self.product_variation}"
