from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    """Category model for different event services"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, help_text="External image URL (optional)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        """Return image URL, prioritizing uploaded image over external URL"""
        if self.image:
            return self.image.url
        return self.image_url or ''


class SubCategory(models.Model):
    """Subcategory model linked to main categories"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "SubCategories"
        ordering = ['name']

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Package(models.Model):
    """Readymade packages with pricing"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField(help_text="Enter features separated by new lines")
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_popular', 'price']

    def __str__(self):
        return self.name

    def get_features_list(self):
        """Return features as a list"""
        return [feature.strip() for feature in self.features.split('\n') if feature.strip()]


class VenueItem(models.Model):
    """Individual venue items"""
    SUBCATEGORY_CHOICES = [
        ('banquet_hall', 'Banquet Hall'),
        ('hotel', 'Hotel'),
        ('resort', 'Resort'),
        ('garden', 'Garden'),
        ('farmhouse', 'Farmhouse'),
        ('convention_center', 'Convention Center'),
    ]
    
    name = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(help_text="Maximum guest capacity")
    location = models.CharField(max_length=200)
    features = models.TextField(help_text="Features separated by new lines")
    main_image = models.ImageField(upload_to='venues/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['subcategory', 'name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while VenueItem.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def get_features_list(self):
        return [feature.strip() for feature in self.features.split('\n') if feature.strip()]


class VenueImage(models.Model):
    """Multiple images for each venue"""
    venue = models.ForeignKey(VenueItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='venues/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.venue.name} - Image {self.order}"


class JewelleryItem(models.Model):
    """Jewellery items for events"""
    SUBCATEGORY_CHOICES = [
        ('bridal_set', 'Bridal Set'),
        ('necklace', 'Necklace'),
        ('earrings', 'Earrings'),
        ('bangles', 'Bangles'),
        ('maang_tikka', 'Maang Tikka'),
        ('nose_ring', 'Nose Ring'),
    ]
    
    name = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES)
    description = models.TextField()
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100, help_text="Gold, Silver, Kundan, etc.")
    main_image = models.ImageField(upload_to='jewellery/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['subcategory', 'name']
        verbose_name_plural = "Jewellery Items"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while JewelleryItem.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class JewelleryImage(models.Model):
    """Multiple images for each jewellery item"""
    jewellery = models.ForeignKey(JewelleryItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='jewellery/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.jewellery.name} - Image {self.order}"


class FoodItem(models.Model):
    """Food/Catering items"""
    SUBCATEGORY_CHOICES = [
        ('veg_menu', 'Vegetarian Menu'),
        ('non_veg_menu', 'Non-Vegetarian Menu'),
        ('desserts', 'Desserts'),
        ('beverages', 'Beverages'),
        ('live_counter', 'Live Counter'),
        ('buffet', 'Buffet Package'),
    ]
    
    name = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES)
    description = models.TextField()
    price_per_plate = models.DecimalField(max_digits=10, decimal_places=2)
    cuisine_type = models.CharField(max_length=100, help_text="Indian, Chinese, Continental, etc.")
    serves = models.IntegerField(help_text="Number of people", default=1)
    main_image = models.ImageField(upload_to='food/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['subcategory', 'name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while FoodItem.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class FoodImage(models.Model):
    """Multiple images for each food item"""
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='food/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.food.name} - Image {self.order}"


class Favorite(models.Model):
    """User favorites for any item"""
    ITEM_TYPE_CHOICES = [
        ('venue', 'Venue'),
        ('jewellery', 'Jewellery'),
        ('food', 'Food'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    item_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'item_type', 'item_id']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.item_type} {self.item_id}"
