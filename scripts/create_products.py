from product.models import (
    Category,
    Brand,
    Product,
    ProductImage,
    ProductVideo,
    Attribute,
    AttributeValue,
    ProductVariation,
    ProductPrice,
    VideoProvider,
)

# Create Categories
category, created = Category.objects.get_or_create(name="Electronics")

# Create Brands
brand, created = Brand.objects.get_or_create(name="Nike")

# Create Video Provider
video_provider, created = VideoProvider.objects.get_or_create(name="YouTube")

# Create Product
product, created = Product.objects.get_or_create(
    name="Smartphone",
    category=category,
    brand=brand,
    weight=0.2,
    min_purchase_qty=10,
    barcode="123456789",
    refundable=True,
    description="A high-end smartphone with advanced features.",
)

# Create Product Image
product_image, created = ProductImage.objects.get_or_create(
    product=product,
    is_thumbnail=True,
    image="path/to/your/image.jpg",
    description="Thumbnail image",
)

# Create Product Video
product_video, created = ProductVideo.objects.get_or_create(
    product=product,
    video_provider=video_provider,
    video_link="https://www.youtube.com/watch?v=your_video_id",
)


# Create Attributes
size_attribute, created = Attribute.objects.get_or_create(name="size")
color_attribute, created = Attribute.objects.get_or_create(name="color")


# Create attribute values
small_value = AttributeValue.objects.get_or_create(
    attribute=size_attribute, value="S"
)
medium_value = AttributeValue.objects.get_or_create(
    attribute=size_attribute, value="M"
)
large_value = AttributeValue.objects.get_or_create(
    attribute=size_attribute, value="L"
)
extra_large_value = AttributeValue.objects.get_or_create(
    attribute=size_attribute, value="XL"
)

red_value = AttributeValue.objects.get_or_create(
    attribute=color_attribute, value="red"
)
green_value = AttributeValue.objects.get_or_create(
    attribute=color_attribute, value="green"
)
blue_value = AttributeValue.objects.get_or_create(
    attribute=color_attribute, value="indigo"
)


# Create product variations and associate them with attributes
variation1, created = ProductVariation.objects.get_or_create(product=product)
variation1.attributes.add(size_attribute)
variation1.attributes.add(color_attribute)

# variation2 = ProductVariation.objects.get_or_create(product=product)
# variation2.attributes.add(
#     AttributeValue.objects.get(attribute=size_attribute, value="M")
# )
# variation2.attributes.add(
#     AttributeValue.objects.get(attribute=color_attribute, value="green")
# )
